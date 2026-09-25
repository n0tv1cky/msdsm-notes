---
name: building-course-recaps
description: Use when asked to make a full-course recap, revision page, cheat sheet, exam-prep page, or interactive notes for an MSDSM course in projects/msdsm-notes, or to extend an existing recap with new lectures.
---

# Building course recaps

## Overview

A recap is **one self-contained HTML page per course** at
`<term>/<course-dir>/recap/course-recap.html`, built from that course's
`lectures/*.md`. It is for **fast pre-exam revision**: dense cheat cards
first, the professor's analogies next to them, and interactive pieces only
where they teach something a card can't. The kind of interactive piece
depends on the content, so every build starts by analysing the course.

Reference implementation: `term1/dsm107-managerial-economics/recap/course-recap.html`.

## Workflow (every step is required)

1. **Profile.** Run `python3 .claude/skills/building-course-recaps/profile_course.py <term>/<course-dir>/lectures`
   from the repo root. It prints per-session signal density (math, code,
   graph, worked, algo, framework) in recording-date order (session labels on
   Drive are unreliable), plus duplicate and missing session numbers. `COURSE_GUIDANCE` in `generate_notes.py` is
   a second hint. Both are evidence, not the verdict.
2. **Read every lecture note.** Group the sessions into 4–8 **modules**
   (topic clusters). For each module, record:
   - its content type, from [components.md](components.md) (**per module**: most courses mix types)
   - the formulas, definitions, and rules worth a cheat card
   - **the professor's analogies, stories, and repeated points**, with their session. The user values these most, and a page with only formulas misses the point.
   - the lecture's own worked numbers (widgets and examples use these, not invented ones)
3. **Present the module plan and wait for approval.** Show a table with
   these columns: module | sessions | type | cheat cards | interactive pieces (or "none: why") | key analogies.
   Also flag any duplicate or missing sessions from step 1.
4. **Build** from [base-template.html](base-template.html). Delete the
   component blocks you don't use. Rules:
   - Concise: cards are fragments, not paragraphs. No hero blurb, only a kicker line.
   - Leave out admin content (quiz rules, grading, logistics) unless asked.
   - Any callout with more than one idea is a bulleted `.note` (`<p>` lead-in, then `<ul>`), never one dense paragraph.
   - Color thread: amber = one side of the module's central contrast, teal = the other. Keep the pairing consistent across the whole page.
   - KaTeX only if the course is formula-heavy. Otherwise use `<code>` formulas.
5. **Verify.** Follow the per-type checks in [components.md](components.md) (Python recompute, slider sweeps, running snippets). Then:
   - open the page in the browser pane, check for zero console errors, and try each jump-nav link
   - test the print version by injecting the `@media print` rules as a live `<style>`, running `document.querySelectorAll('details').forEach(d => d.open = true)` (injected CSS never fires `beforeprint`), then taking a screenshot
   - test a phone-width viewport: with all `<details>` open, `document.documentElement.scrollWidth === clientWidth` (no horizontal scroll)
   - re-scan the lecture notes for analogies you dropped
6. **Publish.**
   - Add an `Interactive recap` pill to that course's row in the root `index.html`.
   - Commit in `projects/msdsm-notes`.
   - **Ask before pushing.**
   - After the push, confirm the GitHub Pages build (`gh api repos/n0tv1cky/msdsm-notes/pages/builds/latest`) and that the recap URL returns 200.

## Extending an existing recap

Re-profile. Put the new sessions into existing modules or a new module
(show the user a plan diff first). Then do steps 4–6 for the changed parts only.

## Common mistakes

| Mistake | Fix |
|---|---|
| Labelling a whole course "numerical", so every module gets the same widget | Classify each module. Prob & Stats needs distribution sliders *and* worked-problem reveals. |
| Adding a chart to framework content to look interactive | Zero widgets is a valid result. Put the effort into cards. |
| Widget numbers that are plausible but wrong | Recompute them in Python. DSM-107 shipped a chart whose MRS was €59 against the stated €30 until this check caught it. |
| A slider that pushes the marker off the chart | Sweep min to max and resize the axes to fit the full range. |
| Clamping curve y to the frame | Clip the path instead. Clamping draws fake flat segments. |
| Native `#anchor` links | Use the template's JS scroll handler. Anchors fail in the preview pane. |
| Session order taken from `ls` or from session numbers | `ls` sorts 1, 10, 11, 2, and DSM-101 has "S12" recordings dated after S15. Use the profiler's date order. |
| Sharing a local `.html` for iPad | Quick Look doesn't run JS. Share the GitHub Pages URL. |
