"""Tests for LLM module (unit tests only, no actual API calls)."""

from mael.llm import estimate_cost, FAST, SMART


def test_estimate_cost_haiku():
    cost = estimate_cost(1000, 500, model=FAST)
    assert cost > 0
    assert cost < 0.01  # Should be very cheap


def test_estimate_cost_sonnet():
    cost = estimate_cost(1000, 500, model=SMART)
    assert cost > 0
    assert cost > estimate_cost(1000, 500, model=FAST)  # Sonnet is more expensive


def test_cost_scales_linearly():
    cost1 = estimate_cost(1000, 1000, model=FAST)
    cost2 = estimate_cost(2000, 2000, model=FAST)
    assert abs(cost2 - 2 * cost1) < 0.0001
