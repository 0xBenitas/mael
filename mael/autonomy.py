"""Autonomy module — the loop generates its own tasks and self-heals.

This is the bridge to Level 5: the snake decides what to work on next.
Three capabilities:
  1. generate_tasks() — propose new tasks based on project state
  2. decompose_task() — break a failing task into smaller sub-tasks
  3. doctor() — diagnose and fix structural issues
"""

import json
import subprocess
from pathlib import Path

from .llm import ask_for_json, ask, SMART, FAST
from .state import load_state, save_state
from .memory import load_metrics, get_learnings, get_trend
from .prompts import SYSTEM_MAEL

MAEL_DIR = Path(".mael")


# ── Task Generation (Level 5) ───────────────────────────────────────

GENERATE_TASKS_PROMPT = """Tu es MAEL en mode AUTONOME. Tu dois proposer les prochaines tâches.

## État du projet
{project_summary}

## Tâches terminées
{completed_tasks}

## Learnings clés
{top_learnings}

## Métriques
Score moyen: {avg_score}, Tendance: {trend}

## Objectif du projet
{goal}

## Instructions
Propose 2-3 nouvelles tâches CONCRÈTES qui :
1. Améliorent le projet existant (refactor, tests, features)
2. Sont réalisables en 1-3 itérations chacune
3. S'appuient sur les learnings accumulés
4. Font progresser vers l'objectif

Chaque tâche doit être ATOMIQUE (un seul fichier, une seule responsabilité).

Réponds en JSON :
{{
  "reasoning": "pourquoi ces tâches",
  "tasks": [
    {{
      "title": "titre court",
      "description": "description précise avec chemins de fichiers",
      "acceptance": "critères mesurables de succès",
      "priority": "critical|high|medium"
    }}
  ]
}}
"""


def generate_tasks(goal: str = "") -> list[dict]:
    """Have the LLM propose next tasks based on project state."""
    state = load_state()
    metrics = load_metrics()
    trend = get_trend()
    learnings = get_learnings()

    completed = [t for t in state.get("tasks", []) if t["status"] == "completed"]
    completed_summary = "\n".join(
        f"- [{t['id']}] {t['title']}" for t in completed
    ) or "(aucune)"

    # Summarize project files
    project_summary = _scan_project()

    # Get top learnings (last 500 chars)
    top_learnings = learnings[-500:] if learnings else "(aucun)"

    prompt = GENERATE_TASKS_PROMPT.format(
        project_summary=project_summary,
        completed_tasks=completed_summary,
        top_learnings=top_learnings,
        avg_score=metrics["aggregate"].get("avg_score", 0),
        trend=trend.get("direction", "no data"),
        goal=goal or state.get("meta", {}).get("goal", "Améliorer le projet"),
    )

    raw = ask_for_json(prompt, system=SYSTEM_MAEL, model=SMART, max_tokens=2048)
    data = _safe_json(raw, {"tasks": []})

    # Assign IDs
    max_id = max((t["id"] for t in state.get("tasks", [])), default=0)
    new_tasks = []
    for i, t in enumerate(data.get("tasks", []), start=max_id + 1):
        new_tasks.append({
            "id": i,
            "title": t.get("title", f"Task {i}"),
            "description": t.get("description", ""),
            "acceptance": t.get("acceptance", ""),
            "status": "pending",
            "priority": t.get("priority", "medium"),
        })

    return new_tasks


def add_generated_tasks(goal: str = "") -> list[dict]:
    """Generate tasks and add them to state.json."""
    tasks = generate_tasks(goal)
    if not tasks:
        return []

    state = load_state()
    state["tasks"].extend(tasks)
    state["status"] = "running"
    save_state(state)
    return tasks


# ── Task Decomposition ───────────────────────────────────────────────

DECOMPOSE_PROMPT = """Une tâche échoue après {n_failures} tentatives.

## Tâche qui échoue
Titre: {title}
Description: {description}
Dernier score: {last_score}
Dernière critique: {critique}

## Instructions
Décompose cette tâche en 2-3 sous-tâches plus petites.
Chaque sous-tâche doit être faisable en UNE itération.
Chaque sous-tâche doit produire UN SEUL fichier de max 100 lignes.

Réponds en JSON :
{{
  "analysis": "pourquoi ça échoue",
  "subtasks": [
    {{
      "title": "sous-tâche",
      "description": "description avec chemin du fichier",
      "acceptance": "critère simple"
    }}
  ]
}}
"""


def decompose_task(task: dict, critique: str = "", last_score: float = 0) -> list[dict]:
    """Break a failing task into smaller sub-tasks."""
    state = load_state()

    # Count failures for this task
    metrics = load_metrics()
    failures = sum(
        1 for m in metrics["iterations"]
        if m.get("task_id") == task["id"] and m["verdict"] == "FAIL"
    )

    prompt = DECOMPOSE_PROMPT.format(
        n_failures=failures,
        title=task["title"],
        description=task["description"],
        last_score=last_score,
        critique=critique[:500],
    )

    raw = ask_for_json(prompt, system=SYSTEM_MAEL, model=FAST, max_tokens=1024)
    data = _safe_json(raw, {"subtasks": []})

    max_id = max((t["id"] for t in state.get("tasks", [])), default=0)
    subtasks = []
    for i, st in enumerate(data.get("subtasks", []), start=max_id + 1):
        subtasks.append({
            "id": i,
            "title": st.get("title", f"Subtask {i}"),
            "description": st.get("description", ""),
            "acceptance": st.get("acceptance", ""),
            "status": "pending",
            "priority": task.get("priority", "high"),
            "parent_id": task["id"],
        })

    return subtasks


# ── Doctor Mode ──────────────────────────────────────────────────────

def doctor() -> dict:
    """Self-diagnose and fix structural issues. Returns a report."""
    report = {"checks": [], "fixes": [], "healthy": True}

    # Check 1: .mael structure
    for f in ["state.json", "learnings.md", "metrics.json", "mutations.md"]:
        path = MAEL_DIR / f
        if path.exists():
            report["checks"].append(f"OK: {f} exists")
        else:
            report["checks"].append(f"MISSING: {f}")
            report["healthy"] = False

    # Check 2: state.json is valid JSON
    try:
        state = load_state()
        n_tasks = len(state.get("tasks", []))
        report["checks"].append(f"OK: state.json valid ({n_tasks} tasks)")
    except Exception as e:
        report["checks"].append(f"BROKEN: state.json — {e}")
        report["healthy"] = False

    # Check 3: metrics.json is valid
    try:
        metrics = load_metrics()
        n = metrics["aggregate"].get("total_iterations", 0)
        report["checks"].append(f"OK: metrics.json valid ({n} iterations)")
    except Exception as e:
        report["checks"].append(f"BROKEN: metrics.json — {e}")
        report["healthy"] = False

    # Check 4: tests pass
    try:
        result = subprocess.run(
            ["python", "-m", "pytest", "tests/", "-q", "--tb=no"],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode == 0:
            report["checks"].append(f"OK: tests pass — {result.stdout.strip().split(chr(10))[-1]}")
        else:
            report["checks"].append(f"FAIL: tests — {result.stdout.strip().split(chr(10))[-1]}")
            report["healthy"] = False
    except Exception as e:
        report["checks"].append(f"ERROR: tests — {e}")

    # Check 5: stuck tasks (in_progress for too long)
    state = load_state()
    metrics = load_metrics()
    for task in state.get("tasks", []):
        if task["status"] == "in_progress":
            failures = sum(
                1 for m in metrics["iterations"]
                if m.get("task_id") == task["id"] and m["verdict"] == "FAIL"
            )
            if failures >= 3:
                report["checks"].append(
                    f"STUCK: Task #{task['id']} '{task['title']}' — {failures} failures"
                )
                report["fixes"].append({
                    "action": "decompose",
                    "task_id": task["id"],
                    "reason": f"{failures} consecutive failures",
                })
                report["healthy"] = False

    # Check 6: CLAUDE.md exists and has patterns
    claude_md = Path("CLAUDE.md")
    if claude_md.exists():
        content = claude_md.read_text(encoding="utf-8")
        n_patterns = content.count("- **[")
        report["checks"].append(f"OK: CLAUDE.md has {n_patterns} patterns")
    else:
        report["checks"].append("MISSING: CLAUDE.md")
        report["healthy"] = False

    return report


# ── Helpers ──────────────────────────────────────────────────────────

def _scan_project() -> str:
    """Quick scan of project structure."""
    lines = []
    for ext in ("*.py", "*.md", "*.json"):
        for p in sorted(Path(".").rglob(ext)):
            if ".mael/logs" in str(p) or "__pycache__" in str(p):
                continue
            try:
                size = p.stat().st_size
                lines.append(f"  {p} ({size}b)")
            except OSError:
                pass
    return "\n".join(lines[:30]) or "(empty project)"


def _safe_json(raw: str, default: dict) -> dict:
    """Parse JSON with fallback."""
    text = raw.strip()
    if text.startswith("```"):
        text = "\n".join(text.split("\n")[1:])
        if text.endswith("```"):
            text = text[:-3]
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return default
