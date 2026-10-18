#!/usr/bin/env python3
"""Add previous/next links to every lecture note, in the order classes were held.

GitHub lists a lectures/ folder alphabetically (S1, S10, S11, ..., S2), so each
note gets a navigation line just below its front matter and again at the end.
Order comes from each note's own front matter (date, then start time), so this
needs nothing outside the repo. The lines sit between <!-- nav --> markers and
are rewritten on every run, so it is safe to re-run; generate_notes.py and
sync_names.py --fix call it after changing notes.

Usage: python3 scripts/nav_links.py
"""
import re
from pathlib import Path

from sessions import FRONT_RE, _start_minutes

REPO = Path(__file__).resolve().parent.parent
NAV_RE = re.compile(r"<!-- nav -->\n.*?<!-- /nav -->\n*", re.S)


def field(front, key):
    m = re.search(rf"^{key}: \"?(.*?)\"?$", front, re.M)
    return m.group(1) if m else ""


def nav_line(prev, nxt):
    def link(note):
        return f"[Session {note['session']} ({note['date']})]({note['path'].name})"
    parts = [
        f"← {link(prev)}" if prev else "← (first lecture)",
        "[All lectures](./)",
        f"{link(nxt)} →" if nxt else "(latest lecture) →",
    ]
    return "<!-- nav -->\n" + " · ".join(parts) + "\n<!-- /nav -->\n"


def update_lectures_dir(lectures_dir):
    """Rewrite the nav lines of every note in one lectures/ folder; return how many changed."""
    notes = []
    for path in lectures_dir.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        m = FRONT_RE.match(text)
        if not m:
            print(f"SKIP (no front matter): {path.relative_to(REPO)}")
            continue
        front = m.group(0)
        notes.append({
            "path": path,
            "text": text,
            "front": front,
            "body": NAV_RE.sub("", text[len(front):]).rstrip() + "\n",
            "date": field(front, "date"),
            "session": field(front, "session"),
            "start": _start_minutes(field(front, "start")),
        })
    notes.sort(key=lambda n: (n["date"], n["start"]))
    changed = 0
    for i, note in enumerate(notes):
        nav = nav_line(notes[i - 1] if i else None, notes[i + 1] if i + 1 < len(notes) else None)
        new = note["front"].rstrip("\n") + "\n\n" + nav + "\n" + note["body"] + "\n" + nav
        if new != note["text"]:
            note["path"].write_text(new, encoding="utf-8")
            changed += 1
    return changed


def update_all():
    changed = sum(update_lectures_dir(d) for d in sorted(REPO.glob("term*/*/lectures")))
    print(f"Navigation links updated in {changed} note(s).")


if __name__ == "__main__":
    update_all()
