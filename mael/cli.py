"""MAEL CLI — Le serpent qui se mord la queue.

Usage:
    python -m mael init                  # Initialize .mael/ structure
    python -m mael run [N]               # Run N iterations (default: 50)
    python -m mael run [N] --dry-run     # Run without API calls
    python -m mael status                # Show current state
    python -m mael reset                 # Reset state for fresh run
    python -m mael doctor                # Self-diagnose and fix issues
    python -m mael generate [goal]       # Auto-generate next tasks
    python -m mael auto [N] [goal]       # Full autonomy: generate + run
"""

import json
import sys
from pathlib import Path
from datetime import datetime


MAEL_DIR = Path(".mael")


def cmd_init():
    """Initialize the MAEL project structure."""
    dirs = [MAEL_DIR, MAEL_DIR / "logs", MAEL_DIR / "rules"]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

    # state.json
    state_file = MAEL_DIR / "state.json"
    if not state_file.exists():
        state = {
            "version": "0.3.0",
            "status": "initialized",
            "current_iteration": 0,
            "tasks": [],
            "meta": {
                "created": datetime.now().strftime("%Y-%m-%d"),
                "description": "MAEL — Méta-Amélioration Évolutive en Ligne",
            },
        }
        state_file.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n")
        print("[MAEL] Created .mael/state.json")

    # learnings.md
    learn_file = MAEL_DIR / "learnings.md"
    if not learn_file.exists():
        learn_file.write_text("# MAEL — Learnings\n\n", encoding="utf-8")
        print("[MAEL] Created .mael/learnings.md")

    # metrics.json
    metrics_file = MAEL_DIR / "metrics.json"
    if not metrics_file.exists():
        metrics_file.write_text(json.dumps({
            "iterations": [],
            "aggregate": {"total_iterations": 0, "success_rate": 0,
                          "avg_score": 0, "mutations_applied": 0},
        }, indent=2) + "\n")
        print("[MAEL] Created .mael/metrics.json")

    # mutations.md
    mut_file = MAEL_DIR / "mutations.md"
    if not mut_file.exists():
        mut_file.write_text("# MAEL — Log des Mutations\n\n", encoding="utf-8")
        print("[MAEL] Created .mael/mutations.md")

    # CLAUDE.md
    claude_file = Path("CLAUDE.md")
    if not claude_file.exists():
        claude_file.write_text(
            "# CLAUDE.md — Mémoire Persistante\n\n"
            "## Patterns Confirmés\n\n"
            "## Gotchas Connus\n\n",
            encoding="utf-8",
        )
        print("[MAEL] Created CLAUDE.md")

    print("[MAEL] Initialization complete. Add tasks to .mael/state.json to begin.")


def cmd_run(args: list[str]):
    """Run the MAEL loop."""
    dry_run = "--dry-run" in args
    clean_args = [a for a in args if a != "--dry-run"]
    max_iter = int(clean_args[0]) if clean_args else 50

    from .engine import run_loop
    summary = run_loop(max_iterations=max_iter, dry_run=dry_run)
    return summary


def cmd_status():
    """Display current MAEL status."""
    state_file = MAEL_DIR / "state.json"
    if not state_file.exists():
        print("[MAEL] Not initialized. Run: python -m mael init")
        return

    state = json.loads(state_file.read_text())
    print(f"\n[MAEL] Status: {state['status']}")
    print(f"[MAEL] Iteration: {state['current_iteration']}")
    print(f"[MAEL] Tasks:")

    for t in state.get("tasks", []):
        icon = {"completed": "✓", "in_progress": "→", "pending": "○"}.get(t["status"], "?")
        print(f"  {icon} [{t['id']}] {t['title']} ({t['status']})")

    metrics_file = MAEL_DIR / "metrics.json"
    if metrics_file.exists():
        metrics = json.loads(metrics_file.read_text())
        agg = metrics.get("aggregate", {})
        print(f"\n[MAEL] Metrics:")
        print(f"  Total iterations: {agg.get('total_iterations', 0)}")
        print(f"  Success rate: {agg.get('success_rate', 0):.0%}")
        print(f"  Avg score: {agg.get('avg_score', 0):.1f}/100")
        print(f"  Mutations: {agg.get('mutations_applied', 0)}")


def cmd_reset():
    """Reset state for a fresh run (keeps structure and learnings)."""
    state_file = MAEL_DIR / "state.json"
    if not state_file.exists():
        print("[MAEL] Not initialized.")
        return

    state = json.loads(state_file.read_text())
    state["status"] = "running"
    state["current_iteration"] = 0
    for t in state.get("tasks", []):
        t["status"] = "pending"
    state_file.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n")
    print("[MAEL] State reset. All tasks set to pending. Learnings preserved.")


def cmd_doctor():
    """Run self-diagnostics."""
    from .autonomy import doctor
    report = doctor()
    status = "HEALTHY" if report["healthy"] else "ISSUES FOUND"
    print(f"\n[MAEL DOCTOR] {status}")
    for check in report["checks"]:
        icon = "✓" if check.startswith("OK") else "✗"
        print(f"  {icon} {check}")
    if report["fixes"]:
        print(f"\n[MAEL DOCTOR] Suggested fixes:")
        for fix in report["fixes"]:
            print(f"  → {fix['action']} task #{fix['task_id']}: {fix['reason']}")


def cmd_generate(args: list[str]):
    """Auto-generate next tasks."""
    goal = " ".join(args) if args else ""
    from .autonomy import add_generated_tasks
    tasks = add_generated_tasks(goal)
    if tasks:
        print(f"[MAEL] Generated {len(tasks)} new task(s):")
        for t in tasks:
            print(f"  ○ [{t['id']}] {t['title']}")
    else:
        print("[MAEL] No tasks generated.")


def cmd_auto(args: list[str]):
    """Full autonomy: generate tasks + run loop."""
    # Parse args
    max_iter = 50
    goal = ""
    for a in args:
        if a.isdigit():
            max_iter = int(a)
        elif a != "--dry-run":
            goal = a

    dry_run = "--dry-run" in args

    if not dry_run:
        # Generate tasks if none pending
        state = json.loads((MAEL_DIR / "state.json").read_text())
        pending = [t for t in state.get("tasks", []) if t["status"] == "pending"]
        if not pending:
            print("[MAEL AUTO] No pending tasks. Generating...")
            cmd_generate([goal] if goal else [])

    # Run loop
    from .engine import run_loop
    run_loop(max_iterations=max_iter, dry_run=dry_run)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    command = sys.argv[1]

    if command == "init":
        cmd_init()
    elif command == "run":
        cmd_run(sys.argv[2:])
    elif command == "status":
        cmd_status()
    elif command == "reset":
        cmd_reset()
    elif command == "doctor":
        cmd_doctor()
    elif command == "generate":
        cmd_generate(sys.argv[2:])
    elif command == "auto":
        cmd_auto(sys.argv[2:])
    else:
        print(f"[MAEL] Unknown command: {command}")
        print(__doc__)
        sys.exit(1)
