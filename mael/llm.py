"""LLM integration for MAEL — multi-model support with cost optimization.

Uses tiered models:
- Haiku for routine phases (AGIR, ÉVALUER, APPRENDRE) — cheap & fast
- Sonnet for meta-reasoning (MUTER) — smarter, used sparingly
"""

import os
import anthropic

# Model tiers
FAST = "claude-haiku-4-5-20251001"
SMART = "claude-sonnet-4-20250514"

_client: anthropic.Anthropic | None = None


def get_client() -> anthropic.Anthropic:
    """Get or create the Anthropic client."""
    global _client
    if _client is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY not set. "
                "Export it: export ANTHROPIC_API_KEY=sk-ant-..."
            )
        _client = anthropic.Anthropic(api_key=api_key)
    return _client


def ask(prompt: str, system: str = "", model: str = FAST,
        max_tokens: int = 2048, temperature: float = 0.3) -> str:
    """Send a prompt to Claude and return the response text.

    Args:
        prompt: The user message.
        system: Optional system prompt.
        model: Model to use (FAST or SMART).
        max_tokens: Max response tokens.
        temperature: Sampling temperature (lower = more focused).

    Returns:
        The assistant's response text.
    """
    client = get_client()
    kwargs = {
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system:
        kwargs["system"] = system

    response = client.messages.create(**kwargs)
    return response.content[0].text


def ask_for_json(prompt: str, system: str = "", model: str = FAST,
                 max_tokens: int = 2048) -> str:
    """Ask Claude and expect a JSON response."""
    full_system = (system + "\n\n" if system else "")
    full_system += "Respond ONLY with valid JSON. No markdown, no explanation."
    return ask(prompt, system=full_system, model=model, max_tokens=max_tokens,
               temperature=0.1)


def estimate_cost(input_tokens: int, output_tokens: int, model: str = FAST) -> float:
    """Estimate cost in USD for a given token count."""
    rates = {
        FAST: {"input": 0.80 / 1_000_000, "output": 4.00 / 1_000_000},
        SMART: {"input": 3.00 / 1_000_000, "output": 15.00 / 1_000_000},
    }
    r = rates.get(model, rates[FAST])
    return input_tokens * r["input"] + output_tokens * r["output"]
