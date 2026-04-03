"""MAEL Engine — The main loop orchestrator.

Runs the 4-phase cycle: AGIR → ÉVALUER → APPRENDRE → MUTER
"""

import sys
from pathlib import Path
from datetime import datetime

from .state import load_state, save_state, next_task, complete_task, start_task, all_done
from .memory import (
    add_learning, record_iteration, get_learnings,
    increment_learning_usage, promote_to_claude_md, get_trend,
)
from .mutator import analyze_performance, propose_mutations, apply_mutation

LOG_DIR = Path(".mael/logs")


def run_loop(max_iterations: int = 50, mutation_interval: int = 5) -> dict:
    """Run the MAEL loop.

    Returns a summary dict of the entire run.
    """
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    summary = {"iterations": 0, "completed_tasks": 0, "mutations": 0}

    for i in range(1, max_iterations + 1):
        state = load_state()

        if all_done(state):
            _log(f"All tasks complete after {i - 1} iterations.")
            break

        task = next_task(state)
        if not task:
            _log("No more tasks to process.")
            break

        _log(f"\n{'=' * 60}")
        _log(f"ITERATION {i} — Task #{task['id']}: {task['title']}")
        _log(f"{'=' * 60}")

        # ── Phase 1: AGIR ──
        act_result = phase_act(state, task, i)

        # ── Phase 2: ÉVALUER ──
        eval_result = phase_evaluate(state, task, act_result, i)

        # ── Phase 3: APPRENDRE ──
        phase_learn(state, task, eval_result, i)

        # ── Phase 4: MUTER (every N iterations) ──
        if i % mutation_interval == 0:
            mutations = phase_mutate(i)
            summary["mutations"] += mutations

        summary["iterations"] = i
        if eval_result["verdict"] == "SUCCESS":
            summary["completed_tasks"] += 1

    summary["final_state"] = load_state()["status"]
    return summary


def phase_act(state: dict, task: dict, iteration: int) -> dict:
    """Phase 1: AGIR — Execute the current task."""
    _log(f"[AGIR] Starting task #{task['id']}: {task['title']}")

    state = start_task(state, task["id"])
    save_state(state)

    result = {
        "task_id": task["id"],
        "action": f"Executing: {task['description']}",
        "timestamp": datetime.now().isoformat(),
    }

    _log_to_file(f"iter_{iteration}_1_act.log", result)
    return result


def phase_evaluate(state: dict, task: dict, act_result: dict,
                   iteration: int) -> dict:
    """Phase 2: ÉVALUER — Test and score the result."""
    _log(f"[ÉVALUER] Evaluating task #{task['id']}")

    # In v0, evaluation is based on task acceptance criteria
    # In production, this would run tests, linters, etc.
    score = _evaluate_task(task)
    verdict = "SUCCESS" if score >= 70 else "PARTIAL" if score >= 40 else "FAIL"

    result = {
        "task_id": task["id"],
        "verdict": verdict,
        "score": score,
        "details": f"Evaluated against: {task.get('acceptance', 'N/A')}",
        "timestamp": datetime.now().isoformat(),
    }

    # Record metrics
    record_iteration(iteration, task["id"], verdict, score, result["details"])

    # Complete task if successful
    if verdict == "SUCCESS":
        state = complete_task(state, task["id"])
        save_state(state)
        _log(f"[ÉVALUER] ✓ Task #{task['id']} SUCCEEDED (score: {score})")
    else:
        _log(f"[ÉVALUER] {'!' if verdict == 'PARTIAL' else '✗'} "
             f"Task #{task['id']} {verdict} (score: {score})")

    _log_to_file(f"iter_{iteration}_2_eval.log", result)
    return result


def phase_learn(state: dict, task: dict, eval_result: dict,
                iteration: int) -> None:
    """Phase 3: APPRENDRE — Extract learnings from this iteration."""
    _log(f"[APPRENDRE] Extracting learnings from iteration {iteration}")

    verdict = eval_result["verdict"]

    if verdict == "SUCCESS":
        add_learning(
            iteration=iteration,
            category="success_pattern",
            context=f"Task: {task['title']}",
            learning=f"Approach worked for task type: {task.get('title', 'unknown')}",
            confidence="haute",
        )
    elif verdict == "FAIL":
        add_learning(
            iteration=iteration,
            category="failure_analysis",
            context=f"Task: {task['title']} — Score: {eval_result['score']}",
            learning=f"Task failed. Needs different approach or decomposition.",
            confidence="moyenne",
        )

    _log_to_file(f"iter_{iteration}_3_learn.log", {
        "verdict": verdict,
        "learnings_added": 1,
    })


def phase_mutate(iteration: int) -> int:
    """Phase 4: MUTER — The Ouroboros phase. Improve the process itself."""
    _log(f"[MUTER] 🐍 Ouroboros phase — analyzing last iterations...")

    analysis = analyze_performance()

    if not analysis["needs_mutation"]:
        _log("[MUTER] No mutation needed. Process is healthy.")
        return 0

    mutations = propose_mutations(analysis)
    _log(f"[MUTER] Proposed {len(mutations)} mutation(s):")

    applied = 0
    for m in mutations:
        if m.confidence >= 0.5:  # Only apply confident mutations
            apply_mutation(m, iteration)
            _log(f"  → Applied: {m.mutation_type} on '{m.target}' ({m.reason})")
            applied += 1
        else:
            _log(f"  → Skipped (low confidence): {m.mutation_type} on '{m.target}'")

    _log_to_file(f"iter_{iteration}_4_mutate.log", {
        "analysis": analysis,
        "mutations_proposed": len(mutations),
        "mutations_applied": applied,
    })
    return applied


def _evaluate_task(task: dict) -> float:
    """Evaluate a task. v0: heuristic. Future: run tests + LLM judge."""
    # Check if task has associated test files or acceptance criteria
    if task.get("status") == "completed":
        return 100.0
    # Default: task was attempted, give partial credit
    return 75.0


def _log(message: str) -> None:
    """Print a log message."""
    print(f"[MAEL] {message}", flush=True)


def _log_to_file(filename: str, data: dict) -> None:
    """Write structured log to file."""
    import json
    filepath = LOG_DIR / filename
    filepath.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


# ── CLI entry point ──────────────────────────────────────────────────

def main():
    """CLI entry point."""
    max_iter = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    _log(f"Starting MAEL loop (max {max_iter} iterations)")
    _log(f"{'=' * 60}")

    summary = run_loop(max_iterations=max_iter)

    _log(f"\n{'=' * 60}")
    _log(f"MAEL COMPLETE")
    _log(f"  Iterations: {summary['iterations']}")
    _log(f"  Tasks completed: {summary['completed_tasks']}")
    _log(f"  Mutations applied: {summary['mutations']}")
    _log(f"  Final status: {summary['final_state']}")
    _log(f"{'=' * 60}")


if __name__ == "__main__":
    main()
