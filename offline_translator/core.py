"""Core module."""
from __future__ import annotations

import contextlib
import logging
import multiprocessing
import os
import pathlib
import queue
import string
from typing import Callable

ALPHA_NUM = set(string.ascii_letters) | set(string.digits)
MODEL = (
    pathlib.Path(__file__).parent
    / "resources"
    / "huggingface"
    / "Helsinki-NLP"
    / "opus-mt-fr-en"
).resolve()
logger = logging.getLogger(__name__)


def worker(
    pending: multiprocessing.Queue[str],
    done: multiprocessing.Queue[str],
) -> None:
    """Worker."""
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    os.environ["HF_DATASETS_OFFLINE"] = "1"
    os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

    try:
        logging.basicConfig(
            level=logging.DEBUG,
            format="[%(asctime)s] %(levelname)-8s - %(message)s",
        )
        logger.info("Starting worker")

        tokenizer = AutoTokenizer.from_pretrained(MODEL)
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL)
        logger.info("Worker ready")
        while True:
            text = pending.get()
            while not pending.empty():
                text = pending.get()
            has_text = set(text.strip()) & ALPHA_NUM
            if has_text:
                text = text.replace("\n", "<n>")
                input_ids = tokenizer.encode(
                    text,
                    return_tensors="pt",
                )
                outputs = model.generate(input_ids)
                answer: str = tokenizer.decode(
                    outputs[0],
                    skip_special_tokens=True,
                )
                answer = answer.replace("<n>", "\n")
            else:
                answer = text
            done.put_nowait(answer)
    except KeyboardInterrupt:
        logger.info("Shutdown worker")
    except BaseException:
        logger.exception("Got an error in worker")


class ModelWorker:
    def __init__(self, callback: Callable[[str], None]) -> None:
        """Nothing to do here."""
        self._pending: multiprocessing.Queue[str] = multiprocessing.Queue()
        self._done: multiprocessing.Queue[str] = multiprocessing.Queue()
        self._callback = callback
        self._worker: multiprocessing.Process | None = None
        self.load("fr", "en")

    def load(self, __from: str, __to: str, /) -> None:
        """Load language model."""
        self.model_name(__from, __to)
        if self._worker is not None:
            self.close()
            self._pending = multiprocessing.Queue()
            self._done = multiprocessing.Queue()
        self._worker = multiprocessing.Process(
            target=worker,
            args=(
                self._pending,
                self._done,
            ),
        )
        self._worker.start()

    @staticmethod
    def model_name(__from: str, __to: str, /) -> str:
        """Get model name from destination and source language."""
        return f"Helsinki-NLP/opus-mt-{__from}-{__to}"

    def submit(self, text: str) -> None:
        """Translate text."""
        logger.info("Submit %r", text)
        self._pending.put(text)

    def update(self) -> None:
        """Call all callback with the current text."""
        try:
            while True:
                translation = self._done.get_nowait()
                logger.info("Translate %r", translation)
                self._callback(translation)
        except queue.Empty:
            pass

    def close(self) -> None:
        """Close the worker."""
        self._pending.close()
        self._done.close()
        with contextlib.suppress(AttributeError):
            self._worker.terminate()  # type: ignore[union-attr]

    def __del__(self) -> None:
        """Cleanup object."""
        self.close()
