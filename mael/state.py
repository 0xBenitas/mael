"""State management for MAEL loop — reads/writes .mael/state.json."""

import json
from pathlib import Path
from datetime import datetime

MAEL_DIR = Path(".mael")
STATE_FILE = MAEL_DIR / "state.json"


def load_state() -> dict:
    """Load the current MAEL state from disk."""
    if not STATE_FILE.exists():
        return _default_state()
    return json.loads(STATE_FILE.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    """Persist MAEL state to disk."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def next_task(state: dict) -> dict | None:
    """Return the next pending or in_progress task, or None if all done."""
    for task in state.get("tasks", []):
        if task["status"] in ("in_progress", "pending"):
            return task
    return None


def complete_task(state: dict, task_id: int) -> dict:
    """Mark a task as completed and bump iteration."""
    for task in state["tasks"]:
        if task["id"] == task_id:
            task["status"] = "completed"
            break
    if all(t["status"] == "completed" for t in state["tasks"]):
        state["status"] = "all_complete"
    state["current_iteration"] = state.get("current_iteration", 0) + 1
    return state


def start_task(state: dict, task_id: int) -> dict:
    """Mark a task as in_progress."""
    for task in state["tasks"]:
        if task["id"] == task_id:
            task["status"] = "in_progress"
            break
    return state


def all_done(state: dict) -> bool:
    """Check if all tasks are completed."""
    return state.get("status") == "all_complete"


def _default_state() -> dict:
    return {
        "version": "0.1.0",
        "status": "initialized",
        "current_iteration": 0,
        "tasks": [],
        "meta": {
            "created": datetime.now().strftime("%Y-%m-%d"),
            "description": "MAEL — Méta-Amélioration Évolutive en Ligne",
        },
    }
