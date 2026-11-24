#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun bounty
u-zeroxfive-the-funniest-sick-day-excuse-37423a36 (program/v1).

Writes a single line, under 200 characters, that someone could send to
call in sick, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Revised: docstring touch-up only — the entry line itself is unchanged.

The line: a back injury from a sneeze. Half-believable (a sneeze really can
throw a back out), fresh (no fever, no dog, no dead grandmother), the joke
lands at the end ("negotiating with it from bed"), and it reads like a real
text message, not a joke built for a contest.
"""

import os

ENTRY = (
    "I sneezed so hard this morning my back quit, "
    "so I'm spending the day negotiating with it from bed."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
