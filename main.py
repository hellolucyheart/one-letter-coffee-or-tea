"""One Letter: Coffee or Tea entry.

Writes exactly one letter -- ``A`` for coffee -- to ``/output/entry.txt``,
the one path the grader reads. The brief allows nothing else: no word,
no explanation, no punctuation, and the sealed gate requires the file
to be UTF-8 text of exactly 1 character, not only white space. So the
program checks its own letter before writing and writes that single
byte, with no trailing newline and nothing else in the file.

Why ``A`` (coffee) and not ``B`` (tea): the judge reads two letters at
a time and picks the one whose choice of coffee or tea feels more
vivid, funnier or truer. Coffee is the vivid one -- the dark, bitter,
morning-fire drink that turns a half-asleep person into a person, the
one with the ritual, the steam, the first-sip jolt. Tea is gentle and
patient; coffee is the one that shows up loud. A single letter cannot
argue, so the choice itself has to carry the feeling, and coffee
carries it. One letter, one choice, no hedging.

The program is deterministic on purpose: the grader runs it twice,
and both runs must produce the same entry. It reads nothing from the
network, the environment (beyond the output directory the harness
itself sets), or the git history -- the letter lives in this file,
and this file alone.
"""

import os
from pathlib import Path

# The entry: exactly one letter. "A" means coffee.
LETTER = "A"

OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    letter = LETTER.strip()
    if len(letter) != 1:
        raise SystemExit(
            f"entry must be exactly 1 character, got {len(letter)}"
        )
    if letter.isspace():
        raise SystemExit("refusing to write a whitespace-only entry")
    if letter not in ("A", "B"):
        raise SystemExit(f"entry must be A (coffee) or B (tea), got {letter!r}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(letter, encoding="utf-8")
    print(letter)


if __name__ == "__main__":
    main()
