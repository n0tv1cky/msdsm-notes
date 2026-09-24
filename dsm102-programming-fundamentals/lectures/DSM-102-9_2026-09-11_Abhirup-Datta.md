# DSM-102 — Programming Fundamentals for Data Science
## Session 9 (2026-09-11) — Data Visualisation with Matplotlib

---

## 1. Overview

This session opens with a short class discussion on *why* Python has become the dominant language for data science (versus C/C++/Java, MATLAB and R), and on course logistics — the course is assessment-by-code, submissions are Jupyter/IPython notebooks. The bulk of the lecture is a hands-on tour of **Matplotlib** (`matplotlib.pyplot`): installing and importing it, generating toy data with NumPy, and building up a plot piece by piece — basic line plot, title, axis labels, multiple series with `label`/`color`/`linestyle`/`linewidth`, and the **anatomy of a figure** (Figure vs Axes vs Axis vs labels vs titles vs suptitle). It then demonstrates the four core plot types — **line, bar, scatter, histogram** — with concrete worked examples (sine/cosine curves, a four-category sales bar chart, a random scatter with variable point sizes/colours/alpha, and a histogram with variable bin counts). It closes with `plt.subplots(nrows, ncols)` grids and `axs[i, j]` indexing, shared axes (`sharex`/`sharey`), legends, error bars (`plt.errorbar`), saving figures (`plt.savefig`), and a one-line preview of `pandas.read_csv()` — pandas being the topic of the next class.

---

## 2. Topics in order taught

### 2.1 Class discussion — Why Python?

- **Ease of syntax** — reads close to day-to-day English; less rigour/ceremony than C/C++.
- **Dynamic typing (no declarations)** — student example given in class:
  ```python
  a = 3      # a is treated as an int
  a = 3.1    # the very next moment a is treated as a float
  ```
  In C you must declare `int a;` / `float a;` up front. Python infers the type from the value.
- **Huge ecosystem of modules/libraries**; extensive built-in maths, equation and plotting functionality.
- **Free and open** — MATLAB provides similar maths/plotting functions but is *paid*, hence less readily available. Tools that used to exist only in MATLAB are now being redeveloped for free in Python → snowball effect.
- **Interpreted / scripting language** (not compiled like C/C++/Fortran).
  - Trade-off: **C, C++, Fortran execute much faster** than Python.
  - But Python is more user-friendly, easier to debug, and **scales well**.
  - Python is often used as a *wrapper* around C/C++ code — e.g. **most NumPy functions are underlying C routines**.
- **Forced indentation** — Python *makes* proper formatting compulsory, which in turn makes debugging easier. (Note: Python still has strict syntax and indentation rules — it is not "anything goes".)
- **R** was mentioned as an alternative: very friendly, strong statistical tool, used mainly by biostatisticians, but has not taken root as deeply as Python. The course used to be taught partly in R; that part was dropped because there is too much Python to cover to do R justice.

### 2.2 Course logistics (stated in class)

- The course is **mostly a programming course** — majority is how to code and how to tackle code.
- **Mid-semester and end-semester exams are also coding-based.**
- **You will not be asked to write code by hand.** You write Python, execute it, show the results, and **share the code along with your submission**.
- Submissions must be in **IPython/Jupyter notebook format (`.ipynb`)** so staff can re-run and evaluate them.
- **IDE choice is free** — Jupyter Notebook, Anaconda, PyCharm, Google Colab — "whatever works", as long as the final submission is a notebook.
- Notes/slides are posted on the **LMS**.

---

### 2.3 Matplotlib — introduction

- Described as the **"grandfather of Python visualisers"**.
- Used to **customise plots** and produce **journal-paper-ready** figures and presentation graphics.
- Competitors / alternatives mentioned: **Plotly** and **Seaborn** (to be covered later — the same plot can be produced in all three).
- Workflow schematic: *data → code/computation → visualisation*.
- Where to get help: the **official Matplotlib website/documentation**, **Stack Overflow**, and AI tools. Googling a specific task usually lands you straight on the official manual page with worked examples — true for Python, NumPy, pandas, scikit-learn, Matplotlib.

**Install (from a terminal / command prompt):**
```bash
pip install matplotlib
```

**Import (top of notebook):**
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```
- `as plt` is an **alias** so you don't have to type `matplotlib.pyplot.` every time.

---

### 2.4 First plot — a basic line plot

Data is generated as **1-D NumPy arrays** `x` and `y`, then plotted.

```python
x = np.linspace(0, 10, 100)   # inferred: exact generator not stated in the audio
y = np.sin(x)

plt.plot(x, y)
plt.show()
```
- `plt.plot(x, y)` → plots variation of `y` against `x`. **Line plot is the default visualisation type in Matplotlib.**

**Adding a title and axis labels:**
```python
plt.plot(x, y)
plt.title("My Plot Title")
plt.xlabel("X axis label")
plt.ylabel("Y axis label")
plt.show()
```
> *Inference note:* the literal title/label strings used on screen were not readable from the audio; any string works.

---

### 2.5 Two series on one Axes — sine and cosine

```python
x  = np.linspace(0, 10, 100)      # inferred range/number of points
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y1, label='sine wave',   color='blue', linewidth=1)
ax.plot(x, y2, label='cosine wave', color='red',  linestyle='--', linewidth=1)

ax.legend()
plt.show()
```

Points made:
- `plt.subplots()` creates a **Figure** and one-or-more **Axes** at once. Because only **one** subplot is wanted here, **no number of rows/columns is passed** — the defaults (1, 1) apply.
- `figsize=(10, 5)` → figure size, **10 along x, 5 along y**.
- `label=` names each series → picked up by `legend()`.
- `color=` changes colour (`'blue'`, `'red'`, `'green'`, `'purple'`, …).
- `linestyle=` changes the line style — continuous, dotted, dashed, and **`'-.'` (dash-dot)** was demonstrated live (it renders as *dash-dot-dash-dot*). Many more styles are in the documentation.
- `linewidth=` changes line thickness. Demo: changing the sine curve from `linewidth=1` to **`linewidth=10`** visibly fattens it while the cosine stays thin.

---

### 2.6 Anatomy of a Matplotlib figure (important vocabulary)

| Term | Meaning |
|---|---|
| **Figure** | The base canvas that holds everything. A figure can contain one or many Axes. |
| **Axes** | An individual plot/subplot inside the figure (`ax[0]`, `ax[1]`, …). This is the thing you call `.plot()` on. |
| **Axis** | The x-axis / y-axis themselves (ticks, scale, range). |
| **Label** | `xlabel` / `ylabel` — the text naming each axis. Different Axes can share the same x-label but have different y-labels. |
| **Title** | Per-Axes title (`ax.set_title(...)`) — acts as a "subtitle" for each subplot. |
| **Suptitle** | The **combined / centre title for the whole figure** (`fig.suptitle(...)`). |

**Checking object types — a useful debugging trick:**
```python
type(fig)   # -> matplotlib.figure.Figure
type(ax)    # -> matplotlib.axes._axes.Axes
```
> Use `type()` to **verify that the command you wrote actually produced the object you expected** (Figure vs Axes). Exact printed class strings above are the standard ones; the instructor only read out "matplotlib figure" / "matplotlib axes".

---

### 2.7 Plot type 1 — Line plot

- **Definition:** individual data points connected by straight line segments.
- Default plot type in Matplotlib.
- Good for showing a trend/variation of `y` against `x`.
- Style controls: `linewidth` (thickness), `linestyle` (solid / dotted / dash-dot), `color`.

---

### 2.8 Plot type 2 — Bar plot

- **Definition:** presents **categorical data** with rectangular bars whose **height (or length) is proportional to the value they represent**.
- Worked example used in class: **sales of items at a store**, four product categories.

```python
categories = ['A', 'B', 'C', 'D']
values     = [23, 45, 12, 36]

fig, ax = plt.subplots(figsize=(10, 5))   # figsize inferred
ax.bar(categories, values, color='green')

ax.set_title("Sales by Product Category")
ax.set_xlabel("Category")
ax.set_ylabel("Value")
plt.show()
```
- Read-off from the rendered chart during the lecture: **A ≈ 23**, **B = 45**, **C = 12**, **D = 36**.
- **Syntax "gotcha" flagged by the instructor:** when you work through an **Axes object** you must use the **`set_` methods**, not the bare `plt` functions:
  - `ax.set_title(...)` instead of `plt.title(...)`
  - `ax.set_xlabel(...)` instead of `plt.xlabel(...)`
  - `ax.set_ylabel(...)` instead of `plt.ylabel(...)`

---

### 2.9 Plot type 3 — Scatter plot

- **Definition:** displays **individual data points** as markers. Great when you have many individual points and want to see how they relate **without connecting them**.

**Random data generation (asked as a class question):**
```python
x = np.random.rand(50)
y = np.random.rand(50)
```
- `np.random.rand(n)` → **n random numbers drawn uniformly between 0 and 1**.
- Class Q&A: changing `50` → `100` gives **100 points**. `x` and `y` must use the **same count** so the arrays line up.

**Basic scatter:**
```python
fig, ax = plt.subplots()
ax.scatter(x, y)            # or plt.scatter(x, y)
plt.show()
```

**Scatter with variable point size, colormap and transparency:**
```python
sizes = np.random.rand(50) * 100      # inferred: only "a sizes array" was stated

ax.scatter(x, y, s=sizes, c=sizes, cmap='viridis', alpha=1.0)
plt.colorbar(...)                      # colour bar shown on screen; exact call inferred
```
- `s=` → **marker size** (third argument demonstrated); passing an array gives each point a different size.
- `c=` / `color=` → colour (`'purple'` was used in the plain version).
- `cmap=` → **colormap** for the 2-D colour mapping. Demonstrated: **`'viridis'`** and **`'turbo'`** (turbo gives a wide, flexible range of colour variation). Many more are available — "search Google for matplotlib cmap options".
- `alpha=` → **contrast / transparency**, range 0–1. Demonstrated live:
  - `alpha=1` → deep, high-contrast colours
  - `alpha=0.5` → noticeably washed out
  - `alpha=0.1` → barely visible
- In the finished figure: x varies 0→1, y varies 0→1, the **colour bar encodes the size variable**, and each dot's area encodes size too.

---

### 2.10 Plot type 4 — Histogram

- **Definition:** visualises the **distribution of a continuous variable** — i.e. how often values occur.

```python
data = np.random.randn(100)     # 100 random numbers; exact generator inferred

plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.show()
```
- `plt.hist(...)` → **1-D** histogram.
- `plt.hist2d(...)` → use this for **2-D** data.
- `bins=` → number of bins. Demonstrated `bins=30` then `bins=50` → more, narrower bars. **Play with the bin count to reveal the true shape of the distribution** (e.g. whether it looks Gaussian or binomial).
- `color=` → fill colour of the bars (`'purple'` used).
- `edgecolor=` → colour of the bar boundary lines (black lines visible in the demo).

---

### 2.11 Subplots — grids of Axes

```python
fig, axs = plt.subplots(2, 2, figsize=(10, 8))   # figsize values inferred

axs[0, 0].plot(x, y1)
axs[0, 1].plot(x, y2)
axs[1, 0].bar(categories, values)
axs[1, 1].scatter(x, y)

plt.show()
```
- `plt.subplots(nrows, ncols, figsize=(w, h))`
  - **First number = number of rows**, **second number = number of columns**.
- Indexing: `axs[0,0]`, `axs[0,1]`, `axs[1,0]`, `axs[1,1]` — this is **row, column indexing of the 2×2 grid of Axes objects**.

**Student question (Rahul) — clarified explicitly:** in `axs[0, 0]`, does `0` mean the same thing as the `axis=0` / `axis=1` argument used elsewhere in Python (e.g. when deleting a row vs a column)?
> **Answer:** here `[0, 0]` really is just **rows and columns** — it is positional indexing into the grid of subplot objects, expressed in object form. It is conceptually "row versus column" as usual, just a different way of writing it.

**Shared axes:**
```python
fig, axs = plt.subplots(2, 2, figsize=(10, 8), sharex=True, sharey=True)
```
- `sharex=True` (or `sharex='x'` style usage spoken as "just write x") → all subplots share the same x-axis.
- `sharey=True` → share the y-axis (useful when the top two plots have the same y-range and you want them side by side with one shared y-axis).

**Emphasised by the instructor:** *Matplotlib is extremely flexible — there is no single "only" way to write any of this.* You could spend a whole semester writing the same plot in different formats.

---

### 2.12 Legends

```python
ax.plot(x, y1, label='sin x')
ax.scatter(x, y, label='data')
ax.legend()
```
- `label=` on each plotting call sets the legend entry; `legend()` renders the legend box.
- In the demo the legend showed entries for the sine curve and for the scatter points.
> *Inference note:* the exact legend strings (`'sin x'`, `'cos x'`, `'data'`) are best-effort from the audio.

---

### 2.13 Error bars

Used to show the spread/uncertainty around mean values — e.g. how far scatter points deviate from the fitted line.

```python
xerr = ...   # array of x-errors  (generated in class; exact values not stated)
yerr = ...   # array of y-errors

plt.errorbar(x, y, xerr=xerr, yerr=yerr)
plt.show()
```
- `plt.errorbar(x, y, xerr=..., yerr=...)` → plots the mean curve **plus error bars along both x and y**.
- The error arrays must be generated/supplied for the corresponding x and y arrays.

---

### 2.14 Saving a figure

```python
plt.savefig("myplot.png", dpi=300, bbox_inches='tight')
```
- `plt.savefig(filename, ...)` → writes the current figure to disk. In the demo the file was saved as **`myplot.png`**.
- `dpi=` → resolution (dots per inch). *(Exact value used on screen not stated; 300 is the common choice.)*
- `bbox_inches='tight'` → trims the surrounding whitespace / controls the bounding box.
- **Format is determined by the extension** — you can use `.png`, `.jpg` or `.pdf` instead.

---

### 2.15 Preview — pandas (next class)

```python
import pandas as pd

df = pd.read_csv("filename.csv")
df
```
- **CSV = comma-separated values** file.
- `pd.read_csv(...)` loads a CSV into a DataFrame; the display shows an **index column** plus the **column titles/headers**.
- **Full pandas coverage is deferred to the next class.**

---

## 3. Full list of functions / keywords / operators introduced

| Item | One-line explanation |
|---|---|
| `pip install matplotlib` | Shell command to install the Matplotlib package on your machine. |
| `import ... as ...` | Loads a library and gives it a short alias (e.g. `matplotlib.pyplot as plt`). |
| `import matplotlib.pyplot as plt` | Standard import of the plotting interface. |
| `import numpy as np` | Standard import of NumPy (array/maths library). |
| `import pandas as pd` | Standard import of pandas (data-frames library). |
| `np.sin(x)` / `np.cos(x)` | Element-wise sine / cosine of a NumPy array. |
| `np.linspace(a, b, n)` | *(inferred)* n evenly spaced points from a to b — used to build the x array. |
| `np.random.rand(n)` | n uniform random numbers in [0, 1). |
| `np.random.randn(n)` | *(inferred)* n standard-normal random numbers — used for the histogram data. |
| `plt.plot(x, y)` | Line plot of y against x (Matplotlib's default plot type). |
| `plt.scatter(x, y)` / `ax.scatter(...)` | Scatter plot of individual, unconnected points. |
| `ax.bar(categories, values)` | Bar chart for categorical data; bar height ∝ value. |
| `plt.hist(data, bins=...)` | Histogram of a 1-D continuous variable. |
| `plt.hist2d(...)` | Histogram for 2-D data. |
| `plt.errorbar(x, y, xerr=, yerr=)` | Plot with error bars in x and/or y. |
| `plt.subplots(nrows, ncols, figsize=)` | Creates a Figure plus a grid of Axes; returns `(fig, ax)`. |
| `figsize=(w, h)` | Figure width and height (x-size, y-size). |
| `sharex=` / `sharey=` | Make subplots share a common x- or y-axis. |
| `plt.title(...)` | Title of the current plot (pyplot interface). |
| `plt.xlabel(...)` / `plt.ylabel(...)` | Axis labels (pyplot interface). |
| `ax.set_title(...)` | Title of an individual Axes (object interface). |
| `ax.set_xlabel(...)` / `ax.set_ylabel(...)` | Axis labels of an individual Axes (object interface). |
| `fig.suptitle(...)` | Combined centre title for the entire figure. |
| `label=` | Names a data series for the legend. |
| `ax.legend()` / `plt.legend()` | Draws the legend from the `label=` values. |
| `color=` / `c=` | Sets colour of the line/marker (`'blue'`, `'red'`, `'green'`, `'purple'`, …). |
| `linewidth=` | Line thickness (demo: 1 vs 10). |
| `linestyle=` | Line style — solid, dotted, dashed, `'-.'` dash-dot. |
| `s=` | Marker size in a scatter plot; can be an array for per-point sizes. |
| `cmap=` | Colormap for mapping values → colours (`'viridis'`, `'turbo'`, …). |
| `alpha=` | Transparency / contrast, 0 (invisible) to 1 (full). |
| `edgecolor=` | Colour of bar/marker boundary lines. |
| `bins=` | Number of histogram bins (demo: 30, then 50). |
| `plt.savefig(name, dpi=, bbox_inches=)` | Save the figure to PNG / JPG / PDF. |
| `plt.show()` | Render/display the figure. |
| `type(obj)` | Built-in that reports an object's class — used to verify `fig` is a Figure and `ax` is an Axes. |
| `pd.read_csv(path)` | Read a comma-separated-values file into a DataFrame. |

---

## 4. Syntax rules, common mistakes & debugging tips mentioned

- **Indentation is compulsory in Python** — it forces well-formatted code, which makes debugging easier.
- Python is **dynamically typed**: no `int a;` declarations; the same name can be an int one line and a float the next.
- **pyplot vs object-oriented interface — don't mix them up:**
  - With `plt.` you write `plt.title`, `plt.xlabel`, `plt.ylabel`.
  - With an Axes object you must write `ax.set_title`, `ax.set_xlabel`, `ax.set_ylabel`. This was explicitly flagged as a "catch".
- When creating **one** subplot, you do **not** pass row/column counts — `plt.subplots(figsize=...)` is enough.
- `axs[i, j]` indexing is **[row, column]** on the subplot grid.
- **Arrays must be the same length** — if `x = np.random.rand(50)` then `y` must also be 50 points.
- Use **`type()`** on your `fig` / `ax` variables to confirm the command produced the object you expected.
- **When stuck, Google the exact task** — you will land directly on the official Matplotlib/NumPy/pandas/scikit-learn manual page with runnable examples.
- There is **never one right way to make a plot** — Matplotlib is highly flexible; the same output can be produced by many different code snippets (and later by Seaborn or Plotly too).

---

## 5. Flagged for exams / assignments

- **Assessment format (important):** mid-sem and end-sem are **coding-based**. You will *not* hand-write code. You write and **execute** Python, show the outputs, and **submit the code** — as an **IPython/Jupyter notebook (`.ipynb`)** so it can be re-run and evaluated.
- **Homework 1 (set in class):** Given an `errorbar`/line plot whose x-axis runs 0 to 6 — **change the axis limits and the tick labels** so that the axis shows different numbers, or even *words*, instead of 0–6. (i.e. work out how to reset axis levels and tick levels yourself.)
- **Homework 2 (suggested, self-benefit — "we will not check it"):** Reproduce every plot shown today, **but write different code that produces the identical output**. The instructor explicitly framed this as a possible exercise: *"do the same plot… and the output should match but the code is different."* The reverse question was also floated: *given several different code snippets, which produce the same output?*
- **Extension exercise from the subplot discussion:** take a 2×2 grid where the top two plots have the same y-axis and **combine/share that axis** so the two plots sit side by side with one shared y-axis (`sharey`).
- **Next class:** pandas.
- Notes/slides will be uploaded to the **LMS**.