"""Tests for core module."""
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from offline_translator.core import MODEL_PATH, TOKENIZER_PATH


def test_model_loading() -> None:
    """Test if the model can be loaded."""
    AutoTokenizer.from_pretrained(TOKENIZER_PATH)
    AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)
