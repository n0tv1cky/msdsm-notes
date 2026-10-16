# msdsm-notes

Personal study notes for IIM Indore / IIT Indore's MSDSM program (Batch 6), generated from lecture transcripts and organized for revision.

**Browse:** https://n0tv1cky.github.io/msdsm-notes/ (published via GitHub Pages, `main` branch root)

## Repository layout

```
index.html, .nojekyll   GitHub Pages site root (must stay at the top level)
README.md
scripts/                note-generation tooling (Python, stdlib only)
  generate_notes.py       transcript -> study notes, via the Anthropic API
  sessions.py             reads the canonical session list; naming + front matter
  sync_names.py           renames notes/transcripts when session numbers change
.claude/skills/         Claude Code skill for building recap pages
<term>/
  <dsm-code>-<short-title>/
    lectures/           per-session AI-generated study notes (Markdown)
    recap/              interactive HTML revision pages (only some courses so far)
```

Only `term1/` exists so far. `index.html` is the navigation page linking into every course -- update it when a course gets its first recap page, or when a new term starts. Course material (slides, readings, PDFs, raw transcripts) is not redistributable and never lives here; `*.pdf` is gitignored as a guard.

## Lecture notes (`lectures/*.md`)

Generated from ASR transcripts of the actual lectures by `scripts/generate_notes.py`, detailed enough to build handwritten notes from without having attended. `generate_notes.py` is the single shared script across every course -- course-specific guidance (what to capture precisely: named theorems, code reconstruction, formulas, case-study numbers, etc.) lives in its `COURSE_GUIDANCE` dict, keyed by DSM code. Adding a new course means adding a dict entry, not a new script.

Run it against a course's transcript directory (kept privately outside this repo, not redistributable):

```
python3 scripts/generate_notes.py /path/to/subjects/<dsm-code>-<short-title>/transcripts
```

It skips any `.txt` whose `<term>/<course-dir>/lectures/<name>.md` already exists here, so re-running the whole pipeline is always safe. `TERM` is a hardcoded constant at the top of the script (currently `"term1"`) -- bump it by hand when a new term's courses start; there's no way to infer it from the transcripts path.

**Note on filenames:** notes are named after the recording, e.g. `DSM-103-4_2026-08-29_Somnath-Dey.md`, and each starts with a front-matter block (course, date, start time, session, faculty). A lecture is identified by course + date + start time; its session N is a derived label: the Nth class of the course actually held, in date/time order, taken from the canonical session list the recording sync writes outside this repo. `generate_notes.py` refuses to write a note under a stale number, and `python3 scripts/sync_names.py --fix` renames notes and transcripts together whenever the list changes.

## Recap pages (`recap/*.html`)

Self-contained, single-file interactive pages -- open directly in any browser, no build step, no dependencies beyond CDN font links (plus KaTeX on formula-heavy courses). Dense formula/definition cards for fast pre-exam scanning, plus interactive pieces only where they teach something a card can't. The kind depends on the content: draggable charts for graph-heavy material (DSM-107's Nash solver, technology-choice slider), worked-example and practice-problem reveals for numerical material, predict-the-output cards for code, step-through visualizers for algorithms, and often none for framework-style material.

Built with the Claude Code skill in [`.claude/skills/building-course-recaps/`](.claude/skills/building-course-recaps/SKILL.md). It profiles a course's `lectures/*.md` (`profile_course.py`), classifies each module by content type, proposes a module plan for approval, then builds from `base-template.html` and verifies every displayed number. To start one, ask Claude Code for "a full-course recap for DSM-1xx".
