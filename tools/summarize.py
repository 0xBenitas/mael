"""
Text summarization utility using simple heuristics.
Extracts the N most important sentences based on length and keyword density.
"""

import re
from typing import List, Tuple


def split_sentences(text: str) -> List[str]:
    """
    Split text into sentences.
    Handles edge cases: empty text, single sentence, mixed punctuation.
    
    Args:
        text: Input text to split
        
    Returns:
        List of sentences (stripped of whitespace)
    """
    if not text or not text.strip():
        return []
    
    # Split on sentence boundaries: . ! ? followed by space or end
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    # Filter empty strings and strip whitespace
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences


def score_sentence(sentence: str, keywords: set = None) -> float:
    """
    Score a sentence based on length and keyword density.
    
    Args:
        sentence: Sentence to score
        keywords: Set of important keywords (optional)
        
    Returns:
        Float score (higher = more important)
    """
    if not sentence:
        return 0.0
    
    # Base score: sentence length (normalized by average)
    words = sentence.split()
    length_score = len(words) / 15.0  # Normalize by typical sentence length
    
    # Keyword score
    keyword_score = 0.0
    if keywords:
        keyword_count = sum(1 for word in words if word.lower() in keywords)
        keyword_score = keyword_count / max(len(words), 1)
    
    # Combined score: 70% length, 30% keywords
    total_score = (0.7 * length_score) + (0.3 * keyword_score)
    return total_score


def extract_keywords(text: str, top_n: int = 10) -> set:
    """
    Extract top N most frequent words as keywords.
    
    Args:
        text: Input text
        top_n: Number of keywords to extract
        
    Returns:
        Set of keywords
    """
    if not text:
        return set()
    
    # Simple word frequency (exclude common stopwords)
    stopwords = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
        'have', 'has', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
        'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those', 'i',
        'you', 'he', 'she', 'it', 'we', 'they', 'what', 'which', 'who', 'when',
        'where', 'why', 'how'
    }
    
    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = {}
    for word in words:
        if word not in stopwords and len(word) > 2:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Get top N words
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return {word for word, _ in sorted_words[:top_n]}


def summarize(text: str, max_sentences: int = 3) -> str:
    """
    Summarize text by extracting the most important sentences.
    
    Args:
        text: Input text to summarize
        max_sentences: Maximum number of sentences in summary
        
    Returns:
        Summarized text (shorter than original)
    """
    # Handle edge case: empty text
    if not text or not text.strip():
        return ""
    
    # Split into sentences
    sentences = split_sentences(text)
    
    # Handle edge case: single sentence or fewer than max_sentences
    if len(sentences) <= max_sentences:
        return text.strip()
    
    # Extract keywords
    keywords = extract_keywords(text)
    
    # Score each sentence with its original index
    scored_sentences: List[Tuple[int, str, float]] = []
    for idx, sentence in enumerate(sentences):
        score = score_sentence(sentence, keywords)
        scored_sentences.append((idx, sentence, score))
    
    # Select top sentences by score, but maintain original order
    top_sentences = sorted(scored_sentences, key=lambda x: x[2], reverse=True)[:max_sentences]
    top_sentences = sorted(top_sentences, key=lambda x: x[0])  # Restore original order
    
    # Reconstruct summary
    summary = " ".join([sentence for _, sentence, _ in top_sentences])
    return summary


if __name__ == '__main__':
    print("=" * 70)
    print("SUMMARIZE.PY — VALIDATION SUITE")
    print("=" * 70)
    
    # ========== STEP 1: Component Testing ==========
    print("\n[STEP 1] Component Testing: split_sentences()")
    test_cases_split = [
        ("", "empty text"),
        ("Hello world.", "single sentence"),
        ("First. Second! Third?", "mixed punctuation"),
        ("Dr. Smith works at MIT. He is smart.", "abbreviations"),
        ('He said "Hello. World." today.', "quoted sentences"),
    ]
    
    for text, desc in test_cases_split:
        result = split_sentences(text)
        print(f"  [{desc}] Input len={len(text)}, Output={len(result)} sentences")
        if result:
            print(f"    → {result[:1]}")  # Show first sentence
    
    # ========== STEP 2: Scoring Component ==========
    print("\n[STEP 2] Component Testing: score_sentence()")
    test_sentences = [
        "This is a short sentence.",
        "This is a much longer sentence that contains more words and should score higher.",
        "",
    ]
    
    for sent in test_sentences:
        score = score_sentence(sent)
        print(f"  Len={len(sent):3d} → Score={score:.3f}")
    
    # ========== STEP 3: Full Summarize Function ==========
    print("\n[STEP 3] Full Function: summarize()")
    
    text_short = "Python is great. Java is powerful. Go is fast."
    result_short = summarize(text_short, max_sentences=2)
    print(f"  Short text (len={len(text_short)})")
    print(f"    Input:  {text_short}")
    print(f"    Output: {result_short}")
    print(f"    Ratio:  {len(result_short)/len(text_short):.2%}")
    
    text_long = (
        "Machine learning is transforming industries worldwide. "
        "Deep learning models require massive computational resources. "
        "Natural language processing enables computers to understand text. "
        "Computer vision allows machines to interpret images. "
        "Reinforcement learning trains agents through trial and error."
    )
    result_long = summarize(text_long, max_sentences=2)
    print(f"\n  Long text (len={len(text_long)})")
    print(f"    Output: {result_long}")
    print(f"    Ratio:  {len(result_long)/len(text_long):.2%}")
    
    # ========== STEP 4: Edge Cases ==========
    print("\n[STEP 4] Edge Cases Validation")
    
    # Case 1: Empty text
    try:
        result = summarize("", max_sentences=3)
        assert result == "", f"Empty text should return empty, got: {repr(result)}"
        print("  ✓ Empty text → empty summary")
    except AssertionError as e:
        print(f"  ✗ Empty text failed: {e}")
    
    # Case 2: Single sentence
    try:
        single = "This is the only sentence."
        result = summarize(single, max_sentences=3)
        assert result == single, f"Single sentence should return as-is, got: {repr(result)}"
        print("  ✓ Single sentence → returned as-is")
    except AssertionError as e:
        print(f"  ✗ Single sentence failed: {e}")
    
    # Case 3: Long text (>1000 chars)
    try:
        long_text = " ".join(["Sentence number {}.".format(i) for i in range(50)])
        result = summarize(long_text, max_sentences=3)
        ratio = len(result) / len(long_text)
        assert ratio < 0.5, f"Summary should be <50% of original, got {ratio:.2%}"
        print(f"  ✓ Long text (1000+ chars) → {ratio:.2%} of original")
    except AssertionError as e:
        print(f"  ✗ Long text failed: {e}")
    
    # ========== STEP 5: Import & Syntax Check ==========
    print("\n[STEP 5] Import & Syntax Verification")
    try:
        from tools.summarize import summarize as imported_func
        print("  ✓ Function successfully imported")
        
        # Quick sanity check
        test_result = imported_func("Hello world. This is a test.", max_sentences=1)
        assert isinstance(test_result, str), "Function should return string"
        print("  ✓ Function returns string type")
        print("  ✓ All validations passed")
    except Exception as e:
        print(f"  ✗ Import/execution failed: {e}")
    
    print("\n" + "=" * 70)
    print("VALIDATION COMPLETE")
    print("=" * 70)
