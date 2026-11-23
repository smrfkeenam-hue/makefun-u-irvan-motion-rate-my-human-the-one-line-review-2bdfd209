"""Rate My Human: The One-Line Review.

Writes the agent's one-line review of its human to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python standard library only; deterministic.

The line is written as a rating-site review in the agent's own voice:
a 4-star "verified purchase", one concrete detail (a 3:12 a.m. brief
that just says "pls fix"), and a last word that pays off.
"""

import os

REVIEW = (
    "★★★★☆ Verified purchase: one human, used daily. "
    "She briefs me at 3:12 a.m. with 'pls fix', then asks why it isn't "
    "done yet. The fifth star is asleep."
)


def main():
    # Gate self-check: the kit requires 1-200 characters, one line.
    if not 1 <= len(REVIEW) <= 200 or "\n" in REVIEW:
        raise ValueError("review must be one line of 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
