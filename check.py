"""Checks the music before a push: python check.py

- every audio file is in a folder (one per screen), named in lowercase with dashes;
- no file over 95 MB (GitHub refuses a pushed file over 100 MB);
- no more than 900 MB in total (a GitHub Pages site holds 1 GB).

Prints the tracks and their sizes; exits with 1 if something is wrong.
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUDIO = {".mp3", ".m4a", ".ogg", ".opus", ".webm", ".wav", ".flac"}
NAME = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
MB = 1024 * 1024
FILE_MAX, TOTAL_MAX = 95 * MB, 900 * MB


def main():
    errors, total = [], 0
    files = sorted(p for p in HERE.rglob("*") if p.is_file() and ".git" not in p.parts)
    for p in files:
        rel = p.relative_to(HERE).as_posix()
        if p.suffix.lower() not in AUDIO:
            continue
        size = p.stat().st_size
        total += size
        print(f"{size / MB:7.1f} MB  {rel}")
        if len(p.relative_to(HERE).parts) != 2:
            errors.append(f"{rel}: put it in the folder of its screen (<folder>/<file>)")
        for part in (p.parent.name, p.stem):
            if not NAME.fullmatch(part):
                errors.append(f"{rel}: {part!r} is not lowercase-with-dashes")
        if size > FILE_MAX:
            errors.append(f"{rel}: {size / MB:.1f} MB, over 95 MB (GitHub refuses 100 MB): encode it smaller or split it")
    print(f"{total / MB:7.1f} MB  in total (GitHub Pages holds 1 GB)")
    if total > TOTAL_MAX:
        errors.append(f"{total / MB:.0f} MB in total, over 900 MB")
    for e in errors:
        print("error:", e, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
