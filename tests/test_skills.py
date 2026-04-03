"""Tests for the atomic skill library."""

import json
from pathlib import Path
from unittest import mock

from mael.skills import (
    save_skill, load_skill, list_skills,
    record_skill_usage, get_best_skills, skills_summary,
)


def test_save_and_load(tmp_path):
    skills_dir = tmp_path / "skills"
    with mock.patch("mael.skills.SKILLS_DIR", skills_dir):
        save_skill("test_skill", "print('hello')", "utility",
                   "A test skill", 85.0, 1)
        skill = load_skill("test_skill")

    assert skill is not None
    assert skill["name"] == "test_skill"
    assert skill["code"] == "print('hello')"
    assert skill["score"] == 85.0
    assert skill["usage_count"] == 0


def test_list_skills(tmp_path):
    skills_dir = tmp_path / "skills"
    with mock.patch("mael.skills.SKILLS_DIR", skills_dir):
        save_skill("a", "code_a", "pattern", "desc a", 90, 1)
        save_skill("b", "code_b", "utility", "desc b", 70, 2)
        save_skill("c", "code_c", "pattern", "desc c", 80, 3)

        all_skills = list_skills()
        assert len(all_skills) == 3

        patterns = list_skills(category="pattern")
        assert len(patterns) == 2


def test_record_usage(tmp_path):
    skills_dir = tmp_path / "skills"
    with mock.patch("mael.skills.SKILLS_DIR", skills_dir):
        save_skill("used", "code", "utility", "desc", 80, 1)
        record_skill_usage("used", 90)
        record_skill_usage("used", 100)

        skill = load_skill("used")
        assert skill["usage_count"] == 2
        assert skill["avg_score_when_used"] == 95.0


def test_get_best_skills(tmp_path):
    skills_dir = tmp_path / "skills"
    with mock.patch("mael.skills.SKILLS_DIR", skills_dir):
        save_skill("good", "code", "utility", "good one", 90, 1)
        save_skill("bad", "code", "utility", "bad one", 20, 2)

        best = get_best_skills(1)
        assert len(best) == 1
        assert best[0]["name"] == "good"


def test_skills_summary(tmp_path):
    skills_dir = tmp_path / "skills"
    with mock.patch("mael.skills.SKILLS_DIR", skills_dir):
        save_skill("summarizer", "def s(): pass", "utility",
                   "Text summarizer", 85, 1)
        summary = skills_summary()
        assert "summarizer" in summary
        assert "Text summarizer" in summary
