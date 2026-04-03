"""Ouroboros mutation module — the loop that improves the loop.

Analyzes past iterations and proposes mutations to the process itself:
- Evaluation criteria
- Phase prompts
- Learning heuristics
"""

from dataclasses import dataclass
from .memory import load_metrics, get_trend, log_mutation


@dataclass
class Mutation:
    """A proposed mutation to the MAEL process."""
    mutation_type: str  # "prompt", "criteria", "heuristic", "structure"
    target: str
    before: str
    after: str
    reason: str
    confidence: float  # 0-1


def analyze_performance(n_iterations: int = 5) -> dict:
    """Analyze recent performance to identify improvement opportunities."""
    metrics = load_metrics()
    trend = get_trend(n_iterations)
    recent = metrics["iterations"][-n_iterations:]

    analysis = {
        "trend": trend,
        "recent_verdicts": [i["verdict"] for i in recent],
        "recent_scores": [i["score"] for i in recent],
        "failure_count": sum(1 for i in recent if i["verdict"] == "FAIL"),
        "avg_recent_score": (
            sum(i["score"] for i in recent) / len(recent) if recent else 0
        ),
        "needs_mutation": False,
        "reasons": [],
    }

    # Decision rules for when to mutate
    if analysis["failure_count"] >= 3:
        analysis["needs_mutation"] = True
        analysis["reasons"].append(
            f"High failure rate: {analysis['failure_count']}/{len(recent)}"
        )

    if trend["direction"] == "declining":
        analysis["needs_mutation"] = True
        analysis["reasons"].append(
            f"Declining trend: delta={trend.get('delta', 0)}"
        )

    if analysis["avg_recent_score"] < 50 and len(recent) >= 3:
        analysis["needs_mutation"] = True
        analysis["reasons"].append(
            f"Low average score: {analysis['avg_recent_score']:.1f}"
        )

    return analysis


def propose_mutations(analysis: dict) -> list[Mutation]:
    """Propose mutations based on performance analysis.

    In production, this would call an LLM to generate creative mutations.
    For v0, it uses heuristic rules.
    """
    mutations = []

    if not analysis["needs_mutation"]:
        return mutations

    for reason in analysis["reasons"]:
        if "failure rate" in reason.lower():
            mutations.append(Mutation(
                mutation_type="prompt",
                target="Phase AGIR prompt",
                before="(current prompt)",
                after="Add: 'Before implementing, verify prerequisites are met.'",
                reason=reason,
                confidence=0.7,
            ))

        if "declining" in reason.lower():
            mutations.append(Mutation(
                mutation_type="criteria",
                target="Evaluation scoring",
                before="Single score 0-100",
                after="Multi-dimensional: correctness(40%), completeness(30%), quality(30%)",
                reason=reason,
                confidence=0.6,
            ))

        if "low average" in reason.lower():
            mutations.append(Mutation(
                mutation_type="heuristic",
                target="Task decomposition",
                before="Execute task as-is",
                after="Break task into sub-steps before execution",
                reason=reason,
                confidence=0.8,
            ))

    return mutations


def apply_mutation(mutation: Mutation, iteration: int) -> None:
    """Apply a mutation and log it."""
    log_mutation(
        iteration=iteration,
        mutation_type=mutation.mutation_type,
        target=mutation.target,
        before=mutation.before,
        after=mutation.after,
        reason=mutation.reason,
    )
