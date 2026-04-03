"""Tests for MAEL memory module."""

from pathlib import Path
from unittest import mock

from mael.memory import (
    add_learning, get_learnings, increment_learning_usage,
    promote_to_claude_md, record_iteration, load_metrics, get_trend,
)


def test_add_and_get_learning(tmp_path):
    learnings_file = tmp_path / "learnings.md"
    learnings_file.write_text("# Learnings\n", encoding="utf-8")

    with mock.patch("mael.memory.LEARNINGS_FILE", learnings_file):
        add_learning(1, "test", "testing context", "Always test first", "haute")
        content = get_learnings()

    assert "Always test first" in content
    assert "Iteration 1" in content
    assert "**Confiance** : haute" in content


def test_increment_learning_usage(tmp_path):
    learnings_file = tmp_path / "learnings.md"
    learnings_file.write_text(
        "# Learnings\n\n"
        "### [2026-04-03] Iteration 1 — test\n"
        "**Contexte** : ctx\n"
        "**Learning** : Always test first\n"
        "**Confiance** : haute\n"
        "**Utilisations** : 0\n",
        encoding="utf-8",
    )

    with mock.patch("mael.memory.LEARNINGS_FILE", learnings_file):
        count = increment_learning_usage("Always test first")

    assert count == 1
    content = learnings_file.read_text(encoding="utf-8")
    assert "**Utilisations** : 1" in content


def test_promote_to_claude_md(tmp_path):
    claude_file = tmp_path / "CLAUDE.md"
    claude_file.write_text(
        "# CLAUDE.md\n\n## Patterns Confirmés\n\n*Aucun*\n",
        encoding="utf-8",
    )

    with mock.patch("mael.memory.CLAUDE_MD", claude_file):
        promote_to_claude_md("Always test before committing")

    content = claude_file.read_text(encoding="utf-8")
    assert "Always test before committing" in content


def test_record_iteration_and_trend(tmp_path):
    metrics_file = tmp_path / "metrics.json"

    with mock.patch("mael.memory.METRICS_FILE", metrics_file):
        record_iteration(1, 1, "SUCCESS", 85.0)
        record_iteration(2, 1, "SUCCESS", 90.0)
        record_iteration(3, 2, "PARTIAL", 55.0)

        metrics = load_metrics()
        assert metrics["aggregate"]["total_iterations"] == 3
        assert metrics["aggregate"]["avg_score"] == 76.7

        trend = get_trend(3)
        assert trend["direction"] == "declining"  # 85 → 55
        assert len(trend["scores"]) == 3
