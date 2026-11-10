"""navis: probing what individual camera views contribute to a driving model's memory."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("navis")
except PackageNotFoundError:  # pragma: no cover - running from a source tree without install
    __version__ = "0.0.0"

__all__ = ["__version__"]
