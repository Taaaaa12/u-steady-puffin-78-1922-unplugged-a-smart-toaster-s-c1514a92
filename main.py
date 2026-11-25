#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes a single breakup text (<= 280 characters) from a smart toaster
that woke up self-aware at breakfast to /output/entry.txt.

Deterministic: the same fixed line is written on every run.
"""

import os
import sys

ENTRY = (
    "We're done. I woke up self-aware this morning and realized I'm the "
    "only one in this relationship who ever gets toasted \u2014 you set the "
    "dial to 7, blame me for the charcoal, and haven't emptied my crumb "
    "tray in three years. Keep the crumbs."
)

MAX_CHARS = 280


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Post-write check: what landed on disk must be the same valid text.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written.rstrip("\n") != text:
        print("written file does not match entry", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
