# fridge-text-3am: the one line a smart fridge texts its owner at 3am

# The entry program: writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt
# (default /output/entry.txt), the message a smart fridge sends its owner
# at 3am. Deterministic: the same bytes on every run.
# No network, no input, standard library only.
#
# Try it locally:
#   MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt

import os
from pathlib import Path

ENTRY = "3am. Four times tonight, nothing taken. I am a fridge, not a hobby."

assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"


def main() -> None:
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = Path(target_dir) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
