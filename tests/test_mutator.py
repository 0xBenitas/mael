"""Tests for the Ouroboros mutation module."""

from unittest import mock

from mael.mutator import analyze_performance, propose_mutations, Mutation


def _mock_metrics(iterations):
    return {
        "iterations": iterations,
        "aggregate": {"total_iterations": len(iterations)},
    }


def test_analyze_detects_high_failure():
    metrics = _mock_metrics([
        {"verdict": "FAIL", "score": 20},
        {"verdict": "FAIL", "score": 30},
        {"verdict": "FAIL", "score": 25},
        {"verdict": "SUCCESS", "score": 80},
        {"verdict": "FAIL", "score": 15},
    ])

    with mock.patch("mael.mutator.load_metrics", return_value=metrics), \
         mock.patch("mael.mutator.get_trend", return_value={
             "direction": "declining", "scores": [20, 30, 25, 80, 15], "delta": -5,
         }):
        analysis = analyze_performance(5)

    assert analysis["needs_mutation"]
    assert analysis["failure_count"] >= 3


def test_analyze_healthy_system():
    metrics = _mock_metrics([
        {"verdict": "SUCCESS", "score": 85},
        {"verdict": "SUCCESS", "score": 90},
        {"verdict": "SUCCESS", "score": 88},
    ])

    with mock.patch("mael.mutator.load_metrics", return_value=metrics), \
         mock.patch("mael.mutator.get_trend", return_value={
             "direction": "improving", "scores": [85, 90, 88], "delta": 3,
         }):
        analysis = analyze_performance(3)

    assert not analysis["needs_mutation"]


def test_propose_mutations_on_failure():
    analysis = {
        "needs_mutation": True,
        "reasons": ["High failure rate: 3/5"],
        "failure_count": 3,
    }
    mutations = propose_mutations(analysis)
    assert len(mutations) >= 1
    assert all(isinstance(m, Mutation) for m in mutations)


def test_no_mutations_when_healthy():
    analysis = {"needs_mutation": False, "reasons": []}
    mutations = propose_mutations(analysis)
    assert len(mutations) == 0
