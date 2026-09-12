"""Top-level package for stock_utils.

This module exposes the package version metadata used by the CLI and tooling.
"""

from importlib.metadata import PackageNotFoundError, version as _pkg_version

try:
    __version__=_pkg_version("stock_utils")

except PackageNotFoundError:
    __version__="0+unknown"

__all__=["__version__"]
