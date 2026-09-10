from importlib.metadata import PackageNotFoundError, version as _pkg_version

try:
    __version__=_pkg_version("stock_utils")

except:
    __version__="0+unknown"

__all__=["__version__"]
