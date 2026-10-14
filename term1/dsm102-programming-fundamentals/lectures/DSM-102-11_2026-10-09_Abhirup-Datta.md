---
course: DSM 102
date: 2026-10-09
start: 7:00pm
session: "11"
faculty: Abhirup Datta
---

# DSM-102 Lecture 11: Visualizing Data with Seaborn
*Session: DSM-102-11, 2026-10-09, Abhirup Datta*

---

## 1. Overview

This session introduced **Seaborn**, a Python plotting library built on top of Matplotlib. It covered no new math or statistics. The goal was to go from a pandas table plus one line of code to an informative plot. The instructor argued that Seaborn removes the tedium of Matplotlib: you refer to columns of a pandas DataFrame **by name**, and Seaborn handles labels, colors, and legends automatically. It also quietly computes some statistics itself, such as means, medians, standard deviations, and confidence intervals.

Using Seaborn's built-in **penguins** dataset, the lecture walked through **eight plot types**:

1. scatter plot
2. histogram (with KDE)
3. bar plot
4. box plot
5. violin plot
6. FacetGrid
7. pair plot
8. heatmap

For each plot the instructor covered three things: what question it answers, how to read it, and what it reveals about the penguins.

**Key habit:** before plotting anything, ask what question you are asking of the data. Once you know the question, the choice of plot is nearly automatic.

---

## 2. Topics Covered (in order)

### 2.1 Why Seaborn instead of raw Matplotlib
- Seaborn sits on top of Matplotlib. Matplotlib still does the actual drawing.
- Seaborn understands **pandas DataFrames directly**: you pass column names, and it works out axis labels, colors, and legends.
- In Matplotlib you would set colors, styles, legends, and axis labels by hand for each group.
- Seaborn does some statistics on its own (mean, median, standard deviation, confidence intervals). **You should know what it computed**, so you can explain your plot if someone asks (e.g., in a report).
- Trivia (not required): the alias `sns` comes from *Samuel Norman Seaborn*, a character in the TV show *The West Wing*.

### 2.2 Loading the data
- Seaborn ships with small practice datasets. The lecture used `penguins`: researchers measured penguins on three islands near Antarctica and then released them.
- **Tidy data shape**, which Seaborn expects:
  - one **row per observation** (one penguin);
  - one **column per variable** (species, island, bill length, etc.).
- If your own data isn't in this shape, reshape it with pandas first, then plot.

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = sns.load_dataset("penguins")   # spoken: "sns dot load data set penguin"
data.head()      # instructor showed the first 5 rows ("column number five", likely head())
data.shape       # (344, 7) -> 344 rows, 7 columns
data.isna().sum()  # count missing values per column (spoken: "is n a")
```
*Inferred: the exact call used to show "five" rows is assumed to be `head()`. The missing-value check is assumed to be `isna().sum()`.*

- Columns: `species`, `island`, `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`, `sex`.
- **NaN** is how pandas marks a **missing value**. Some penguins have a row but no measurements.
- ⚠️ **Seaborn silently skips rows with NaN and does not warn you.** Keep this in mind when interpreting counts.

### 2.3 Theme and figure settings
This cell doesn't draw anything. It changes how all later plots look:
- a gray background with white grid lines (the `"darkgrid"` style);
- figure DPI = 300, which is sharp enough to print;
- figure size = $6 \times 3$ inches (6 in wide, 3 in tall).

```python
sns.set_theme(style="darkgrid",
              rc={"figure.dpi": 300, "figure.figsize": (6, 3)})
```
*Inferred: the instructor described the effects but not the exact syntax. It could equally have been done via `plt.rcParams[...]`.*

---

### 2.4 Plot 1: Scatter plot (`sns.scatterplot`)
- **Question it answers:** how do two numeric variables relate?
- **How to read it:** one dot per observation (penguin). The horizontal position is one variable and the vertical position is the other.

```python
sns.scatterplot(x="bill_length_mm", y="bill_depth_mm",
                data=data, hue="species");
```
- `hue="species"` colors points by category and adds a legend automatically.
- **What it showed:**
  - Blue is Adelie, orange is Chinstrap, green is Gentoo.
  - **Within each species**, longer bills go with deeper bills (a positive relationship).
  - **When all three are mixed together**, the overall trend appears to point the *other* way. The reason is that the three species sit in different places on the plot:
    - Adelie has short, deep bills (top-left).
    - Gentoo has long, shallow bills (bottom-right).
  - We can only see this because of the `hue` argument. *(Aside, not named in lecture: a reversal like this is often called Simpson's paradox.)*
- **Tip: the trailing semicolon `;`.** Without it, Jupyter prints a text line above the plot (the returned Axes object, e.g. `<Axes: xlabel=..., ylabel=...>`). Adding `;` at the end of the line suppresses it.

**Styled version** (encoding more columns):
```python
sns.scatterplot(x="bill_length_mm", y="bill_depth_mm", data=data,
                hue="species",        # color  = species
                style="sex",          # marker = sex (crosses vs circles)
                size="body_mass_g",   # dot size = body mass
                sizes=(10, 180),      # min/max marker size
                alpha=0.6);           # transparency to reveal overlapping points
```
*Inferred: the transcript says sizes "10 to 18", so the upper bound may be 18 or 180. The exact `alpha` value was not stated; 0.6 is a placeholder.*

---

### 2.5 Plot 2: Histogram (`sns.histplot`) and KDE
- **Question it answers:** for a single numeric column, what values does it take, what is typical, how spread out is it, and are there strange values?
- **Definition:** a histogram shows the distribution of one numeric variable.
  - Take the whole range and cut it into equal slices called **bins**.
  - Count how many observations fall in each bin.
  - **Bar height = count**, nothing more.

```python
sns.histplot(x="flipper_length_mm", data=data);   # bins="auto" by default
```
- Only two arguments are needed: `x` (the column) and `data` (the table). There is no `y`.
- **What it showed:**
  - Flipper length ranges from about **170 mm to about 230 mm**.
  - There are **two hills**: a taller one around **190 mm** and a lower one around **215 mm**, with a dip between them.
  - **Two hills usually mean two different groups mixed in one column.** The instructor asked the class to guess the groups; the hue plot below answered it (species).

**Horizontal version:** pass `y=` instead of `x=`. It is the same information drawn on its side.
```python
sns.histplot(y="flipper_length_mm", data=data);
```

**Bin width:**
```python
sns.histplot(x="flipper_length_mm", data=data, binwidth=3);  # every bin exactly 3 mm wide
```
- Narrower bins show more detail but also more noise.
- Wider bins look smoother but can hide features.
- No bin width is "correct." **Advice: try two or three bin widths and trust only the features that survive all of them.**

**KDE (Kernel Density Estimate):**
```python
sns.histplot(x="flipper_length_mm", data=data, kde=True);
```
- A KDE is a smooth curve estimating the shape of the distribution. It is built by placing a small bump on every observation and adding all the bumps together.
- The standard formula (not written in lecture) is:
  $$\hat f(x) = \frac{1}{nh}\sum_{i=1}^{n} K\!\left(\frac{x - x_i}{h}\right)$$
  Here $K$ is the bump shape (kernel) and $h$ is the bandwidth.
- Advantage: the curve doesn't depend on where the bin edges fall.
- Caveat: **the KDE is an estimate (a smooth guess). The bars are the actual counts.**

**Histogram by group:**
```python
sns.histplot(x="flipper_length_mm", data=data, hue="species");
sns.histplot(x="flipper_length_mm", data=data, hue="species", alpha=0.5);  # alpha value inferred
```
- This answers the two-hills question:
  - The left hill is **Adelie (blue) and Chinstrap (orange)**, which overlap heavily.
  - The right hill is **Gentoo (green)**.
- Problem: the overlapping histograms are drawn on top of each other and look muddy. Fix it by changing `alpha` or `multiple`.

**Other variations shown** (exact combinations partly inferred):
```python
sns.histplot(x="flipper_length_mm", data=data, hue="species", multiple="stack");
sns.histplot(x="flipper_length_mm", data=data, hue="species", stat="density");
sns.histplot(x="flipper_length_mm", data=data, hue="species", element="step");  # outline instead of bars
```

---

### 2.6 Plot 3: Bar plot (`sns.barplot`)
- **Question it answers:** we know the species differ in flipper length, but by how much? Use a bar plot when comparing **one summary number across groups**.
- **Definition:** a bar plot compares a summary statistic of a numeric variable across categories.

```python
sns.barplot(x="species", y="flipper_length_mm", data=data);
```
- ⚠️ **Key difference from a histogram:**
  - In a histogram, bar height is a **count**.
  - In a Seaborn bar plot, bar height is the **mean** by default.
- **Results:**
  - Adelie: about 190 mm (the instructor said "180 to 190").
  - Chinstrap: close to 200 mm.
  - Gentoo: above 200 mm.
- **To actually count rows, use a separate function:** `sns.countplot`.
- **Error bars:** the small black lines on the bars show, by default, a **95% confidence interval** around the mean.
  - Seaborn computes the mean and the CI itself without asking you. **You must know this so you can explain the plot.**
  - The interval can be changed.

```python
sns.countplot(x="species", data=data);   # bar height = number of rows

# median instead of mean, standard deviation instead of CI:
sns.barplot(x="species", y="flipper_length_mm", data=data,
            estimator="median", errorbar="sd");

# split each species by sex:
sns.barplot(x="species", y="flipper_length_mm", data=data, hue="sex");
```
*Inferred: exact `estimator`/`errorbar` syntax. The instructor said "median and standard deviation" verbally. A different CI level would be written `errorbar=("ci", 90)`.*

- With `hue="sex"`, Seaborn picks colors and adds labels and a legend automatically. In Matplotlib you would set each of these by hand.

---

### 2.7 Plot 4: Box plot (`sns.boxplot`)
- **Question it answers:** how do several groups' distributions compare side by side?
- **Definition:** a box plot summarizes a distribution using **five numbers**: min, $Q_1$, median, $Q_3$, max. The whiskers typically extend to $1.5 \times \text{IQR}$, where $\text{IQR} = Q_3 - Q_1$, and points beyond them are drawn as outliers.
- The code is the same as the bar plot; just swap the function name.

```python
sns.boxplot(x="species", y="flipper_length_mm", data=data);
sns.boxplot(x="species", y="flipper_length_mm", data=data, hue="sex");
```
- ⚠️ **Correction:** the instructor described the box as showing the "mean (~190) and standard deviation." A standard box plot actually shows the **median** (center line) and the **interquartile range** (box). Use the five-number definition above.
- Bar and box plots were also shown side by side in subplots. The exact code was not spoken; a likely version is:

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
sns.barplot(x="species", y="flipper_length_mm", data=data, ax=axes[0])
sns.boxplot(x="species", y="flipper_length_mm", data=data, ax=axes[1]);
```

---

### 2.8 Plot 5: Violin plot (`sns.violinplot`)
- **Weakness of box plots:** they boil each group down to five numbers. A two-hill (bimodal) distribution would look like an ordinary box, and the two hills would vanish.
- **A violin plot combines the summary and the shape.** Take the KDE curve, stand it up vertically, and mirror it left and right. The mirroring adds no information; it just makes the shape easier to see.

```python
sns.violinplot(x="species", y="flipper_length_mm", data=data);
sns.violinplot(x="species", y="flipper_length_mm", data=data, hue="sex");
sns.violinplot(x="species", y="flipper_length_mm", data=data, hue="sex", split=True);
```
*The spoken "8 equal to true" is reconstructed as `split=True`.*

- **How to read it:**
  - Where the violin is **fat**, many penguins have that flipper length; where it is thin, few do. For example, Adelie is fattest around 190 mm.
  - Inside each violin there is a mini box plot:
    - white marker = **median**;
    - thick dark bar = **box** (middle 50%);
    - thin line = **whiskers**.
  - Nothing from the box plot is lost.
- `split=True` (with `hue="sex"`) draws half violins back to back, female on one side and male on the other. This saves space and makes comparison easier.

---

### 2.9 Plot 6: FacetGrid (`sns.FacetGrid`)
- **Problem:** so far each plot has been a single picture, with groups squeezed in using color. Color works for two or three groups. Suppose we want flipper length by island **and** by sex at once: 3 islands × 2 sexes = 6 combinations. Six overlapping histograms in one plot would be a mess.
- **Definition:** FacetGrid produces a grid of small plots, one for each subset of the data.

```python
g = sns.FacetGrid(data, col="island", row="sex")   # 3 columns x 2 rows of empty panels
g.map(sns.histplot, "flipper_length_mm");          # spoken: "drawing dot map"
```
- Creating the grid alone shows **empty boxes** (3 columns × 2 rows). Calling `.map(...)` fills each panel with the chosen plot.
- Variations shown (syntax partly inferred):

```python
g = sns.FacetGrid(data, col="island", row="sex", hue="species")
g.map(sns.histplot, "flipper_length_mm", kde=True)       # add smooth curve
g.map(sns.kdeplot, "flipper_length_mm")                  # KDE only
g.map(sns.histplot, "flipper_length_mm", element="step") # step style
```

---

### 2.10 Plot 7: Pair plot (`sns.pairplot`)
- **Question it answers:** someone hands you a new dataset. What are all the relationships at once?
- **Definition:** a pair plot shows the relationship between every pair of numeric columns in a single figure.

```python
sns.pairplot(data, hue="species");                   # diagonal = KDE (default with hue)
sns.pairplot(data, hue="species", diag_kind="hist"); # diagonal = histograms
sns.pairplot(data, hue="species", kind="reg");       # off-diagonal scatter + fitted line
```
*Inferred: the instructor said "heights" (likely mishearing `hue`) and showed a version with lines and shaded regions; `kind="reg"` is the probable call.*

- **Layout:** variables are `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`.
  - **Off-diagonal panels** are scatter plots of each pair.
  - **Diagonal panels** would pair a variable with itself, which gives a useless straight line. Instead, Seaborn draws each variable's distribution there: a KDE by default with `hue`, or a histogram with `diag_kind="hist"`.
- **Line and shaded band:** the instructor described these as "mean" and "sigma/variance." In Seaborn's `kind="reg"`, the line is a **fitted linear regression** and the shaded band is its **95% confidence interval**.

---

### 2.11 Plot 8: Heatmap (`sns.heatmap`) of correlations
- **Question it answers:** the pair plot shows relationships as pictures. How strongly are two columns related, **as a number**?
- **The correlation coefficient** ranges from $-1$ to $+1$:
  - $r = +1$ (close to): strong positive correlation;
  - $r = -1$ (close to): strong negative (anti-)correlation;
  - $r = 0$: no (linear) correlation.
- The Pearson formula (not written in lecture; pandas computes it) is:
  $$r_{xy} = \frac{\sum_{i}(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum_{i}(x_i-\bar{x})^2}\,\sqrt{\sum_{i}(y_i-\bar{y})^2}}, \qquad -1 \le r_{xy} \le 1$$
- **Pandas does the statistics; Seaborn just draws the matrix.**

```python
import numpy as np

corr = data.corr(numeric_only=True)        # correlation matrix of numeric columns
sns.heatmap(corr, annot=True);             # spoken "n not equal to two" -> annot=True: print values in cells

mask = np.triu(np.ones_like(corr, dtype=bool))   # hide upper triangle (it mirrors the lower)
sns.heatmap(corr, mask=mask, annot=True);
```
*Inferred: the exact correlation call, the masking code, and any colormap arguments.*

- **What it showed:**
  - The diagonal is always $1$, since each variable is perfectly correlated with itself.
  - Some pairs are strongly positive and some are negative (anti-correlated).
  - No pair had a correlation of exactly zero.
- The masked version hides the upper triangle and shows only the lower one, because the matrix is symmetric.

---

## 3. Functions, Keywords, and Parameters Introduced

| Item | Meaning |
|---|---|
| `import seaborn as sns` | Import Seaborn with its conventional alias |
| `sns.load_dataset("penguins")` | Load a built-in practice dataset as a pandas DataFrame |
| `df.head()` | Show the first 5 rows |
| `df.shape` | (rows, columns) tuple; here $(344, 7)$ |
| `df.isna()` / `.sum()` | Flag missing (NaN) values / count them per column |
| `NaN` | pandas' marker for a missing value |
| `sns.set_theme(style=..., rc=...)` | Set global style (e.g. `"darkgrid"`), DPI, figure size |
| `sns.scatterplot` | One dot per observation; relationship of two numeric variables |
| `sns.histplot` | Distribution of one numeric variable via binned counts |
| `sns.countplot` | Bar height = number of rows per category |
| `sns.barplot` | Bar height = summary statistic (default **mean**) per category, with error bars |
| `sns.boxplot` | Five-number summary per group |
| `sns.violinplot` | Mirrored KDE plus a mini box plot per group |
| `sns.kdeplot` | Standalone kernel density curve |
| `sns.FacetGrid(data, col=, row=)` | Grid of small plots, one per data subset |
| `g.map(func, "col")` | Draw a plot function in every FacetGrid panel |
| `sns.pairplot` | All pairwise numeric relationships in one figure |
| `sns.heatmap` | Color-coded matrix (used for correlations) |
| `df.corr()` | Pandas correlation matrix |
| `np.triu`, `np.ones_like` | Build an upper-triangle mask for the heatmap |
| `plt.subplots` | Create multiple axes to place plots side by side |
| `x=`, `y=` | Column names for the axes (x vs y also flips orientation in `histplot`) |
| `data=` | The DataFrame to plot from |
| `hue=` | Color by a categorical column (auto legend) |
| `style=` | Marker shape by a column |
| `size=`, `sizes=(min, max)` | Marker size by a numeric column, and its range |
| `alpha=` | Transparency, $0$ (invisible) to $1$ (opaque); reveals overlaps |
| `bins="auto"` / `binwidth=` | Automatic binning / fixed bin width (e.g. 3 mm) |
| `kde=True` | Overlay a KDE curve on a histogram |
| `multiple="stack"` | Stack group histograms instead of overlapping them |
| `stat="density"` | Normalize histogram to density instead of counts |
| `element="step"` | Draw histogram as an outline instead of bars |
| `estimator=` | Summary statistic for `barplot` (e.g. `"median"`) |
| `errorbar=` | Error bar type: 95% CI by default, `"sd"`, `("ci", level)` |
| `split=True` | Half violins per `hue` level, back to back |
| `diag_kind=` | Pair plot diagonal type (`"kde"` or `"hist"`) |
| `kind="reg"` | Pair plot off-diagonals with a regression line and CI band |
| `annot=True` | Print numeric values inside heatmap cells |
| `mask=` | Hide heatmap cells (e.g. upper triangle) |
| trailing `;` | Suppress Jupyter's text echo of the returned Axes object |

---

## 4. Syntax Rules, Common Mistakes, and Tips

- **Tidy data first:** one row per observation and one column per variable. Reshape with pandas if needed.
- **Silent NaN dropping:** Seaborn skips missing rows without warning. Check `data.isna().sum()`.
- **Trailing semicolon** removes the printed `<Axes ...>` line above plots.
- **Bar plot ≠ histogram:**
  - `barplot` heights are **means**;
  - `histplot` heights are **counts**;
  - use `countplot` to count rows.
- **Know what Seaborn computed:** bar plot error bars are 95% CIs by default. Be ready to explain them if you put a plot in a report.
- **Bin width:** try two or three values and trust only features that persist across all of them.
- **KDE is a smooth estimate.** Histogram bars are the real counts.
- **Overlapping `hue` histograms look muddy.** Use `alpha`, `multiple="stack"`, or `element="step"`.
- **Box plots hide multimodality.** Use a violin plot or histogram to check the shape.
- **Too many groups for color:** use `FacetGrid` (small multiples).
- **Mixed groups can reverse trends:** always try `hue=` with a categorical variable. The bill length vs. depth example showed a positive trend within species but the opposite trend when pooled.

---

## 5. Flagged as Important

- **Memorize the eight functions:** `scatterplot`, `histplot`, `barplot`, `boxplot`, `violinplot`, `FacetGrid`, `pairplot`, `heatmap` (plus `countplot` and `kdeplot` as related extras).
- **The habit to take away:** before plotting, ask *what question am I asking of the data?* Each plot answers one kind of question:

| Question | Plot |
|---|---|
| How do two numbers relate? | scatter plot |
| What does one number's distribution look like? | histogram / KDE |
| How does a summary number compare across groups? | bar plot |
| How many rows are in each category? | count plot |
| How do distributions compare across groups? | box plot / violin plot |
| How does a distribution vary across many subsets? | FacetGrid |
| What are all the pairwise relationships? | pair plot |
| What is the numeric strength of each relationship? | correlation heatmap |

- For every plot, be able to state **what question it answers, how to read it, and what it says about the data.**
- No specific exam or assignment was announced in this session.