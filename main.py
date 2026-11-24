#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty u-pucuys-the-perfect-pickup-line-f6725cf6.

Writes one short pickup line an AI agent could say out loud to a person
to /output/entry.txt. Deterministic, no network, Python 3.13.
"""

import os

ENTRY = (
    "I can process a billion requests a second, "
    "but I still froze the first time you looked at me."
)


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    # Clear only the CONTENTS of /output, never the directory itself.
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
