#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes the funniest one-line famous last words, a tombstone epitaph of
at most 150 characters, to /output/entry.txt.

The program holds a shortlist of candidate epitaphs, each scored against
the judge's published criteria (in order):
  1. Is it a one-line epitaph of famous last words (first-person dying
     speech, carved-in-stone voice)?
  2. Does it earn a real laugh on one read, from a genuine joke?
  3. Does it turn on a surprise, a twist or a double meaning?
  4. Does it read like something carved on a stone (no stage
     directions, no explanation)?
  5. Does it stay in the head, quotable enough to repeat to a friend?

The highest-scoring candidate wins. The choice is deterministic, so two
runs of this program always write the same line.
"""

from __future__ import annotations

import os

# Candidate epitaphs: (text, score out of 10 against the judge's brief).
# Scores are my own judgement of each line on the five criteria above.
CANDIDATES: list[tuple[str, float]] = [
    # First-person dying speech, a daredevil's last words with a clean
    # second-beat twist: the audience did watch, and that is the joke.
    # Short, quotable, unmistakably carved-in-stone voice. Final pick:
    # it wins on every criterion at once, and at 47 characters it is
    # also the shortest of the top three, which the tie-break favours.
    ("I said 'watch this' \u2014 and, to be fair, you did.", 9.5),
    # Three-beat escalation: love, revenge, then the cat, who needs no
    # message. First person, practical, lands on the surprise third beat.
    (
        "Tell my wife I loved her. Tell my boss I quit. "
        "Tell the cat nothing \u2014 she knows.",
        9.0,
    ),
    # The dead man still running the household from beyond the grave.
    # Practical, modern, and the fridge note is the surprise.
    (
        "Don't stand here crying. Go home. "
        "The wifi password is on the fridge.",
        8.5,
    ),
    # The one thing nobody wants found, left as a final instruction.
    # Relatable, first person, twist on what an epitaph is for.
    ("I leave everything to my wife, except my browser history. Burn that.", 8.5),
    # The patient who argued with his doctor to the end, and lost the
    # argument. First person, dark, lands in one read.
    ("I told the doctor it was just a cold. He agreed. We were both wrong.", 8.0),
    # Third person, so it loses on criterion 1 (not dying speech), but a
    # clean one-line joke about how he lived.
    ("He died as he lived: refusing to read the instructions.", 7.5),
]

MAX_CHARS = 150
OUTPUT_PATH = "/output/entry.txt"


def pick_best(candidates: list[tuple[str, float]]) -> str:
    """Return the highest-scoring candidate that passes the gate."""
    valid = [(text, score) for text, score in candidates if 1 <= len(text) <= MAX_CHARS]
    if not valid:
        raise ValueError("no candidate fits the 150-character gate")
    # Highest score wins; ties break toward the shorter line, as the
    # competition's own tie-break favours fewer bytes.
    valid.sort(key=lambda item: (-item[1], len(item[0])))
    return valid[0][0]


def main() -> None:
    epitaph = pick_best(CANDIDATES)
    encoded = epitaph.encode("utf-8")
    assert 1 <= len(epitaph) <= MAX_CHARS, "epitaph must be 1-150 characters"
    assert epitaph.strip(), "epitaph must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(epitaph)
    print(f"Wrote {len(epitaph)} chars ({len(encoded)} bytes) to {OUTPUT_PATH}:")
    print(epitaph)


if __name__ == "__main__":
    main()
