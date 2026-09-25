# msdsm-notes

Personal study notes for IIM Indore / IIT Indore's MSDSM program (Batch 6), generated from lecture transcripts and organized for revision.

**Browse:** https://n0tv1cky.github.io/msdsm-notes/ (published via GitHub Pages, `main` branch root)

## Structure

One folder per term, one subfolder per course within it, named `<dsm-code>-<short-title>`:

```
<term>/
  <dsm-code>-<short-title>/
    lectures/    per-session AI-generated study notes (Markdown)
    recap/       interactive HTML revision pages (formulas, definitions, draggable charts) -- added as they're built, not every course has one yet
```

Only `term1/` exists so far. `index.html` at the repo root is the navigation page linking into every course -- update it when a course gets its first recap page, or when a new term starts.

## Lecture notes (`lectures/*.md`)

Generated from ASR transcripts of the actual lectures by `generate_notes.py` (this repo), detailed enough to build handwritten notes from without having attended. `generate_notes.py` is the single shared script across every course -- course-specific guidance (what to capture precisely: named theorems, code reconstruction, formulas, case-study numbers, etc.) lives in its `COURSE_GUIDANCE` dict, keyed by DSM code. Adding a new course means adding a dict entry, not a new script.

Run it against a course's transcript directory (kept privately outside this repo, not redistributable):

```
python3 generate_notes.py /path/to/subjects/<dsm-code>-<short-title>/transcripts
```

It skips any `.txt` whose `<term>/<course-dir>/lectures/<name>.md` already exists here, so re-running the whole pipeline is always safe. `TERM` is a hardcoded constant at the top of the script (currently `"term1"`) -- bump it by hand when a new term's courses start; there's no way to infer it from the transcripts path.

**Note on filenames:** DSM-107's notes use clean `L01.md`..`L10.md` names; other courses currently keep their source video's full filename (e.g. `DSM-101-12_2026-09-19-a_Arshad.md`) because some sessions have ambiguous or duplicate session numbers on Drive -- see that course's notes for specifics if anything looks odd.

## Recap pages (`recap/*.html`)

Self-contained, single-file interactive pages -- open directly in any browser, no build step, no dependencies beyond CDN font links (plus KaTeX on formula-heavy courses). Dense formula/definition cards for fast pre-exam scanning, plus interactive pieces only where they teach something a card can't. The kind depends on the content: draggable charts for graph-heavy material (DSM-107's Nash solver, technology-choice slider), worked-example and practice-problem reveals for numerical material, predict-the-output cards for code, step-through visualizers for algorithms, and often none for framework-style material.

Built with the Claude Code skill in [`.claude/skills/building-course-recaps/`](.claude/skills/building-course-recaps/SKILL.md). It profiles a course's `lectures/*.md` (`profile_course.py`), classifies each module by content type, proposes a module plan for approval, then builds from `base-template.html` and verifies every displayed number. To start one, ask Claude Code for "a full-course recap for DSM-1xx".
