"""Text summarization using simplified TF-IDF scoring.

Extracts the most important sentences by scoring them based on
word frequency (Term Frequency). No external dependencies.
"""

import re
from collections import Counter

# Common stop words (English + French)
STOP_WORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "shall",
    "should", "may", "might", "can", "could", "of", "in", "to", "for",
    "with", "on", "at", "from", "by", "as", "it", "its", "this", "that",
    "and", "or", "but", "not", "so", "if", "than", "too", "very",
    "le", "la", "les", "un", "une", "des", "du", "de", "et", "ou",
    "est", "sont", "pour", "dans", "sur", "avec", "par", "qui", "que",
}


def split_sentences(text: str) -> list[str]:
    """Split text into sentences."""
    if not text or not text.strip():
        return []
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return [s.strip() for s in sentences if s.strip()]


def score_sentence(sentence: str, word_freq: dict | list) -> float:
    """Score a sentence based on word frequency (TF scoring).

    Args:
        sentence: The sentence to score.
        word_freq: A dict of {word: count} or a list (ignored, for compat).

    Returns:
        Average word frequency score for the sentence.
    """
    if isinstance(word_freq, list):
        word_freq = {}
    words = re.findall(r"\b[a-zA-Z\u00C0-\u017F]+\b", sentence.lower())
    words = [w for w in words if w not in STOP_WORDS and len(w) > 2]
    if not words:
        return 0.0
    freq_score = sum(word_freq.get(w, 0) for w in words) / len(words)
    length_bonus = len(words) * 0.1  # prefer longer sentences
    return freq_score + length_bonus


def _compute_word_freq(sentences: list[str]) -> dict[str, int]:
    """Compute word frequencies across all sentences."""
    all_words = []
    for s in sentences:
        words = re.findall(r"\b[a-zA-Z\u00C0-\u017F]+\b", s.lower())
        all_words.extend(w for w in words if w not in STOP_WORDS and len(w) > 2)
    return dict(Counter(all_words))


def summarize(text: str, max_sentences: int = 3) -> str:
    """Summarize text by extracting the most important sentences.

    Uses simplified TF scoring: sentences containing the most frequent
    words in the text are ranked highest.

    Args:
        text: Input text to summarize.
        max_sentences: Maximum number of sentences to return.

    Returns:
        A summary string with the top-ranked sentences in original order.
    """
    if not text or not text.strip():
        return ""

    sentences = split_sentences(text)
    if not sentences:
        return ""
    if len(sentences) <= max_sentences:
        return " ".join(sentences)

    word_freq = _compute_word_freq(sentences)

    scored = []
    for i, s in enumerate(sentences):
        score = score_sentence(s, word_freq)
        scored.append((score, i, s))

    scored.sort(reverse=True, key=lambda x: x[0])
    selected = scored[:max_sentences]
    selected.sort(key=lambda x: x[1])  # restore original order

    return " ".join(s for _, _, s in selected)


if __name__ == "__main__":
    demo = (
        "Python is a programming language. "
        "It was created by Guido van Rossum. "
        "Python is used for web development. "
        "It supports multiple paradigms. "
        "Python has a large standard library. "
        "Many companies use Python in production."
    )
    print("Input:", demo)
    print("Summary:", summarize(demo, 2))
    print()
    print("Empty:", repr(summarize("")))
    print("Short:", summarize("Just one sentence."))
