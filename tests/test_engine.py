"""Integration tests for the MAEL engine in dry-run mode."""

import json
from pathlib import Path
from unittest import mock

from mael.engine import run_loop, phase_act, phase_evaluate, phase_learn, _parse_json


def _make_state_dir(tmp_path):
    """Set up a minimal .mael directory structure for testing."""
    mael_dir = tmp_path / ".mael"
    mael_dir.mkdir()
    (mael_dir / "logs").mkdir()

    state = {
        "version": "0.1.0",
        "status": "running",
        "current_iteration": 0,
        "tasks": [
            {
                "id": 1, "title": "Test task A", "status": "pending",
                "description": "A simple test task",
                "acceptance": "Must produce output", "priority": "high",
            },
            {
                "id": 2, "title": "Test task B", "status": "pending",
                "description": "Another test task",
                "acceptance": "Must complete", "priority": "medium",
            },
        ],
    }
    (mael_dir / "state.json").write_text(json.dumps(state), encoding="utf-8")
    (mael_dir / "learnings.md").write_text("# Learnings\n", encoding="utf-8")
    (mael_dir / "metrics.json").write_text(
        json.dumps({"iterations": [], "aggregate": {
            "total_iterations": 0, "success_rate": 0, "avg_score": 0,
            "mutations_applied": 0,
        }}), encoding="utf-8",
    )
    (mael_dir / "mutations.md").write_text("# Mutations\n", encoding="utf-8")
    (tmp_path / "CLAUDE.md").write_text("# CLAUDE.md\n## Patterns Confirmés\n", encoding="utf-8")

    return mael_dir


def test_full_dry_run_loop(tmp_path, monkeypatch):
    """Test a complete loop run in dry-run mode."""
    _make_state_dir(tmp_path)
    monkeypatch.chdir(tmp_path)

    summary = run_loop(max_iterations=5, dry_run=True)

    assert summary["iterations"] >= 2
    assert summary["completed_tasks"] >= 2
    assert summary["final_state"] == "all_complete"

    # Verify metrics were recorded
    metrics = json.loads((tmp_path / ".mael/metrics.json").read_text())
    assert len(metrics["iterations"]) >= 2

    # Verify learnings were added
    learnings = (tmp_path / ".mael/learnings.md").read_text()
    assert "Iteration" in learnings

    # Verify logs were created
    logs = list((tmp_path / ".mael/logs").glob("*.log"))
    assert len(logs) >= 6  # 3 phases × 2 tasks


def test_dry_run_with_mutation_interval(tmp_path, monkeypatch):
    """Test that mutation phase triggers at the right interval."""
    mael_dir = _make_state_dir(tmp_path)

    # Add more tasks to reach mutation interval
    state = json.loads((mael_dir / "state.json").read_text())
    for i in range(3, 8):
        state["tasks"].append({
            "id": i, "title": f"Task {i}", "status": "pending",
            "description": f"Task {i} desc", "acceptance": "ok",
        })
    (mael_dir / "state.json").write_text(json.dumps(state), encoding="utf-8")

    monkeypatch.chdir(tmp_path)
    summary = run_loop(max_iterations=10, mutation_interval=3, dry_run=True)

    # Check mutation log exists for iteration 3 or 6
    mutate_logs = list((tmp_path / ".mael/logs").glob("*_4_mutate.log"))
    assert len(mutate_logs) >= 1


def test_parse_json_with_markdown_fences():
    """Test JSON parsing strips markdown code fences."""
    raw = '```json\n{"key": "value"}\n```'
    result = _parse_json(raw, {})
    assert result == {"key": "value"}


def test_parse_json_fallback():
    """Test JSON parsing falls back to default on bad input."""
    result = _parse_json("not json at all", {"default": True})
    assert result == {"default": True}
