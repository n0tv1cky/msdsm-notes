# msdsm-notes

Personal study notes for IIM Indore / IIT Indore's MSDSM program (Batch 6), generated from lecture transcripts and organized for revision.

## Structure

One folder per course, named `<dsm-code>-<short-title>`:

```
<dsm-code>-<short-title>/
  lectures/    per-session AI-generated study notes (Markdown)
  recap/       interactive HTML revision pages (formulas, definitions, draggable charts) -- added as they're built, not every course has one yet
```

## Lecture notes (`lectures/*.md`)

Generated from ASR transcripts of the actual lectures by `generate_notes.py` (this repo), detailed enough to build handwritten notes from without having attended. `generate_notes.py` is the single shared script across every course -- course-specific guidance (what to capture precisely: named theorems, code reconstruction, formulas, case-study numbers, etc.) lives in its `COURSE_GUIDANCE` dict, keyed by DSM code. Adding a new course means adding a dict entry, not a new script.

Run it against a course's transcript directory (kept privately outside this repo, not redistributable):

```
python3 generate_notes.py /path/to/subjects/<dsm-code>-<short-title>/transcripts
```

It skips any `.txt` whose `<course-dir>/lectures/<name>.md` already exists here, so re-running the whole pipeline is always safe.

**Note on filenames:** DSM-107's notes use clean `L01.md`..`L10.md` names; other courses currently keep their source video's full filename (e.g. `DSM-101-12_2026-09-19-a_Arshad.md`) because some sessions have ambiguous or duplicate session numbers on Drive -- see that course's notes for specifics if anything looks odd.

## Recap pages (`recap/*.html`)

Self-contained, single-file interactive pages -- open directly in any browser, no build step, no dependencies beyond two CDN font links. Dense formula/definition cards for fast pre-exam scanning, plus a handful of small draggable charts per course that let you test the mechanics (a payoff-matrix Nash solver, a wage/technology-choice slider, etc.) instead of just re-reading.
