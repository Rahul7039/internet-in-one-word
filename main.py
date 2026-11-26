"""The Internet in One Word — entry program.

Writes the chosen word, byte-identical, to /output/entry.txt.
The word is a fixed constant: it is never generated or paraphrased.
"""

WORD = "highschool"

# Gate guards: one word, 1-30 chars, no whitespace of any kind.
assert isinstance(WORD, str)
assert 1 <= len(WORD) <= 30, f"word must be 1-30 chars, got {len(WORD)}"
assert WORD == WORD.strip(), "word must not have leading/trailing whitespace"
assert not any(ch.isspace() for ch in WORD), "word must be a single word (no spaces)"

def main() -> None:
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

if __name__ == "__main__":
    main()
