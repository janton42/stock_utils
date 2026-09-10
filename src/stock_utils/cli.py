import argparse
import importlib.metadata
import sys
from pathlib import Path

from . import __version__
from .core import Orchestrator

def _build_parser() -> argparse.ArgumentParser:
    prog = importlib.metadata.metadata("practice")["Name"]
    parser = argparse.ArgumentParser(prog=prog, description=(__doc__ or ''))
    parser.add_argument(
        '--version',
        action='version',
        version=f'{prog}  {__version__}',
        help='Show version and exit',
    )

    parser.add_argument(
        '--silent',
        action='store_true',
        help='Disable audio.'
    )

    return parser

def main(argv: list[str]|None=None)->int:
    argv=sys.argv[1:] if argv is None else argv
    parser = _build_parser()

    args=parser.parse_args(argv)
    if hasattr(args, "func"):
        return int(args.func(args) or 0)
    o = Orchestrator('Orchestrator')
    o.menu_loop(args.silent)

    return 0


if __name__=='__main__':
    raise SystemExit(main())
