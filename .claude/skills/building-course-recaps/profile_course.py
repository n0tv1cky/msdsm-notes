#!/usr/bin/env python3
"""Profile a course's lecture notes to decide what kind of recap page it needs.

Prints per-lecture signal counts (math, code, graph/curve language, worked
numbers, frameworks/cases, algorithms, analogies) in *session order* and a
course-level mix. These are evidence for the module plan, not a verdict --
read the flagged lectures before deciding what a module should contain.

Usage: python3 profile_course.py <path-to>/<term>/<course-dir>/lectures
"""
import re
import sys
from pathlib import Path

SIGNALS = {
    # $...$ / $$...$$ blocks -> formula density
    "math": re.compile(r"\$\$.+?\$\$|\$[^$\n]+?\$", re.S),
    # fenced code blocks
    "code": re.compile(r"^```", re.M),
    # things you'd draw: curves, axes, shifts, shapes of distributions
    "graph": re.compile(
        r"\b(curve|axis|axes|slope|intercept|graph|plot|diagram|shift(s|ed)? (left|right|up|down|outward|inward)|"
        r"indifference|isoquant|isocost|frontier|budget line|demand|supply|equilibrium|histogram|"
        r"distribution|bell[- ]shaped|peak|tail|pdf|cdf)\b", re.I),
    # worked numerical problems
    "worked": re.compile(r"\b(worked example|example:|numerical|compute|calculate|solution|substitut\w+|plug\w* in)\b", re.I),
    # step-by-step procedures / data-structure mechanics
    "algo": re.compile(
        r"\b(algorithm|pseudocode|O\(|big[- ]o|complexity|traversal|insert(ion)?|delet(e|ion)|push|pop|"
        r"enqueue|dequeue|pointer|node|recurs\w+|sort\w*|search\w*|stack|queue|linked list|tree|array)\b", re.I),
    # frameworks, rubrics, case studies, dos/don'ts
    "framework": re.compile(
        r"\b(framework|model of|rubric|checklist|do's|don'ts|dos and don'ts|principle|case study|case of|"
        r"evaluation criteria|audience|structure of|stakeholder|methodology|hypothesis|survey|sampling design)\b", re.I),
    # weak proxy only -- analogies are rarely phrased with these words; a low
    # score does NOT mean none. Always read the notes for them.
    "analogy": re.compile(r"\b(analog\w+|like a|think of|imagine|metaphor|story|anecdote|intuition|intuitively)\b", re.I),
}

# Session ordering: "DSM-101-12_2026-09-19-a_Arshad" or "L07"
NAME_RE = re.compile(r"DSM-\d+-(\d+)_(\d{4}-\d{2}-\d{2})(?:-([a-z]))?", re.I)
L_RE = re.compile(r"^L(\d+)$", re.I)


def parse(stem):
    """(session_number, date, suffix); number 10**6 = unrecognised name."""
    m = NAME_RE.search(stem)
    if m:
        return (int(m.group(1)), m.group(2), m.group(3) or "")
    m = L_RE.match(stem)
    if m:
        return (int(m.group(1)), "", "")
    return (10**6, stem, "")


def session_key(stem):
    # Date first: Drive filenames' session numbers are unreliable (e.g. two
    # "S12" recordings dated after S14/S15), so the recording date is the
    # true teaching order. Undated names (L01..L10) fall back to the number.
    n, date, suffix = parse(stem)
    return (date or "", n, suffix)


def label(stem):
    n, date, suffix = parse(stem)
    if n == 10**6:
        return stem[:22]
    return f"S{n:02d}" + (f" {date}{('-' + suffix) if suffix else ''}" if date else "")


def main():
    lectures = Path(sys.argv[1]).resolve()
    files = sorted(lectures.glob("*.md"), key=lambda p: session_key(p.stem))
    if not files:
        sys.exit(f"No .md notes in {lectures}")

    cols = list(SIGNALS)
    totals = dict.fromkeys(cols, 0.0)
    print(f"{lectures.parent.name}: {len(files)} lecture notes\n")
    print(f"{'session':<20}{'words':>7}" + "".join(f"{c:>10}" for c in cols) + "   (per 1k words; analogy = weak proxy)")

    seen = {}
    for p in files:
        text = p.read_text(encoding="utf-8")
        words = max(len(text.split()), 1)
        counts = {c: len(r.findall(text)) for c, r in SIGNALS.items()}
        counts["code"] //= 2  # opening + closing fence
        per_k = {c: counts[c] * 1000 / words for c in cols}
        for c in cols:
            totals[c] += per_k[c]
        n = parse(p.stem)[0]
        seen.setdefault(n, []).append(p.stem)
        print(f"{label(p.stem):<20}{words:>7}" + "".join(f"{per_k[c]:>10.1f}" for c in cols))

    print("\ncourse mean       " + " " * 7 + "".join(f"{totals[c] / len(files):>10.1f}" for c in cols))

    dupes = {n: s for n, s in seen.items() if len(s) > 1 and n != 10**6}
    if dupes:
        print("\nDuplicate session numbers (distinct recordings -- keep both, don't merge blindly):")
        for n, stems in sorted(dupes.items()):
            print(f"  S{n:02d}: " + ", ".join(stems))
    nums = sorted(n for n in seen if n != 10**6)
    gaps = [n for n in range(nums[0], nums[-1] + 1) if n not in seen] if nums else []
    if gaps:
        print("Missing session numbers (no notes): " + ", ".join(f"S{n:02d}" for n in gaps))
    order = [parse(p.stem)[0] for p in files]
    if any(b < a for a, b in zip(order, order[1:])):
        print("Session numbers go backwards in date order -- some labels are likely wrong; "
              "table above is in recording-date order.")


if __name__ == "__main__":
    main()
