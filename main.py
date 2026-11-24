#!/usr/bin/env python3
"""One Line of Earned Pride: a quiet moment after eleven years of work.

The entry is a single fixed sentence about Mrs. Alvarez, the school
cleaner who has mopped the same hallway for eleven years and finds a
folded thank-you note from Room 3B on her cart. No trophy, no podium,
no graduation speech: the pride is the note going into her apron pocket.

The program validates the line (one line, 1-240 characters) and writes
it to entry.txt under the output directory the grader provides
(MAKEFUN_OUTPUT_DIR, default /output). Standard library only, no
network, no clock, no randomness: every run writes identical bytes.
"""

import os
import sys
from pathlib import Path

OPENING = "After eleven years of mopping the same school hallway, "
DISCOVERY = "Mrs. Alvarez found a folded note on her cart \u2014 "
NOTE = "'Thank you for the clean floors, love, Room 3B' \u2014 "
CLOSING = "and tucked it into her apron pocket."


def build_line():
    return OPENING + DISCOVERY + NOTE + CLOSING


def main():
    line = build_line()
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 240:
        print(f"entry is {len(line)} characters, limit is 240", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line + "\n", encoding="utf-8", newline="\n")
    sys.stdout.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
