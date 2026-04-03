"""Atomic Skill Library — reusable micro-competencies accumulated by MAEL.

Inspired by:
- HyperAgents (Meta Research): atomic skill acquisition
- OpenSpace (HKUDS): FIX/DERIVED/CAPTURED skill modes
- GEPA optimize_anything: skills as optimizable text artifacts

A skill is a small, reusable Python snippet + metadata that MAEL has
learned works well. Skills are stored as JSON in .mael/skills/.
"""

import json
from pathlib import Path
from datetime import datetime

SKILLS_DIR = Path(".mael/skills")


def save_skill(name: str, code: str, category: str,
               description: str, score: float,
               source_iteration: int) -> Path:
    """Save a reusable skill to the library.

    Args:
        name: Short identifier (e.g. "tf_idf_scorer")
        code: The Python code snippet
        category: "pattern" | "utility" | "test" | "prompt"
        description: What this skill does
        score: Quality score when discovered (0-100)
        source_iteration: Which iteration produced this skill

    Returns:
        Path to the saved skill file.
    """
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    skill = {
        "name": name,
        "category": category,
        "description": description,
        "code": code,
        "score": score,
        "source_iteration": source_iteration,
        "created": datetime.now().isoformat(),
        "usage_count": 0,
        "avg_score_when_used": 0.0,
    }

    path = SKILLS_DIR / f"{name}.json"
    path.write_text(json.dumps(skill, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    return path


def load_skill(name: str) -> dict | None:
    """Load a skill by name."""
    path = SKILLS_DIR / f"{name}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def list_skills(category: str | None = None) -> list[dict]:
    """List all skills, optionally filtered by category."""
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    skills = []
    for p in sorted(SKILLS_DIR.glob("*.json")):
        try:
            skill = json.loads(p.read_text(encoding="utf-8"))
            if category is None or skill.get("category") == category:
                skills.append(skill)
        except (json.JSONDecodeError, KeyError):
            continue
    return skills


def record_skill_usage(name: str, score: float) -> None:
    """Record that a skill was used and the score achieved."""
    path = SKILLS_DIR / f"{name}.json"
    if not path.exists():
        return
    skill = json.loads(path.read_text(encoding="utf-8"))
    n = skill["usage_count"]
    old_avg = skill["avg_score_when_used"]
    skill["usage_count"] = n + 1
    skill["avg_score_when_used"] = round((old_avg * n + score) / (n + 1), 1)
    path.write_text(json.dumps(skill, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")


def get_best_skills(n: int = 5) -> list[dict]:
    """Get the top N skills by usage-weighted score."""
    skills = list_skills()
    for s in skills:
        s["_rank"] = s["score"] * 0.4 + s["avg_score_when_used"] * 0.6
    skills.sort(key=lambda s: s["_rank"], reverse=True)
    return skills[:n]


def skills_summary() -> str:
    """Generate a text summary of available skills for injection into prompts."""
    skills = get_best_skills(10)
    if not skills:
        return "(no skills in library)"
    lines = []
    for s in skills:
        lines.append(f"- **{s['name']}** ({s['category']}): {s['description']} "
                     f"[score: {s['score']}, used: {s['usage_count']}x]")
    return "\n".join(lines)
