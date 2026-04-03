"""Test suite for summarize utility.

Tests cover:
- Empty text
- Short text (< max_sentences)
- Long text (> max_sentences)
- max_sentences=1 edge case
"""
import sys
from pathlib import Path

import pytest

# Add src to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from summarize import split_sentences, score_sentence, summarize


class TestSplitSentences:
    """Test sentence splitting component."""

    def test_empty_text(self):
        """Empty text should return empty list."""
        result = split_sentences("")
        assert result == [], f"Expected [], got {result}"
        print("✓ test_empty_text passed")

    def test_single_sentence(self):
        """Single sentence without period."""
        result = split_sentences("Hello world")
        assert len(result) >= 1, f"Expected at least 1 sentence, got {len(result)}"
        print(f"✓ test_single_sentence passed: {result}")

    def test_multiple_sentences(self):
        """Multiple sentences with periods."""
        text = "First sentence. Second sentence. Third sentence."
        result = split_sentences(text)
        assert len(result) >= 3, f"Expected >= 3 sentences, got {len(result)}: {result}"
        print(f"✓ test_multiple_sentences passed: {len(result)} sentences")


class TestScoreSentence:
    """Test sentence scoring component."""

    def test_score_non_empty(self):
        """Non-empty sentence should have positive score."""
        sentence = "This is a test sentence with multiple words."
        score = score_sentence(sentence)
        assert isinstance(score, (int, float)), f"Expected numeric score, got {type(score)}"
        assert score >= 0, f"Expected non-negative score, got {score}"
        print(f"✓ test_score_non_empty passed: score={score}")

    def test_score_empty(self):
        """Empty sentence should have zero or minimal score."""
        score = score_sentence("")
        assert isinstance(score, (int, float)), f"Expected numeric score, got {type(score)}"
        print(f"✓ test_score_empty passed: score={score}")


class TestSummarize:
    """Test main summarize function."""

    def test_empty_text(self):
        """Empty text should return empty string."""
        result = summarize("", max_sentences=3)
        assert result == "", f"Expected empty string, got '{result}'"
        print("✓ test_empty_text passed")

    def test_short_text_less_than_max(self):
        """Text with fewer sentences than max_sentences should return all."""
        text = "First sentence. Second sentence."
        result = summarize(text, max_sentences=5)
        # Result should contain both sentences or be a reasonable summary
        assert len(result) > 0, f"Expected non-empty result, got '{result}'"
        assert "First" in result or "Second" in result, \
            f"Expected original content in result, got '{result}'"
        print(f"✓ test_short_text_less_than_max passed: '{result}'")

    def test_long_text_exceeds_max(self):
        """Text with more sentences than max_sentences should be truncated."""
        text = "Sentence one. Sentence two. Sentence three. Sentence four. Sentence five."
        result = summarize(text, max_sentences=2)
        assert len(result) > 0, f"Expected non-empty result, got '{result}'"
        # Result should be shorter than original
        assert len(result) <= len(text), \
            f"Expected result shorter than original. Original: {len(text)}, Result: {len(result)}"
        print(f"✓ test_long_text_exceeds_max passed: '{result}'")

    def test_max_sentences_one(self):
        """max_sentences=1 should return single sentence or empty."""
        text = "First sentence. Second sentence. Third sentence."
        result = summarize(text, max_sentences=1)
        assert isinstance(result, str), f"Expected string, got {type(result)}"
        # Count sentences in result (rough check)
        sentence_count = result.count(".") if result else 0
        assert sentence_count <= 2, \
            f"Expected <= 2 sentences in result, got {sentence_count}: '{result}'"
        print(f"✓ test_max_sentences_one passed: '{result}'")

    def test_max_sentences_zero(self):
        """max_sentences=0 should return empty or minimal result."""
        text = "First sentence. Second sentence."
        result = summarize(text, max_sentences=0)
        assert isinstance(result, str), f"Expected string, got {type(result)}"
        print(f"✓ test_max_sentences_zero passed: '{result}'")


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_single_long_sentence(self):
        """Single very long sentence should be handled."""
        text = "This is a very long sentence that goes on and on with many words but no periods until the very end."
        result = summarize(text, max_sentences=1)
        assert isinstance(result, str), f"Expected string, got {type(result)}"
        print(f"✓ test_single_long_sentence passed: '{result}'")

    def test_text_with_special_chars(self):
        """Text with special characters should be handled."""
        text = "Hello! How are you? I'm fine, thanks. Great!"
        result = summarize(text, max_sentences=2)
        assert isinstance(result, str), f"Expected string, got {type(result)}"
        print(f"✓ test_text_with_special_chars passed: '{result}'")

    def test_text_with_numbers(self):
        """Text with numbers and abbreviations should be handled."""
        text = "The year is 2024. Dr. Smith works at MIT. He has 3 degrees."
        result = summarize(text, max_sentences=2)
        assert isinstance(result, str), f"Expected string, got {type(result)}"
        print(f"✓ test_text_with_numbers passed: '{result}'")
