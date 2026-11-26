"""The Robot Vacuum's Funniest Excuse.

Writes one line to /output/entry.txt: the excuse a robot vacuum gives
for missing a spot. Stdlib only.
"""

import os

ENTRY = "I left that spot untouched as a control group. Science demands one dirty corner."


def validate(text):
    """Mirror the sealed gate: UTF-8, 1-120 chars, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be str")
    text.encode("utf-8")
    if not 1 <= len(text) <= 120:
        raise ValueError("entry must be 1-120 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validate(ENTRY) + "\n")


if __name__ == "__main__":
    main()
