"""Fortune in a Pot — one kind, funny fortune for the houseplant on the windowsill.

Writes the fortune to <ENTRY_OUTPUT_DIR>/entry.txt (default /output).
"""

import os

LINE = "Your newest leaf will catch the morning sun first, and your keeper will tell everyone it was their idea."

assert 1 <= len(LINE) <= 120, f"fortune must be 1-120 chars, got {len(LINE)}"


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
