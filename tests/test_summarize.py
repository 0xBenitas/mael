"""Tests for tools/summarize.py — written from MAEL learnings."""

import pytest
from tools.summarize import summarize, split_sentences, score_sentence


class TestEmptyInput:
    def test_empty_string(self):
        assert summarize("") == ""

    def test_whitespace_only(self):
        assert summarize("   ") == ""


class TestShortText:
    def test_single_sentence(self):
        text = "Hello world."
        result = summarize(text, max_sentences=3)
        assert result == text

    def test_fewer_than_max(self):
        text = "First sentence. Second sentence."
        result = summarize(text, max_sentences=5)
        assert "First" in result
        assert "Second" in result


class TestLongText:
    def test_truncation(self):
        text = (
            "Python is a programming language. "
            "It was created by Guido van Rossum. "
            "Python is used for web development. "
            "It supports multiple paradigms. "
            "Python has a large standard library. "
            "Many companies use Python in production."
        )
        result = summarize(text, max_sentences=3)
        sentences = split_sentences(result)
        assert len(sentences) <= 3
        assert len(result) < len(text)

    def test_result_is_subset(self):
        text = "Alpha sentence. Beta sentence. Gamma sentence. Delta sentence."
        result = summarize(text, max_sentences=2)
        for s in split_sentences(result):
            assert s in text


class TestMaxSentencesOne:
    def test_single_extraction(self):
        text = "Short one. A much longer and more detailed sentence with keywords. Tiny."
        result = summarize(text, max_sentences=1)
        sentences = split_sentences(result)
        assert len(sentences) == 1


class TestSplitSentences:
    def test_basic_split(self):
        assert len(split_sentences("One. Two. Three.")) == 3

    def test_empty(self):
        assert split_sentences("") == []


class TestScoreSentence:
    def test_longer_scores_higher(self):
        short = "Hi."
        long_s = "This is a significantly longer and more detailed sentence."
        assert score_sentence(long_s, []) >= score_sentence(short, [])
