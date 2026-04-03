"""Self-Refine module — the simplest self-improving loop.

Implements: generate → critique → refine → repeat
Works with any callable that acts as an LLM.
"""

from dataclasses import dataclass


@dataclass
class RefineResult:
    """Result of a self-refine loop."""
    final_output: str
    iterations: int
    scores: list[float]
    critiques: list[str]
    converged: bool


def self_refine(
    initial_prompt: str,
    generate_fn,
    critique_fn,
    refine_fn,
    score_fn=None,
    max_iterations: int = 5,
    target_score: float = 90.0,
) -> RefineResult:
    """Run a Self-Refine loop.

    Args:
        initial_prompt: The starting prompt or content to improve.
        generate_fn: Callable(prompt) -> str. Generates initial output.
        critique_fn: Callable(output) -> str. Critiques the output.
        refine_fn: Callable(output, critique) -> str. Refines based on critique.
        score_fn: Optional Callable(output) -> float. Scores 0-100.
        max_iterations: Maximum refinement iterations.
        target_score: Stop if score reaches this threshold.

    Returns:
        RefineResult with final output and iteration history.
    """
    # Step 1: Generate initial output
    current = generate_fn(initial_prompt)
    scores = []
    critiques = []

    for i in range(max_iterations):
        # Score current output
        score = score_fn(current) if score_fn else 0.0
        scores.append(score)

        # Check convergence
        if score_fn and score >= target_score:
            return RefineResult(
                final_output=current,
                iterations=i + 1,
                scores=scores,
                critiques=critiques,
                converged=True,
            )

        # Critique
        critique = critique_fn(current)
        critiques.append(critique)

        # Refine
        current = refine_fn(current, critique)

    # Final score
    if score_fn:
        scores.append(score_fn(current))

    return RefineResult(
        final_output=current,
        iterations=max_iterations,
        scores=scores,
        critiques=critiques,
        converged=False,
    )


def simple_critique(output: str, criteria: list[str] | None = None) -> str:
    """Generate a simple critique template. Useful as a starting point.

    In production, replace this with an LLM call.
    """
    criteria = criteria or [
        "clarity", "completeness", "correctness", "conciseness"
    ]
    lines = [f"Evaluate on: {', '.join(criteria)}", ""]
    lines.append(f"Output to critique:\n{output[:500]}")
    lines.append("\nProvide specific, actionable feedback for improvement.")
    return "\n".join(lines)
