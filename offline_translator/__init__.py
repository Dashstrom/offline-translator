"""Main module."""

from .cli import entrypoint
from .core import ModelWorker
from .info import (
    __author__,
    __email__,
    __license__,
    __maintainer__,
    __summary__,
    __version__,
)
from .ui import OfflineTranslator

__all__ = [
    "entrypoint",
    "ModelWorker",
    "__author__",
    "__email__",
    "__license__",
    "__maintainer__",
    "__summary__",
    "__version__",
    "OfflineTranslator",
]
