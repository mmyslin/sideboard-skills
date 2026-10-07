#!/usr/bin/env python3
"""Copy shared/conventions.md into every skills/*/SKILL.md between the markers.

Each skill ships as its own zip, so the shared conventions have to be repeated in
every SKILL.md. This keeps one source of truth. With --check, it changes nothing and
exits 1 if any skill's copy has drifted (build-zips.sh runs that).
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = "<!-- conventions:start -->", "<!-- conventions:end -->"
BLOCK = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)


def main() -> int:
    check = "--check" in sys.argv[1:]
    shared = (ROOT / "shared" / "conventions.md").read_text().strip()
    wanted = f"{START}\n{shared}\n{END}"
    problems = []
    for skill in sorted(ROOT.glob("skills/*/SKILL.md")):
        text = skill.read_text()
        if not BLOCK.search(text):
            problems.append(f"{skill.relative_to(ROOT)}: no conventions markers")
            continue
        updated = BLOCK.sub(lambda _m: wanted, text, count=1)
        if updated != text:
            if check:
                problems.append(f"{skill.relative_to(ROOT)}: conventions out of date")
            else:
                skill.write_text(updated)
                print(f"synced {skill.relative_to(ROOT)}")
    for p in problems:
        print(p, file=sys.stderr)
    if problems:
        if check:
            print("run scripts/sync-conventions.py to fix", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
