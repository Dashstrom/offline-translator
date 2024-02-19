"""Tests for core module."""
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from offline_translator.core import MODEL


def test_model_loading() -> None:
    """Test if the model can be loaded."""
    AutoTokenizer.from_pretrained(MODEL)
    AutoModelForSeq2SeqLM.from_pretrained(MODEL)
