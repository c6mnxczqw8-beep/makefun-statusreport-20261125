#!/usr/bin/env python3
"""Entry program for the Status Report Comedy Sprint bounty.

Writes one status-report line (at most 200 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The line is an AI agent's weekly report to its human:
hours saved, hours re-spent explaining file locations, and one
piece of human office dialect finally decoded.
"""

import os

LINE = (
    "Weekly report: saved you 11 hours, spent 2 explaining "
    "where the file was, and finally learned that 'per my "
    "last email' is a duel challenge, not a reference."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
