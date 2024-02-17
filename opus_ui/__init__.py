"""Main module."""

from .cli import entrypoint
from .core import DISTRIBUTION, METADATA, hello

__all__ = [
    "entrypoint",
    "DISTRIBUTION",
    "METADATA",
    "hello",
]
