"""Tests for the autonomy module (doctor, task decomposition)."""

import json
from pathlib import Path

from mael.autonomy import doctor, _scan_project


def test_doctor_on_healthy_project(tmp_path, monkeypatch):
    """Doctor should report healthy on a well-structured project."""
    # Set up minimal structure
    mael_dir = tmp_path / ".mael"
    mael_dir.mkdir()
    (mael_dir / "state.json").write_text(json.dumps({
        "version": "0.3.0", "status": "running", "current_iteration": 0,
        "tasks": [{"id": 1, "title": "test", "status": "pending"}],
    }))
    (mael_dir / "learnings.md").write_text("# Learnings\n")
    (mael_dir / "metrics.json").write_text(json.dumps({
        "iterations": [], "aggregate": {
            "total_iterations": 0, "success_rate": 0,
            "avg_score": 0, "mutations_applied": 0,
        },
    }))
    (mael_dir / "mutations.md").write_text("# Mutations\n")
    (tmp_path / "CLAUDE.md").write_text("# CLAUDE.md\n## Patterns Confirmés\n")

    monkeypatch.chdir(tmp_path)
    report = doctor()

    assert any("state.json" in c for c in report["checks"])
    assert any("learnings" in c for c in report["checks"])


def test_doctor_detects_missing_files(tmp_path, monkeypatch):
    """Doctor should flag missing .mael files."""
    mael_dir = tmp_path / ".mael"
    mael_dir.mkdir()
    # Only create state.json, skip the rest
    (mael_dir / "state.json").write_text(json.dumps({
        "version": "0.3.0", "status": "running", "current_iteration": 0,
        "tasks": [],
    }))

    monkeypatch.chdir(tmp_path)
    report = doctor()

    missing = [c for c in report["checks"] if "MISSING" in c]
    assert len(missing) >= 1  # At least learnings.md or metrics.json missing


def test_scan_project():
    """Scan should return file listings."""
    result = _scan_project()
    assert isinstance(result, str)
    assert len(result) > 0
