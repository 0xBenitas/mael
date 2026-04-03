"""Persistent memory management — learnings, metrics, CLAUDE.md."""

import json
import re
from pathlib import Path
from datetime import datetime

MAEL_DIR = Path(".mael")
LEARNINGS_FILE = MAEL_DIR / "learnings.md"
METRICS_FILE = MAEL_DIR / "metrics.json"
MUTATIONS_FILE = MAEL_DIR / "mutations.md"
CLAUDE_MD = Path("CLAUDE.md")


# ── Learnings ────────────────────────────────────────────────────────

def add_learning(iteration: int, category: str, context: str,
                 learning: str, confidence: str = "moyenne") -> None:
    """Append a new learning entry to learnings.md."""
    date = datetime.now().strftime("%Y-%m-%d")
    entry = (
        f"\n### [{date}] Iteration {iteration} — {category}\n"
        f"**Contexte** : {context}\n"
        f"**Learning** : {learning}\n"
        f"**Confiance** : {confidence}\n"
        f"**Utilisations** : 0\n"
    )
    LEARNINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LEARNINGS_FILE, "a", encoding="utf-8") as f:
        f.write(entry)


def get_learnings() -> str:
    """Read learnings file content."""
    if not LEARNINGS_FILE.exists():
        return ""
    return LEARNINGS_FILE.read_text(encoding="utf-8")


def increment_learning_usage(learning_text: str) -> int:
    """Find a learning by text, increment its usage count. Return new count."""
    if not LEARNINGS_FILE.exists():
        return 0
    content = LEARNINGS_FILE.read_text(encoding="utf-8")
    pattern = re.compile(
        r"(\*\*Learning\*\* : " + re.escape(learning_text) + r".*?"
        r"\*\*Utilisations\*\* : )(\d+)",
        re.DOTALL,
    )
    match = pattern.search(content)
    if not match:
        return 0
    new_count = int(match.group(2)) + 1
    content = content[: match.start(2)] + str(new_count) + content[match.end(2):]
    LEARNINGS_FILE.write_text(content, encoding="utf-8")
    return new_count


def promote_to_claude_md(learning: str) -> None:
    """Add a confirmed pattern to CLAUDE.md."""
    if not CLAUDE_MD.exists():
        return
    content = CLAUDE_MD.read_text(encoding="utf-8")
    marker = "## Patterns Confirmés"
    if marker not in content:
        return
    if learning in content:
        return  # already promoted
    date = datetime.now().strftime("%Y-%m-%d")
    insertion = f"\n- **[{date}]** {learning}"
    content = content.replace(
        marker,
        marker + insertion,
    )
    CLAUDE_MD.write_text(content, encoding="utf-8")


# ── Metrics ──────────────────────────────────────────────────────────

def load_metrics() -> dict:
    """Load metrics from disk."""
    if not METRICS_FILE.exists():
        return {"iterations": [], "aggregate": {
            "total_iterations": 0, "success_rate": 0,
            "avg_score": 0, "mutations_applied": 0,
        }}
    return json.loads(METRICS_FILE.read_text(encoding="utf-8"))


def record_iteration(iteration: int, task_id: int, verdict: str,
                     score: float, details: str = "") -> dict:
    """Record metrics for one iteration."""
    metrics = load_metrics()
    entry = {
        "iteration": iteration,
        "task_id": task_id,
        "verdict": verdict,
        "score": score,
        "details": details,
        "timestamp": datetime.now().isoformat(),
    }
    metrics["iterations"].append(entry)

    # Update aggregates
    total = len(metrics["iterations"])
    successes = sum(1 for i in metrics["iterations"] if i["verdict"] == "SUCCESS")
    avg = sum(i["score"] for i in metrics["iterations"]) / total if total else 0

    metrics["aggregate"]["total_iterations"] = total
    metrics["aggregate"]["success_rate"] = round(successes / total, 3) if total else 0
    metrics["aggregate"]["avg_score"] = round(avg, 1)

    save_metrics(metrics)
    return metrics


def save_metrics(metrics: dict) -> None:
    """Persist metrics to disk."""
    METRICS_FILE.parent.mkdir(parents=True, exist_ok=True)
    METRICS_FILE.write_text(
        json.dumps(metrics, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def get_trend(n: int = 5) -> dict:
    """Compute trend over the last N iterations."""
    metrics = load_metrics()
    recent = metrics["iterations"][-n:]
    if len(recent) < 2:
        return {"direction": "insufficient_data", "scores": [i["score"] for i in recent]}
    scores = [i["score"] for i in recent]
    delta = scores[-1] - scores[0]
    direction = "improving" if delta > 0 else "declining" if delta < 0 else "stable"
    return {"direction": direction, "scores": scores, "delta": delta}


# ── Mutations ────────────────────────────────────────────────────────

def log_mutation(iteration: int, mutation_type: str, target: str,
                 before: str, after: str, reason: str) -> None:
    """Log a meta-mutation to mutations.md."""
    if not MUTATIONS_FILE.exists():
        MUTATIONS_FILE.parent.mkdir(parents=True, exist_ok=True)
        MUTATIONS_FILE.write_text("# MAEL — Log des Mutations\n\n", encoding="utf-8")

    content = MUTATIONS_FILE.read_text(encoding="utf-8")
    count = content.count("### Mutation #") + 1

    entry = (
        f"\n### Mutation #{count} — Iteration {iteration} — {mutation_type}\n"
        f"**Cible** : {target}\n"
        f"**Avant** : {before}\n"
        f"**Après** : {after}\n"
        f"**Raison** : {reason}\n"
        f"**Résultat** : *(en attente d'évaluation)*\n"
    )
    with open(MUTATIONS_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
