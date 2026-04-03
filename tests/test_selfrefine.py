"""Tests for the Self-Refine module."""

from mael.selfrefine import self_refine, RefineResult


def test_self_refine_converges():
    """Test that self-refine stops when target score is reached."""
    call_count = 0

    def generate(prompt):
        return "initial output"

    def critique(output):
        return "needs improvement: be more specific"

    def refine(output, critique):
        return output + " [refined]"

    def score(output):
        nonlocal call_count
        call_count += 1
        # Score increases with each refinement
        return min(50 + call_count * 20, 100)

    result = self_refine(
        initial_prompt="test",
        generate_fn=generate,
        critique_fn=critique,
        refine_fn=refine,
        score_fn=score,
        max_iterations=10,
        target_score=90.0,
    )

    assert isinstance(result, RefineResult)
    assert result.converged
    assert result.scores[-1] >= 90.0
    assert result.iterations < 10  # Should converge before max


def test_self_refine_max_iterations():
    """Test that self-refine respects max iterations."""
    def generate(prompt):
        return "output"

    def critique(output):
        return "still bad"

    def refine(output, critique):
        return output

    def score(output):
        return 10.0  # Never improves

    result = self_refine(
        initial_prompt="test",
        generate_fn=generate,
        critique_fn=critique,
        refine_fn=refine,
        score_fn=score,
        max_iterations=3,
    )

    assert not result.converged
    assert result.iterations == 3
    assert len(result.critiques) == 3


def test_self_refine_no_score():
    """Test self-refine works without a score function."""
    result = self_refine(
        initial_prompt="test",
        generate_fn=lambda p: "v1",
        critique_fn=lambda o: "improve",
        refine_fn=lambda o, c: o + "+",
        max_iterations=2,
    )

    assert result.final_output == "v1++"
    assert result.iterations == 2
