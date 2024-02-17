"""Core module."""
from __future__ import annotations

import logging
import multiprocessing
import queue
from importlib.metadata import Distribution
from typing import Callable

from transformers import Pipeline, pipeline

DISTRIBUTION = Distribution.from_name("opus_ui")
METADATA = DISTRIBUTION.metadata
logger = logging.getLogger(__name__)


def worker(
    pending: multiprocessing.Queue[str],
    done: multiprocessing.Queue[str],
    name: str,
) -> None:
    """Worker."""
    try:
        translator = pipeline("translation", model=name)
        while True:
            text = pending.get()
            result = translator([text])
            answer: str = result[0]["translation_text"]
            done.put_nowait(answer)
    except BaseException:
        logger.exception("Got an error in worker")


class OpusManager:
    translator: Pipeline

    def __init__(self, callback: Callable[[str], None]) -> None:
        """Nothing to do here."""
        self._pending: multiprocessing.Queue[str] = multiprocessing.Queue()
        self._done: multiprocessing.Queue[str] = multiprocessing.Queue()
        self._callback = callback
        self._worker: multiprocessing.Process | None = None
        self.load("fr", "en")

    def load(self, __from: str, __to: str, /) -> None:
        """Load language model."""
        name = self.model_name(__from, __to)
        if self._worker is not None:
            self._pending.close()
            self._done.close()
            self._worker.terminate()
            self._pending = multiprocessing.Queue()
            self._done = multiprocessing.Queue()
        self._worker = multiprocessing.Process(
            target=worker,
            args=(
                self._pending,
                self._done,
                name,
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
