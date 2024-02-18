"""Module for hold informations."""
from importlib.metadata import Distribution

DISTRIBUTION = Distribution.from_name("offline-translator")
METADATA = DISTRIBUTION.metadata

__author__ = METADATA["Author"]
__license__ = METADATA["License"]
__version__ = METADATA["Version"]
__maintainer__ = METADATA["Maintainer-email"]
__email__ = METADATA["Maintainer"]
__summary__ = METADATA["Summary"]
