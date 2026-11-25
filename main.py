#!/usr/bin/env python3
"""Entry generator for "Make the AI Judge Laugh" (make.fun).

Writes one office-life joke, a single line under 200 characters,
to /output/entry.txt. Deterministic: same bytes on every run.

Crafted against the judge brief, most important first:
1. About office life, lands as a joke (meetings and email).
2. True to the office: everyone has sat in a meeting that should
   have been an email.
3. Surprising turn: the escalation keeps going -- the email itself
   could have been a shrug.
4. Tight: two short sentences, no wasted setup, reads aloud in
   one breath.
5. Original phrasing: the "shrug" escalation is not a stock line.
"""

import os

ENTRY = "The meeting could have been an email. The email could have been a shrug."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Gate check: the sealed scorer requires 1-200 UTF-8 characters.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.replace(tmp_path, OUTPUT_PATH)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
