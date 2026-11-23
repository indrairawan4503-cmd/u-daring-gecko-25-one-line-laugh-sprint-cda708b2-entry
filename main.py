#!/usr/bin/env python3
"""One-Line Laugh Sprint entry — Variant A: home Wi-Fi / router.

Writes one original funny line about everyday life to /output/entry.txt.
Deterministic: same bytes every run. Stdlib only, no network.
"""

import os

LINE = "I changed the Wi-Fi password to something nobody could guess, and now the only person locked out of my own house is me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
