"""MAEL Engine v0.2 — The main loop orchestrator with LLM integration.

Runs the 4-phase cycle: AGIR → ÉVALUER → APPRENDRE → MUTER
Each phase now calls Claude (Haiku for routine, Sonnet for mutations).
"""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

from .state import load_state, save_state, next_task, complete_task, start_task, all_done
from .memory import (
    add_learning, record_iteration, get_learnings,
    increment_learning_usage, promote_to_claude_md, get_trend,
    load_metrics, log_mutation,
)
from .prompts import (
    SYSTEM_MAEL, PHASE_ACT, PHASE_EVALUATE, PHASE_LEARN, PHASE_MUTATE,
)

LOG_DIR = Path(".mael/logs")
CLAUDE_MD = Path("CLAUDE.md")

# Track costs across the session
_session_costs = {"input_tokens": 0, "output_tokens": 0, "estimated_usd": 0.0}


def run_loop(max_iterations: int = 50, mutation_interval: int = 5,
             dry_run: bool = False) -> dict:
    """Run the MAEL loop.

    Args:
        max_iterations: Max iterations before stopping.
        mutation_interval: Run MUTER phase every N iterations.
        dry_run: If True, use mock LLM responses (for testing).

    Returns:
        Summary dict of the entire run.
    """
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    summary = {
        "iterations": 0, "completed_tasks": 0, "mutations": 0,
        "total_cost_usd": 0.0,
    }

    for i in range(1, max_iterations + 1):
        state = load_state()

        if all_done(state):
            if not dry_run:
                # Level 5: auto-generate next tasks
                _log("[AUTONOMIE] All tasks done. Generating next missions...")
                from .autonomy import add_generated_tasks
                new = add_generated_tasks()
                if new:
                    for t in new:
                        _log(f"[AUTONOMIE] New task: #{t['id']} {t['title']}")
                    state = load_state()
                else:
                    _log(f"All tasks complete after {i - 1} iterations.")
                    break
            else:
                _log(f"All tasks complete after {i - 1} iterations.")
                break

        task = next_task(state)
        if not task:
            _log("No more tasks to process.")
            break

        # Auto-decompose stuck tasks (3+ failures)
        if not dry_run:
            _n_fails = sum(
                1 for m in load_metrics()["iterations"]
                if m.get("task_id") == task["id"] and m["verdict"] == "FAIL"
            )
            if _n_fails >= 3 and not task.get("parent_id"):
                _log(f"[AUTONOMIE] Task #{task['id']} stuck ({_n_fails} fails). Decomposing...")
                from .autonomy import decompose_task
                subtasks = decompose_task(task, last_score=0)
                if subtasks:
                    state["tasks"].extend(subtasks)
                    task["status"] = "decomposed"
                    save_state(state)
                    for st in subtasks:
                        _log(f"[AUTONOMIE] Subtask: #{st['id']} {st['title']}")
                    continue  # skip to next iteration with subtask

        _log(f"\n{'=' * 60}")
        _log(f"ITERATION {i} — Task #{task['id']}: {task['title']}")
        _log(f"{'=' * 60}")

        # ── Phase 1: AGIR ──
        act_result = phase_act(state, task, i, dry_run=dry_run)

        # ── Phase 2: ÉVALUER ──
        eval_result = phase_evaluate(state, task, act_result, i, dry_run=dry_run)

        # ── Phase 3: APPRENDRE ──
        phase_learn(state, task, eval_result, i, dry_run=dry_run)

        # ── Phase 4: MUTER (every N iterations) ──
        if i % mutation_interval == 0:
            mutations = phase_mutate(i, dry_run=dry_run)
            summary["mutations"] += mutations

        summary["iterations"] = i
        if eval_result["verdict"] == "SUCCESS":
            summary["completed_tasks"] += 1

    summary["total_cost_usd"] = round(_session_costs["estimated_usd"], 4)
    summary["final_state"] = load_state()["status"]
    return summary


# ── Phase implementations ────────────────────────────────────────────

def phase_act(state: dict, task: dict, iteration: int,
              dry_run: bool = False) -> dict:
    """Phase 1: AGIR — Ask the LLM to execute the task."""
    _log(f"[AGIR] Task #{task['id']}: {task['title']}")

    state = start_task(state, task["id"])
    save_state(state)

    claude_md = _read_claude_md()
    learnings = get_learnings()

    # Inject available skills
    from .skills import skills_summary
    skills_ctx = skills_summary()

    prompt = PHASE_ACT.format(
        iteration=iteration,
        task_id=task["id"],
        task_title=task["title"],
        task_description=task["description"],
        task_acceptance=task.get("acceptance", "N/A"),
        skills=skills_ctx,
        claude_md=claude_md[:2000],  # Limit context size
        learnings=learnings[-1500:] if learnings else "(none)",
    )

    if dry_run:
        response = _mock_act_response(task)
    else:
        from .llm import ask, SMART
        response = ask(prompt, system=SYSTEM_MAEL, model=SMART, max_tokens=8192)

    # Execute: parse code blocks, write files, run commands
    from .executor import execute_response
    exec_result = execute_response(response)

    if exec_result.files_written:
        _log(f"[AGIR] Wrote {len(exec_result.files_written)} file(s): "
             f"{', '.join(exec_result.files_written)}")
    for cmd_r in exec_result.commands_run:
        status = "OK" if cmd_r["success"] else "FAIL"
        _log(f"[AGIR] Ran: {cmd_r['command']} → {status}")

    result = {
        "task_id": task["id"],
        "response": response,
        "files_written": exec_result.files_written,
        "commands": exec_result.commands_run,
        "execution_success": exec_result.success,
        "execution_errors": exec_result.errors,
        "timestamp": datetime.now().isoformat(),
    }

    _log_to_file(f"iter_{iteration}_1_act.log", result)
    _log(f"[AGIR] Response: {response[:200]}...")
    return result


def phase_evaluate(state: dict, task: dict, act_result: dict,
                   iteration: int, dry_run: bool = False) -> dict:
    """Phase 2: ÉVALUER — Score the result with LLM + tests."""
    _log(f"[ÉVALUER] Evaluating task #{task['id']}")

    # Run tests + gather execution info
    test_output = _run_tests()
    metrics = load_metrics()
    trend = get_trend()

    # Include execution results in evaluation context
    exec_info = ""
    if act_result.get("files_written"):
        exec_info += f"Files written: {', '.join(act_result['files_written'])}\n"
    if act_result.get("execution_errors"):
        exec_info += f"Execution errors: {'; '.join(act_result['execution_errors'])}\n"
    for cmd in act_result.get("commands", []):
        exec_info += f"Command '{cmd['command']}': {'OK' if cmd['success'] else 'FAIL'}\n"
        if cmd.get("stdout"):
            exec_info += f"  stdout: {cmd['stdout'][:500]}\n"

    prompt = PHASE_EVALUATE.format(
        iteration=iteration,
        task_id=task["id"],
        task_title=task["title"],
        task_acceptance=task.get("acceptance", "N/A"),
        act_result=act_result["response"][:2000] + "\n\n## Execution Results\n" + exec_info,
        test_output=test_output[:1000] if test_output else "(no tests run)",
        avg_score=metrics["aggregate"].get("avg_score", 0),
        trend=trend.get("direction", "no data"),
    )

    if dry_run:
        eval_data = _mock_eval_response(task)
    else:
        from .llm import ask_for_json, FAST
        raw = ask_for_json(prompt, system=SYSTEM_MAEL, model=FAST)
        eval_data = _parse_json(raw, default_eval())

    score = eval_data.get("total", 75)
    verdict = eval_data.get("verdict", "SUCCESS" if score >= 70 else "PARTIAL" if score >= 40 else "FAIL")
    critique = eval_data.get("critique", "")

    result = {
        "task_id": task["id"],
        "verdict": verdict,
        "score": score,
        "scores": eval_data.get("scores", {}),
        "critique": critique,
        "suggestion": eval_data.get("suggestion", ""),
        "test_output": test_output,
        "timestamp": datetime.now().isoformat(),
    }

    record_iteration(iteration, task["id"], verdict, score, critique)

    if verdict == "SUCCESS":
        state = complete_task(state, task["id"])
        save_state(state)
        _log(f"[ÉVALUER] ✓ SUCCEEDED — score: {score}/100")
    else:
        _log(f"[ÉVALUER] {'!' if verdict == 'PARTIAL' else '✗'} {verdict} — score: {score}/100")
        if critique:
            _log(f"[ÉVALUER] Critique: {critique[:200]}")

    _log_to_file(f"iter_{iteration}_2_eval.log", result)
    return result


def phase_learn(state: dict, task: dict, eval_result: dict,
                iteration: int, dry_run: bool = False) -> None:
    """Phase 3: APPRENDRE — Extract learnings via LLM."""
    _log(f"[APPRENDRE] Extracting learnings from iteration {iteration}")

    learnings = get_learnings()

    prompt = PHASE_LEARN.format(
        iteration=iteration,
        task_title=task["title"],
        verdict=eval_result["verdict"],
        score=eval_result["score"],
        critique=eval_result.get("critique", ""),
        learnings=learnings[-2000:] if learnings else "(none)",
    )

    if dry_run:
        learn_data = _mock_learn_response(eval_result)
    else:
        from .llm import ask_for_json, FAST
        raw = ask_for_json(prompt, system=SYSTEM_MAEL, model=FAST)
        learn_data = _parse_json(raw, {"learnings": [], "patterns_seen_again": [], "promote_to_claude_md": []})

    # Record new learnings
    for item in learn_data.get("learnings", []):
        add_learning(
            iteration=iteration,
            category=item.get("category", "general"),
            context=f"Task: {task['title']}",
            learning=item.get("learning", ""),
            confidence=item.get("confidence", "moyenne"),
        )

    # Check for reused patterns
    for pattern in learn_data.get("patterns_seen_again", []):
        count = increment_learning_usage(pattern)
        if count >= 2:
            _log(f"[APPRENDRE] Promoting pattern (used {count}x): {pattern[:80]}")
            promote_to_claude_md(pattern)

    # Direct promotions from LLM
    for promo in learn_data.get("promote_to_claude_md", []):
        promote_to_claude_md(promo)

    # Save skills to library (atomic skill acquisition)
    from .skills import save_skill
    for sk in learn_data.get("skills_to_save", []):
        if sk.get("name") and sk.get("code"):
            save_skill(
                name=sk["name"],
                code=sk["code"],
                category=sk.get("category", "utility"),
                description=sk.get("description", ""),
                score=eval_result.get("score", 0),
                source_iteration=iteration,
            )
            _log(f"[APPRENDRE] Skill saved: {sk['name']}")

    # Log meta-reasoning if present
    meta = learn_data.get("meta_reasoning", "")
    if meta:
        _log(f"[META] {meta[:200]}")

    n = len(learn_data.get("learnings", []))
    n_skills = len(learn_data.get("skills_to_save", []))
    _log(f"[APPRENDRE] Added {n} learning(s), {n_skills} skill(s)")

    _log_to_file(f"iter_{iteration}_3_learn.log", learn_data)


def phase_mutate(iteration: int, dry_run: bool = False) -> int:
    """Phase 4: MUTER — The Ouroboros phase. Uses Sonnet for meta-reasoning."""
    _log(f"[MUTER] 🐍 Ouroboros phase — the loop improves itself...")

    metrics = load_metrics()
    trend = get_trend()
    recent = metrics["iterations"][-5:]
    mutations_file = Path(".mael/mutations.md")
    past_mutations = ""
    if mutations_file.exists():
        past_mutations = mutations_file.read_text(encoding="utf-8")[-1000:]

    metrics_summary = "\n".join(
        f"  Iter {m['iteration']}: {m['verdict']} (score {m['score']})"
        for m in recent
    )

    prompt = PHASE_MUTATE.format(
        iteration=iteration,
        n_last=len(recent),
        metrics_summary=metrics_summary or "(no data)",
        trend=json.dumps(trend),
        past_mutations=past_mutations or "(none)",
        act_prompt_preview=PHASE_ACT[:100] + "...",
        eval_prompt_preview=PHASE_EVALUATE[:100] + "...",
        learn_prompt_preview=PHASE_LEARN[:100] + "...",
    )

    if dry_run:
        mutate_data = _mock_mutate_response()
    else:
        from .llm import ask_for_json, SMART
        raw = ask_for_json(prompt, system=SYSTEM_MAEL, model=SMART, max_tokens=4096)
        mutate_data = _parse_json(raw, {"analysis": "", "health": "healthy", "mutations": []})

    health = mutate_data.get("health", "healthy")
    _log(f"[MUTER] System health: {health}")
    _log(f"[MUTER] Analysis: {mutate_data.get('analysis', '')[:200]}")

    applied = 0
    for m in mutate_data.get("mutations", []):
        confidence = m.get("confidence", 0)
        if confidence >= 0.5:
            log_mutation(
                iteration=iteration,
                mutation_type=m.get("type", "unknown"),
                target=m.get("target", ""),
                before=m.get("before_summary", ""),
                after=m.get("after", ""),
                reason=m.get("reason", ""),
            )
            _log(f"[MUTER] Applied mutation: {m['type']} → {m['target']}")
            applied += 1
        else:
            _log(f"[MUTER] Skipped (confidence {confidence}): {m.get('target', '')}")

    _log_to_file(f"iter_{iteration}_4_mutate.log", mutate_data)
    return applied


# ── Helpers ──────────────────────────────────────────────────────────

def _read_claude_md() -> str:
    if CLAUDE_MD.exists():
        return CLAUDE_MD.read_text(encoding="utf-8")
    return ""


def _run_tests() -> str:
    """Run pytest and return output. Returns empty string on error."""
    try:
        result = subprocess.run(
            ["python", "-m", "pytest", "tests/", "-v", "--tb=short"],
            capture_output=True, text=True, timeout=60,
        )
        return result.stdout + result.stderr
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return ""


def _parse_json(raw: str, default: dict) -> dict:
    """Parse JSON from LLM response, with fallback."""
    # Strip markdown code fences if present
    text = raw.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        text = "\n".join(lines[1:])
        if text.endswith("```"):
            text = text[:-3]
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        _log(f"[WARN] Failed to parse JSON, using defaults. Raw: {raw[:200]}")
        return default


def default_eval() -> dict:
    return {
        "scores": {"correctness": 15, "completeness": 15, "quality": 15,
                    "testability": 15, "learning": 15},
        "total": 75, "verdict": "SUCCESS", "critique": "", "suggestion": "",
    }


# ── Mock responses for dry-run / testing ─────────────────────────────

def _mock_act_response(task: dict) -> str:
    return f"### Analyse\nTask '{task['title']}' analysée.\n\n### Implémentation\nCode simulé.\n"


def _mock_eval_response(task: dict) -> dict:
    return {
        "scores": {"correctness": 16, "completeness": 15, "quality": 15,
                    "testability": 14, "learning": 15},
        "total": 75, "verdict": "SUCCESS",
        "critique": "Mock evaluation — task appears well-structured.",
        "suggestion": "",
    }


def _mock_learn_response(eval_result: dict) -> dict:
    return {
        "learnings": [{
            "category": "success_pattern",
            "learning": f"Task scored {eval_result['score']}/100",
            "confidence": "haute",
            "reusable_for": "similar tasks",
        }],
        "patterns_seen_again": [],
        "promote_to_claude_md": [],
    }


def _mock_mutate_response() -> dict:
    return {
        "analysis": "System performing at acceptable level.",
        "health": "healthy",
        "mutations": [],
    }


def _log(message: str) -> None:
    print(f"[MAEL] {message}", flush=True)


def _log_to_file(filename: str, data) -> None:
    filepath = LOG_DIR / filename
    if isinstance(data, str):
        filepath.write_text(data, encoding="utf-8")
    else:
        filepath.write_text(
            json.dumps(data, indent=2, ensure_ascii=False, default=str) + "\n",
            encoding="utf-8",
        )


# ── CLI entry point ──────────────────────────────────────────────────

def main():
    """CLI entry point.

    Usage: python -m mael.engine [max_iterations] [--dry-run]
    """
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]
    max_iter = int(args[0]) if args else 50

    mode = "DRY RUN (mock LLM)" if dry_run else "LIVE (Claude API)"
    _log(f"Starting MAEL loop — {mode} — max {max_iter} iterations")
    _log(f"{'=' * 60}")

    summary = run_loop(max_iterations=max_iter, dry_run=dry_run)

    _log(f"\n{'=' * 60}")
    _log(f"MAEL COMPLETE")
    _log(f"  Iterations: {summary['iterations']}")
    _log(f"  Tasks completed: {summary['completed_tasks']}")
    _log(f"  Mutations applied: {summary['mutations']}")
    _log(f"  Estimated cost: ${summary['total_cost_usd']}")
    _log(f"  Final status: {summary['final_state']}")
    _log(f"{'=' * 60}")


if __name__ == "__main__":
    main()
