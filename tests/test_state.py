"""Tests for MAEL state management."""

import json
import tempfile
from pathlib import Path
from unittest import mock

from mael.state import load_state, save_state, next_task, complete_task, start_task, all_done


def _make_state(tasks=None):
    return {
        "version": "0.1.0",
        "status": "running",
        "current_iteration": 0,
        "tasks": tasks or [],
    }


def test_next_task_returns_pending():
    state = _make_state([
        {"id": 1, "status": "completed", "title": "done"},
        {"id": 2, "status": "pending", "title": "todo"},
        {"id": 3, "status": "pending", "title": "also todo"},
    ])
    task = next_task(state)
    assert task["id"] == 2


def test_next_task_returns_in_progress_first():
    state = _make_state([
        {"id": 1, "status": "completed", "title": "done"},
        {"id": 2, "status": "in_progress", "title": "doing"},
        {"id": 3, "status": "pending", "title": "todo"},
    ])
    task = next_task(state)
    assert task["id"] == 2


def test_next_task_none_when_all_done():
    state = _make_state([
        {"id": 1, "status": "completed", "title": "done"},
    ])
    assert next_task(state) is None


def test_complete_task():
    state = _make_state([
        {"id": 1, "status": "in_progress", "title": "doing"},
        {"id": 2, "status": "pending", "title": "todo"},
    ])
    state = complete_task(state, 1)
    assert state["tasks"][0]["status"] == "completed"
    assert state["status"] != "all_complete"


def test_complete_last_task_sets_all_complete():
    state = _make_state([
        {"id": 1, "status": "completed", "title": "done"},
        {"id": 2, "status": "in_progress", "title": "finishing"},
    ])
    state = complete_task(state, 2)
    assert state["status"] == "all_complete"
    assert all_done(state)


def test_start_task():
    state = _make_state([{"id": 1, "status": "pending", "title": "todo"}])
    state = start_task(state, 1)
    assert state["tasks"][0]["status"] == "in_progress"


def test_save_and_load_roundtrip(tmp_path):
    state = _make_state([{"id": 1, "status": "pending", "title": "test"}])
    state_file = tmp_path / ".mael" / "state.json"
    state_file.parent.mkdir(parents=True)

    with mock.patch("mael.state.STATE_FILE", state_file):
        save_state(state)
        loaded = load_state()

    assert loaded["tasks"][0]["title"] == "test"
    assert loaded["version"] == "0.1.0"
