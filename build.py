"""Download huggingface models and tokenizers."""
import os
import pathlib
import warnings

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

HF_PATH = (
    pathlib.Path(__file__).parent
    / "offline_translator"
    / "resources"
    / "huggingface"
).resolve()
TOKENIZER_PATH = HF_PATH / "tokenizer"
MODEL_PATH = HF_PATH / "model"

TOKENIZER_PATH.mkdir(parents=True, exist_ok=True)
MODEL_PATH.mkdir(parents=True, exist_ok=True)

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
warnings.filterwarnings("ignore")
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fr-en")
tokenizer.save_pretrained(TOKENIZER_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-fr-en")
model.save_pretrained(MODEL_PATH)
