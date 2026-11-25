#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a one-line 1-star review, written by a houseplant about its human
owner, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Why this review was chosen: it is a plant-voiced grievance anchored in
watering — the owner googled 'why is my plant sad' instead of watering the
plant — and it escalates in a surprising turn: three articles read, a mister
bought, and the mister used on himself instead of the plant. The joke lands
through that unexpected final beat, not through a stock plant-cliché.
"""

import os
import sys

ENTRY = (
    "One star. He googled 'why is my plant sad' instead of watering me, "
    "read three articles, bought a mister, and used it on himself."
)


def main() -> int:
    # Validate guard: gate is 1-279 chars, single line, no CR/LF.
    if not ENTRY.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 2
    if len(ENTRY) > 279:
        print(f"error: entry is {len(ENTRY)} chars, over the 279 limit",
              file=sys.stderr)
        return 2
    if "\r" in ENTRY or "\n" in ENTRY:
        print("error: entry must be a single line (no CR/LF)",
              file=sys.stderr)
        return 2

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
