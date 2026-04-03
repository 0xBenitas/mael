"""Minimal import validation before full test suite."""
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

try:
    from summarize import split_sentences, score_sentence, summarize
    print("✓ Import successful: summarize module found")
    print(f"  - split_sentences: {callable(split_sentences)}")
    print(f"  - score_sentence: {callable(score_sentence)}")
    print(f"  - summarize: {callable(summarize)}")
except ModuleNotFoundError as e:
    print(f"✗ Import failed: {e}")
    sys.exit(1)
