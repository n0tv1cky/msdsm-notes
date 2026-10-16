"""Canonical lecture identity and labels, looked up from the zoom sync's list.

A lecture is identified by (course, date, start time). Its label, session N,
is derived: the Nth class of the course actually held, in date/time order (a
combined double class gets a range label such as "12-13"). The zoom-recordings
sync writes the full list to ~/.zoom-recordings-sync/sessions.json after every
run. That file holds Drive file IDs, so it is read from outside this public
repo and never copied in.

Notes and transcripts are named after the recording minus ".mp4", e.g.
"DSM-103-4_2026-08-29_Somnath-Dey", and each note starts with a front-matter
block giving course, date, start and session.
"""
import json
import re
from pathlib import Path

SESSIONS_JSON = Path.home() / ".zoom-recordings-sync" / "sessions.json"

# "DSM-101-12_2026-09-19-a_Arshad", "DSM-102-12-13_2026-10-10_Abhirup-Datta"
STEM_RE = re.compile(r"^DSM-(\d+)-[\d-]+?_(\d{4}-\d{2}-\d{2})(?:-([a-z]))?_", re.I)
# Legacy DSM-107 names (L01..), matched by session number.
L_RE = re.compile(r"^L(\d+)$", re.I)
FRONT_RE = re.compile(r"\A---\n.*?\n---\n\n?", re.S)


def _start_minutes(start):
    m = re.match(r"(\d+):(\d+)\s*([ap]m)", start.strip(), re.I)
    h, mi, ap = int(m.group(1)), int(m.group(2)), m.group(3).lower()
    return (h % 12 + (12 if ap == "pm" else 0)) * 60 + mi


def load():
    """{course_code: [session dicts sorted by date, start]}"""
    data = json.loads(SESSIONS_JSON.read_text())
    by_course = {}
    for s in data["sessions"]:
        code = re.search(r"\d+", s["course"]).group(0)
        by_course.setdefault(code, []).append(s)
    for lst in by_course.values():
        lst.sort(key=lambda s: (s["date"], _start_minutes(s["start"])))
    return by_course


def name_of(entry):
    return entry["fileName"].rsplit(".", 1)[0]


def lookup(code, stem, sessions):
    """(sessions.json entry, None) for a transcript/note stem, or (None, reason).

    Matched by course + date. When a course met twice that day, an exact
    canonical name or an "-a"/"-b" suffix (start-time order) picks the class.
    """
    lst = sessions.get(code, [])
    m = L_RE.match(stem)
    if m:
        hits = [s for s in lst if str(s["session"]) == str(int(m.group(1)))]
        return (hits[0], None) if hits else (None, "no such session")
    m = STEM_RE.match(stem)
    if not m:
        return None, "unrecognised name"
    date, suffix = m.group(2), (m.group(3) or "").lower()
    hits = [s for s in lst if s["date"] == date]
    if not hits:
        return None, f"no session on {date}"
    if len(hits) == 1:
        return hits[0], None
    exact = [s for s in hits if name_of(s) == stem]
    if exact:
        return exact[0], None
    if not suffix:
        return None, f"{len(hits)} sessions on {date}, name has no -a/-b"
    idx = ord(suffix) - ord("a")
    if idx >= len(hits):
        return None, f"suffix -{suffix} but only {len(hits)} sessions on {date}"
    return hits[idx], None


def front_matter(entry):
    return (
        "---\n"
        f"course: {entry['course']}\n"
        f"date: {entry['date']}\n"
        f"start: {entry['start']}\n"
        f"session: \"{entry['session']}\"\n"
        f"faculty: {entry['faculty'].strip()}\n"
        "---\n\n"
    )


def with_front_matter(text, entry):
    """Replace any leading front-matter block with the canonical one."""
    return front_matter(entry) + FRONT_RE.sub("", text, count=1)
