#!/usr/bin/env python3
"""Check (and with --fix, apply) canonical names and front matter for lecture
notes and their transcripts, from the session list in sessions.json (see
sessions.py).

Run after any Drive rename. Notes (<TERM>/<course>/lectures/<name>.md) and
the private transcript pair (subjects/<course>/transcripts/<name>.txt/.vtt)
are renamed together; otherwise generate_notes.py would regenerate every
renamed lecture under its old name. Each note's leading front-matter block
(course, date, start, session, faculty) is rewritten to match.

Usage: python3 scripts/sync_names.py [--fix]
"""
import subprocess
import sys
from pathlib import Path

from sessions import load, lookup, name_of, with_front_matter

REPO = Path(__file__).resolve().parent.parent
TERM = "term1"
SUBJECTS = Path("/Users/n0tv1cky/Documents/Personal/masters/subjects")


def tracked(path):
    return subprocess.run(["git", "ls-files", "--error-unmatch", str(path)],
                          cwd=REPO, capture_output=True).returncode == 0


def move(src, dst):
    if tracked(src):
        subprocess.run(["git", "mv", str(src), str(dst)], cwd=REPO, check=True)
    else:
        src.rename(dst)


def plan(sessions):
    moves, fronts, problems = [], [], []
    for course_dir in sorted((REPO / TERM).glob("dsm*")):
        code = course_dir.name[3:6]
        notes = list((course_dir / "lectures").glob("*.md"))
        tdir = SUBJECTS / course_dir.name / "transcripts"
        trans = list(tdir.glob("*.txt")) + list(tdir.glob("*.vtt")) if tdir.is_dir() else []
        for f in notes + trans:
            entry, why = lookup(code, f.stem, sessions)
            if entry is None:
                problems.append(f"{course_dir.name}/{f.name}: {why}")
                continue
            dst = f.with_name(name_of(entry) + f.suffix)
            if dst != f:
                moves.append((f, dst))
            if f.suffix == ".md":
                text = f.read_text(encoding="utf-8")
                if with_front_matter(text, entry) != text:
                    fronts.append((dst, entry))
    targets = [d for _, d in moves]
    for d in set(targets):
        if targets.count(d) > 1:
            problems.append(f"two files would be renamed to {d.name}")
    sources = {s for s, _ in moves}
    for _, d in moves:
        if d.exists() and d not in sources:
            problems.append(f"{d.name} already exists and is not itself being renamed")
    return moves, fronts, problems


def main():
    fix = "--fix" in sys.argv
    moves, fronts, problems = plan(load())
    verb = "RENAME" if fix else "WOULD RENAME"
    for s, d in sorted(moves):
        print(f"{verb}: {s.parent.parent.name}/{s.parent.name}/{s.name} -> {d.name}")
    for d, _ in fronts:
        print(f"{'UPDATE' if fix else 'WOULD UPDATE'} front matter: {d.name}")
    for p in problems:
        print("PROBLEM:", p)
    if not fix:
        print(f"\n{len(moves)} rename(s), {len(fronts)} front-matter update(s), "
              f"{len(problems)} problem(s). Re-run with --fix to apply.")
        return
    if any("would be renamed" in p or "already exists" in p for p in problems):
        sys.exit("Refusing to rename: name collisions above.")
    # Two phases so chained renames (10->9, 11->10, 10->11) can't clobber each other.
    tmp = [(s, s.with_name(s.name + ".renaming"), d) for s, d in moves]
    for s, t, _ in tmp:
        move(s, t)
    for _, t, d in tmp:
        move(t, d)
    for d, entry in fronts:
        d.write_text(with_front_matter(d.read_text(encoding="utf-8"), entry), encoding="utf-8")
    print(f"\nRenamed {len(moves)} file(s), updated front matter on {len(fronts)} note(s).")


if __name__ == "__main__":
    main()
