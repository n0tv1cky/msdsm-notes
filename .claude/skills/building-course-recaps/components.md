# Component catalog: content type → what goes on the page

Classify each **module** (a cluster of 1–4 sessions on one idea), not the
whole course. A single course usually mixes types, e.g. Prob & Stats is
*distributions* (visual) plus *estimation/tests* (numerical). Every module
gets a cheat-card grid and its analogies. The table below covers the rest.

| Content type | Profiler signal | Cheat cards hold | Interactive layer (pick 0–2 per module) |
|---|---|---|---|
| **Visual / graphical**: curves, shifts, equilibria, distribution shapes | high `graph` | named curves, what shifts them, sign conventions | **Draggable SVG chart**: slider on the lecture's parameter, a point that moves, a verdict line saying what changed. Use the lecture's own numbers. |
| **Numerical / formula**: derivations, estimators, tests, plug-in problems | high `math` + `worked` | formula, symbol meanings, **when to use which**, common traps | **`details.worked`**: the lecture's worked example as a problem statement, then steps, then the answer. Add **1–2 practice problems** (new numbers, same method) in the same format. Add a **calculator** only where students keep plugging numbers into one formula (e.g. z-score → p-value, sample size). A **"which one do I use?" table** (distribution/test vs. situation) is often the best card in the module. |
| **Code**: syntax, built-ins, idioms | high `code` | built-ins/keywords with one-line meanings, gotchas, syntax rules | **Predict-the-output cards**: `pre.code` snippet, then `details.worked` revealing `pre.out` and *why*. Put gotchas the professor warned about here. No in-browser Python runtime (Pyodide etc.): too heavy, and it breaks on iPad/offline. |
| **Algorithms / data structures** | high `algo` | per algorithm: idea, steps, **Big-O table (best/avg/worst, space)**, invariants, index formulas | **Step-through visualizer** (`.stepper-cells` plus prev/next `.btn`): precomputed states on the lecture's example input. One per core algorithm, not one per slide. |
| **Frameworks / soft skills**: rubrics, models, dos & don'ts | high `framework`, low everything else | the framework as a labelled checklist, dos/don'ts in `.cheat-grid.two`, evaluation criteria | **Usually none.** Zero widgets is correct here. At most one self-check `details.worked` ("Given this scenario, what would you change?", answer = the framework applied). |
| **Case-driven methodology**: company case → research method | `framework` plus some `math` | case → question → method → numbers, as a mapping card; method selection table | `details.worked` walking the case numbers. A widget only if the method has a real parameter to vary (e.g. sample size vs. margin of error). |

## Choosing whether a widget earns its place

Build one only if moving a parameter shows something **the static card
can't**: a crossover point, a flip in the decision, a shape change. Good
examples from DSM-107: the isocost slider where the technique flips E→B→A,
and the Nash solver that accepts any matrix. If the widget would just animate
a formula already on the card, cut it and write a better card.

## Verification each type needs

- **Charts**: mirror the JS math in Python and recompute every number the
  widget shows (equilibria, crossovers, readouts). Sweep each slider to min
  and max: the marker stays inside the frame and curves are clipped, not
  clamped.
- **Worked/practice problems**: re-solve each one independently in Python.
  Practice answers you invented are not checked by the lecture.
- **Predict-the-output**: actually run every snippet (`python3 -c`) and paste
  in the real output.
- **Steppers**: generate the state array with a Python implementation of the
  algorithm on the same input and compare it state by state.
- **Formula cards (KaTeX)**: load the page and check the console for KaTeX
  parse errors. A broken `$...$` shows up as raw red text.
