from __future__ import annotations

import argparse
import json
from pathlib import Path

from .models import Note, ProjectState, Snippet, Task


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ticket_ledger")
    subparsers = parser.add_subparsers(dest="command")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
