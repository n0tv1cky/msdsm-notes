# DSM-102 — Programming Fundamentals for Data Science
## Session 10 — 2026-09-19 (Instructor: Abhirup Datta)

---

## 1. Overview

This session has two technical halves plus course admin. After settling exam-format and class-project logistics (groups of four, an EDA-style class project, and scheduling extra weekend sessions), the instructor moves into **pandas DataFrames**: how a DataFrame differs from a `dict`/`list` (automatic indexing, labelled columns), how to build one from a dictionary of lists, and how to combine several DataFrames with `pd.merge()` — including merging on a column whose row order differs between tables, merging on a *different* key (`group` instead of `employee`), what happens when a key value is missing (the row silently disappears under the default inner join), and the "row explosion" problem you get when one key maps to several values (multiple skills per group). That last point is left as an open exercise: collapse the exploded table back to **one row per employee with the skills stored as a list**, using `groupby`/aggregation. The second half introduces **user-defined functions with default arguments**, simulating noisy data with NumPy (a downward parabola $y=-x^2$ plus random noise of tunable amplitude), plotting raw noisy data as dots versus the underlying "mean curve" as a line — the conceptual basis of regression/curve fitting — and finally **1-D interpolation with `scipy.interpolate.interp1d`** using the four kinds `'nearest'`, `'linear'`, `'quadratic'`, `'cubic'`, comparing how each reconstructs the trend from noisy points.

> **Reconstruction note:** the instructor typed code live and pasted it into chat; the transcript only captures fragments of it. Code blocks below are best-effort reconstructions from the spoken walkthrough. Places where the exact literal values / syntax had to be inferred are explicitly marked `# INFERRED`.

---

## 2. Course / Admin Announcements

- **Exam scope:** nothing outside the syllabus will be asked. No proctoring, so web/LLM lookup can't be prevented — but "people who know the answer sort it out faster; people who don't burn time googling or burn tokens on Claude."
- Instructor thinks **purely objective (MCQ) questions are not very useful** for this course → expect code-writing / output-matching questions instead (see §6).
- **Class project (mandatory-style deliverable):**
  - Same model as previous years' DSM-102: a **basic EDA (Exploratory Data Analysis)** project on a dataset of your choice, using the tools covered in class.
  - **32 students → 8 groups of 4.** Class representatives (Ashita, Vikat/"Viketti", Harsh) to collect and submit the group list.
  - Discussion of the project starts in the next session.
- **Scheduling:** a one-week gap between classes is too long. Instructor unavailable on the 22nd; available 23rd, 24th, and possibly the 26th. Midterm is on a Saturday; an SM quiz may land somewhere in the midterm weeks. Preference is for **at least one class on the weekend**, because most students are working professionals and need weekend time to actually *type the code themselves*.
- **Advice:** "If you don't do it in a daily manner and you're not at that level, it keeps piling up at the end — that's a big problem."
- Notebooks from this session will be uploaded to the **LMS / Google Classroom**.

---

## 3. Topics in Order Taught

### 3.1 What a DataFrame is (student question, answered mid-class)

- A **DataFrame** is a table-like data structure, conceptually "like a dictionary": **keys become column names**, and the values stored against them become the column data.
- What pandas adds *on top of* a plain dict/list:
  - an automatic **index** (row labels),
  - column **labels**,
  - structured, systematic add/delete/modify operations on large data.
- pandas is built on top of the basic utilities of **NumPy** plus dict/list semantics.
- Lists are the basic building block, but for **large data + systematic manipulation** you are better off with pandas.
- An alternative raised by a student: just load the whole thing from an **Excel/CSV file** — valid, but doesn't answer the "one row per employee" design question.

### 3.2 Creating DataFrames

```python
import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
    'group':    ['Accounting', 'Engineering', 'Engineering', 'HR']
})
df1
```

Displaying `df1` shows the two columns **plus an auto-generated integer index** `0,1,2,3` — the key visual difference from a dict or list.

```python
df2 = pd.DataFrame({
    'employee':  ['Lisa', 'Bob', 'Jake', 'Sue'],   # deliberately re-ordered
    'hire_date': [2004, 2008, 2012, 2014]          # INFERRED values
})
df2
```

Note the **order of employees is shuffled** in `df2` relative to `df1` — this is the whole point of the next step.

### 3.3 Merging two DataFrames — `pd.merge()`

```python
df3 = pd.merge(df1, df2)
df3
```

- `pd.merge(left, right)` with no extra arguments performs a **one-to-one join on the common column(s)** — here `employee`.
- Key observation made in class: even though the rows in `df2` are in a different order, **the merge matches on the *value* of the key, not on position** — Bob's hire date lands next to Bob's group correctly.
- This is how you **join multiple tables** that share a field.

### 3.4 Many-to-one merge on a different key

```python
df4 = pd.DataFrame({
    'group':      ['Accounting', 'Engineering', 'HR'],
    'supervisor': ['Carly', 'Guido', 'Steve']        # INFERRED names
})

df5 = pd.merge(df3, df4)
df5
```

- Here the shared column is `group`, not `employee`. Three groups, three supervisors → each employee row gets the supervisor of its group (**many-to-one merge**).
- Instructor note: in Colab/Jupyter you can hit **Tab** after `pd.` to autocomplete and browse available functions (this is how `merge` and later `drop_duplicates` were spotted).

### 3.5 Adding a column with a missing value — the silent row drop

- Motivating discussion (a digression on data ethics): some fields are **optional / sensitive** — marital status, ethnicity, nationality, salary. In the US and other jurisdictions you legally **cannot ask** such questions pre-employment because they have no bearing on the job. So a real dataset will have **blanks** in those columns.
- A `nationality` column (values like `Indian`, `European`) was added, with one employee's entry **left out entirely**.
- **What went wrong:** after merging, "it removes the third one completely" — the employee with no nationality entry **vanished from the merged result**.
- **Rule / debugging tip:** the default `pd.merge` is an **inner join** — keys present in one table but not the other are dropped. You must still *have a row* for that key, with a blank/`NaN` value:

```python
df7 = pd.DataFrame({
    'employee':    ['Bob', 'Jake', 'Lisa', 'Sue'],
    'nationality': ['Indian', np.nan, 'European', 'Indian']   # INFERRED; blank, not omitted
})
```
  (Or, equivalently, use `how='outer'` / `how='left'` — the instructor's fix in class was "it can be blank.")

### 3.6 The row-explosion problem (the open exercise)

A skills table was added where **one group has several skills**:

```python
df8 = pd.DataFrame({
    'group':  ['Accounting', 'Accounting',
               'Engineering', 'Engineering',
               'HR', 'HR'],
    'skills': ['math', 'spreadsheets',
               'software', 'math',
               'spreadsheets', 'organization']
})

df9 = pd.merge(df7, df8)     # merges on 'group'
df9
```

**Problem observed:** now Bob appears **twice**, Jake twice, Lisa twice, Sue twice — one row per (employee, skill) pair. This is **information redundancy**. From an HR/manager point of view you want **one entry per employee** ("how many employees do we have, who are they, who do they report to").

**Target output (stated explicitly by the instructor):**

| employee | group | hire_date | supervisor | nationality | skills |
|---|---|---|---|---|---|
| Bob | Accounting | 2008 | Carly | Indian | `['math', 'spreadsheets']` |
| Jake | Engineering | … | Guido | … | `['software', 'math']` |
| Lisa | Engineering | … | Guido | … | `['software', 'math']` |
| Sue | HR | … | Steve | … | `['spreadsheets', 'organization']` |

i.e. **single row per employee, with the skills column holding a list/array of that group's skills.**

**Approaches suggested during class (none fully completed live — this is the homework):**
- "Maintain an array in the skills section."
- Use **`groupby`** on the columns that are unique per employee (`employee`, `group`, `hire_date`, `supervisor`, `nationality`) and aggregate `skills` into a joined list.
- Aggregate `df8` **before** merging: collapse `df8` by `group` so each group has one row with a list of skills, *then* merge. (Instructor tried "merge on group after grouping" — same problem recurred until the groupby result was actually **assigned to a variable**.)
- **Common mistake called out explicitly:** `df8.groupby(...)` returns a new object — it does **not** modify `df8` in place. You must assign it: `df9 = df8.groupby(...).agg(...)`. Running the groupby without assignment produced "nothing changes / nothing happened."
- A student spotted **`drop_duplicates`** in the DataFrame method list as another possible tool.

Sketch of the intended solution (**INFERRED — not shown working in class**):

```python
# collapse skills per group into a list, then merge
skills_by_group = df8.groupby('group')['skills'].apply(list).reset_index()
df10 = pd.merge(df7, skills_by_group)   # one row per employee, skills = list
df10
```

> **This is an assigned homework / open exercise.** The instructor said he'd post the answer later if nobody solves it, and offered a "brownie point" for a working solution pasted in the chat.

---

### 3.7 Background check + how the exam will handle it

Before the second half, the instructor checked prerequisites:
- Interpolation, regression, line fitting, curve fitting: **not yet covered** in DSM-101 or by Prof. Surya.
- `scipy`: not used before. Functions (`def`): yes, covered.
- Backgrounds: mostly science/engineering (one from **architecture**, one B.Tech Electrical).

**Consequence for assessment — see §6.**

---

### 3.8 User-defined function with default (keyword) arguments

Code discussed (reconstruction; the `linspace`/noise lines were described verbally):

```python
import numpy as np
import matplotlib.pyplot as plt

def create_data(n, xmax=10, amp_noise=1.5):
    x_data = np.linspace(0, xmax, n)
    y_data = -x_data**2                          # downward-opening parabola
    y_data += amp_noise * np.random.randn(n)     # INFERRED noise term
    return x_data, y_data
```

Points made while walking through it:

- `np.linspace(0, xmax, n)` generates `n` evenly spaced numbers from `0` to `xmax`.
- The curve is $y = -x^{2}$ — a **downward** parabola (the instructor corrected a student who said $y = x^2$: "It's not an upward parabola, it's a downward parabola").
- **`+=` operator:** `y_data += amp_noise` is *exactly equivalent* to `y_data = y_data + amp_noise`. "Plus-equals expresses that addition — it makes life simpler."
- **Default arguments vs. hard-coding (important design lesson):**
  - If you write `xmax = 10` *inside* the function body, the value is **hard-coded** and the function can only ever do one thing.
  - If you write `xmax=10` in the **parameter list**, the caller has a *choice*: pass a value and it is used, omit it and it **defaults to 10**.
  - Benefit: "a part of the code becomes more reusable and can be used multiple times… the more you write, the more chances you make a mistake. The less you write and the more you reuse the same snippet, the fewer bugs/errors you end up with." Also keeps the code compact.
- `return` hands back both arrays as a tuple, unpacked at the call site.

### 3.9 Calling it and plotting: signal vs. noise

```python
x_data, y_data = create_data(n=100, amp_noise=0.5)   # xmax not passed → defaults to 10

plt.plot(x_data, y_data, 'o')          # noisy samples as dots      # INFERRED style string
plt.plot(x_data, -x_data**2, '-')      # underlying 'mean curve'    # INFERRED
plt.show()
```

Experiment run live — **only `amp_noise` was changed**, everything else identical:

| `amp_noise` | Observed result |
|---|---|
| `0.5` | dots hug the parabola tightly; barely any scatter |
| `1.5` | visible scatter about the mean curve |
| `4.5` | large spread; the trend is still there but much noisier |

**Conceptual takeaway (this is the regression idea):**
- The **dots = real-world measured data**; the **continuous line = the mean curve / fitted curve**.
- Sources of noise in real data: **human recording error in surveys, repeated-measurement variation, instrument noise**, etc.
- "Real data is represented by the dots. The fitting of that is this linear/curve fit — that's how you do regression."
- Workflow being simulated: first *generate* noisy data around a known curve, then **throw away the knowledge of the true curve** and try to recover the trend from the dots alone.

### 3.10 Recovering the trend: the question to ask

Given only the scatter of dots:
- Is there a **trend**?
- Can I represent this data by a **straight line**, or do I need a **curved** line?
- We happen to know the truth here is $-x^2$ (curved), but the point is whether the *data alone* forces that conclusion. **Can I rule out a linear fit?**

### 3.11 1-D interpolation with SciPy

```python
from scipy.interpolate import interp1d

x_fine = np.linspace(0, 10, 500)        # dense evaluation grid   # INFERRED size

f_nearest = interp1d(x_data, y_data, kind='nearest')
f_linear  = interp1d(x_data, y_data, kind='linear')
f_quad    = interp1d(x_data, y_data, kind='quadratic')
f_cubic   = interp1d(x_data, y_data, kind='cubic')

y0 = f_nearest(x_fine)
y1 = f_linear(x_fine)
y2 = f_quad(x_fine)
y3 = f_cubic(x_fine)

plt.plot(x_data, y_data, 'o')
plt.plot(x_fine, y0, 'r')      # colour argument comes BEFORE, per instructor
plt.plot(x_fine, y1, 'k')
plt.plot(x_fine, y2, 'y')
plt.plot(x_fine, y3)
plt.show()
```

- **This is interpolation, not extrapolation** — explicitly flagged. `interp1d` only evaluates *within* the range of the input `x` data.
- The four `kind` values demonstrated: **`'nearest'`, `'linear'`, `'quadratic'`, `'cubic'`**.
- **`'nearest'` result:** the curve passes through essentially *every* data point — a staircase that chases the noise. Instructor's verdict: "it is actually **worse**… it goes through all the data points… this is not the right way to plot." → **over-fitting the noise instead of capturing the trend.**
- **`'linear'`:** "not very different" from nearest in this noisy case — still chases points.
- `'quadratic'` and `'cubic'` were plotted together for comparison.
- **Syntax note given while fixing a plot:** the colour/format specification "has to be in the beginning, not the end — that's the syntax." (i.e. the position of the format/colour argument in the `plt.plot(...)` call matters; it goes with the x,y data, not tacked on at the end.) *(Transcript is garbled here; treat the exact form as approximate.)*
- **How to explore new libraries (repeated tip):** search the function name (e.g. `scipy interpolate interp1d`) — the docs pages list all the options, parameters and **scroll down to worked application examples**. "It's very rich, please go ahead and use it accordingly." Also use **Tab-completion** in Colab to see what methods an object exposes.

---

## 4. Reference: every function / keyword / operator introduced

| Item | One-line meaning |
|---|---|
| `import pandas as pd` | Load pandas under the conventional alias `pd`. |
| `import numpy as np` | Load NumPy under the conventional alias `np`. |
| `import matplotlib.pyplot as plt` | Load the plotting module; *required or the plot calls fail*. |
| `pd.DataFrame({...})` | Build a labelled table from a dict: keys → column names, lists → column values. |
| DataFrame **index** | Auto-generated row labels `0..n-1` you get for free; the main add-on over dict/list. |
| `pd.merge(left, right)` | Join two DataFrames on their common column(s); default is an **inner join**, matching by value not position. |
| `df.groupby(col)` | Split rows into groups sharing a key value, for aggregation. **Returns a new object — must be assigned.** |
| `.agg(...)` / `.apply(list)` | Collapse each group to a single row; `apply(list)` gathers the group's values into a Python list. |
| `.reset_index()` | Turn group keys back into ordinary columns after a groupby. |
| `df.drop_duplicates()` | Remove duplicate rows (suggested by a student as an alternative tool). |
| `def name(args):` | Define a function. |
| default/keyword argument `xmax=10` | Gives the parameter a fallback value; caller may override or omit it. |
| `return` | Send value(s) back to the caller; multiple values come back as a tuple. |
| `np.linspace(start, stop, n)` | `n` evenly spaced values from `start` to `stop` inclusive. |
| `**` | Exponentiation operator, e.g. `x_data**2` is $x^2$. |
| `+=` | In-place add: `y += a` $\equiv$ `y = y + a`. |
| `np.random.randn(n)` | `n` standard-normal random numbers (used to build the noise vector). *(INFERRED — the exact noise generator wasn't spoken.)* |
| `plt.plot(x, y, fmt)` | Plot y vs x; `fmt` chooses marker/line style and colour (`'o'`, `'r'`, `'k'`, `'y'`). |
| `plt.show()` | Render the figure. |
| `from scipy.interpolate import interp1d` | Import SciPy's 1-D interpolator. |
| `interp1d(x, y, kind=...)` | Build a callable interpolating function; `kind` ∈ `'nearest'`, `'linear'`, `'quadratic'`, `'cubic'`. |
| `np.nan` | Missing-value placeholder — use this instead of omitting a row, so merges don't silently delete records. |
| Tab-completion in Colab | Press Tab after `pd.` / `df.` to browse available functions and methods. |

---

## 5. Formulas / equations used

- Simulated signal (the "mean curve"):
  $$y = -x^{2}$$
  (downward-opening parabola on $x \in [0, x_{\max}]$, default $x_{\max} = 10$)

- Noisy observed data:
  $$y_{\text{data}} = -x_{\text{data}}^{2} + a_{\text{noise}}\cdot \varepsilon,\qquad \varepsilon \sim \mathcal{N}(0,1)$$
  with $a_{\text{noise}} \in \{0.5,\,1.5,\,4.5\}$ tried in class (`amp_noise`).

- Compound-assignment identity:
  $$\texttt{y\_data += amp\_noise} \;\;\equiv\;\; \texttt{y\_data = y\_data + amp\_noise}$$

- Grid used for evaluation: $x_{\text{fine}} = \text{linspace}(0,\,x_{\max},\,N_{\text{fine}})$, with $N_{\text{fine}} \gg n$ so the interpolant is drawn smoothly.

---

## 6. Flagged for Exams / Assignments

1. **Scope:** only syllabus material. No proctoring, but speed matters — knowing the material beats googling it during the exam.
2. **Question style:** rather than MCQs, expect **"here is the output I want — give me the code"** questions. Verbatim: *"If I give this kind of thing, like I am expecting this kind of an output, you have to give me the answer — will that be okay?"* A student asked for exactly this style of `groupby` question and the instructor agreed.
3. **Interpolation / regression formulas will be GIVEN.** Since interpolation, regression and curve fitting have not been taught in DSM-101 or earlier in this course, and some students are from non-science backgrounds:
   - In the exam, **a code snippet and the relevant formula will be supplied**.
   - You will only be required to make **modifications using basic Python / NumPy / pandas knowledge**.
   - Nothing that "only B.Tech/B.Sc. students would know" will be assumed; any such information will be provided to everyone.
4. **Homework / open exercise (the main takeaway task):** starting from the merged employee + skills table with duplicated employee rows, produce a table with **one row per employee** where `skills` is a **list/array** of that group's skills (e.g. Bob → `['math','spreadsheets']`). Use `groupby` + aggregation (and/or aggregate the skills table *before* merging). Post your solution in the class chat; the answer will be released if nobody gets it.
5. **Class project:** form **8 groups of 4**; deliverable is a **basic EDA** on a dataset of your choice using the tools taught. Group lists to be submitted via the class reps; project briefing next session.
6. **Debugging reminders worth memorising:**
   - `groupby`/`merge`/`drop_duplicates` are **not in-place** — assign the result or "nothing happens."
   - Default `pd.merge` is an **inner join** → an omitted key row **silently disappears**. Insert a blank/`NaN` row instead of leaving the record out.
   - Forgetting `import matplotlib.pyplot as plt` (or the pyplot import generally) → plotting "won't work."
   - Format/colour argument position in `plt.plot()` matters.