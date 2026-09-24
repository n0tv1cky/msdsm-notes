# DSM-103 — Data Structures
## Session Notes — 2026-08-22 (Instructor: Somnath Dey)
### Topic: Two-Dimensional Arrays, Row-/Column-Major Addressing, and Sparse (Triangular & Band) Matrices

---

## 1. Overview

This session moves from one-dimensional arrays (previous lecture: traversal, bubble sort, linear search) to **two-dimensional arrays**. The central theme is the gap between the **logical representation** of a matrix (rows × columns, two subscripts) and its **physical representation** in memory (a linear, contiguous, one-dimensional sequence of cells). The lecture derives the **index formulas** and **address formulas** for both **row-major** and **column-major** storage of a full $m \times n$ array, works them on a $3\times 4$ example, and then generalises the same "count everything stored before this element" technique to **sparse matrices**: triangular matrices (upper/lower, left/right), diagonal matrices, tridiagonal matrices, and $\alpha$–$\beta$ band matrices. For each of these the class derives the number of elements stored per row/column and hence the compressed 1-D index, with the $\alpha$–$\beta$ band matrix requiring a three-case analysis. The session ends with a discussion of why such compaction matters (memory savings vs. $O(1)$ access cost), a homework assignment on two remaining triangular forms, and administrative notes.

---

## 2. Topics Covered (in order taught)

### 2.1 Recap of previous lecture
- Traversal of a one-dimensional array.
- Sorting a 1-D array using **bubble sort**.
- **Searching** an element in a 1-D array.

### 2.2 Two-dimensional arrays — definition
- An array is a collection of **homogeneous** elements. In a 2-D array those elements are organised into **rows and columns**.
- **Two subscripts** are needed to identify an element: $a_{ij}$ means the element in the $i$-th **row** and $j$-th **column**.
- Array dimensions written as $m \times n$: $m$ = number of rows, $n$ = number of columns.
- **Assumption used throughout the lecture:** indices are **1-based**, i.e. $1 \le i \le m$ and $1 \le j \le n$. (The instructor repeatedly stressed this when a student got confused with 0-based indexing.)

### 2.3 Logical vs. physical representation
- **Logical organisation**: how the data structure is conceptually arranged (2-D grid, 2 indices).
- **Physical representation**: how it actually sits in memory. Memory is a **contiguous, linear (1-D) arrangement**, so the 2-D grid must be flattened into a **single index**.
- Therefore we need a **mapping (indexing) formula** from $(i,j)$ to a single linear index, and from there to a memory address.

### 2.4 Two flattening orders — worked on a $3\times 4$ example

Take the $3 \times 4$ matrix ($m=3$, $n=4$):

$$
\begin{bmatrix}
a_{11} & a_{12} & a_{13} & a_{14}\\
a_{21} & a_{22} & a_{23} & a_{24}\\
a_{31} & a_{32} & a_{33} & a_{34}
\end{bmatrix}
$$

**Row-major order** — store the whole first row, then the whole second row, etc. Memory picture (one contiguous strip, left to right):

```
a11 a12 a13 a14 | a21 a22 a23 a24 | a31 a32 a33 a34
 1   2   3   4     5   6   7   8     9  10  11  12
```

**Column-major order** — store the whole first column, then the second column, etc.:

```
a11 a21 a31 | a12 a22 a32 | a13 a23 a33 | a14 a24 a34
 1   2   3     4   5   6     7   8   9    10  11  12
```

### 2.5 Indexing and addressing formulas (full $m \times n$ array, 1-based)

**Row-major.** Before reaching $a_{ij}$ we must store all elements of the first $i-1$ complete rows ($n$ each), plus $j$ elements of row $i$:

$$\text{Index}_{\text{row-major}}(a_{ij}) = (i-1)\cdot n + j$$

$$\text{Address}(a_{ij}) = B + \big[(i-1)\cdot n + (j-1)\big]\cdot w$$

where $B$ = **base address** (address of the first element) and $w$ = **number of words/bytes per element**.

> Logic stated in class: to get the *address* you count the elements stored **before** $a_{ij}$ (i.e. up to $a_{i,j-1}$), multiply by $w$, and add the base address. Equivalently $\text{Address} = B + (\text{Index}-1)\cdot w$.

**Column-major.** Before $a_{ij}$ we store the first $j-1$ complete columns ($m$ each), plus $i$ elements of column $j$:

$$\text{Index}_{\text{col-major}}(a_{ij}) = (j-1)\cdot m + i$$

$$\text{Address}(a_{ij}) = B + \big[(j-1)\cdot m + (i-1)\big]\cdot w$$

**Worked example 1 (row-major), $a_{2,3}$ in the $3\times4$ array:**
$$\text{Index} = (2-1)\times 4 + 3 = 4 + 3 = 7$$
So $a_{23}$ sits at the **7th position**. If $B=100$ and $w=1$ byte: $\text{Address} = 100 + (7-1)\times 1 = 106$.

**Worked example 2 (column-major), $a_{2,3}$ in the same array ($m=3$):**
$$\text{Index} = (3-1)\times 3 + 2 = 6 + 2 = 8$$
So in column-major order $a_{23}$ is the **8th element**. With $w=1$ byte: $\text{Address} = B + (8-1)\times 1 = B + 7$.

### 2.6 Q&A points raised in class
- **Q: Who decides row-major vs column-major — programmer or machine?**
  **A:** In general the system/compiler uses **row-major order** by default. If an application needs column-wise access, you must implement the column-major conversion yourself — i.e. write the routine that converts the 2-D logical array into the single linear array using the corresponding formula before storing.
- The application code still writes `A[i][j]`; **internally** the index formula converts $(i,j)$ into the 1-D index and the location is accessed from there.

### 2.7 Sparse matrices — motivation and taxonomy

- **Definition (working):** a large 2-D array in which the **majority of the elements are zero/null**; only a small number of positions actually carry data.
- **Example given:** a $100 \times 100$ array = 10,000 positions, but only about 500 elements actually present → storing the full 2-D array wastes ~9,500 cells.
- Instead of a plain 2-D array, use a **specialised sparse representation** that stores only the occupied region, plus an index formula that maps $(i,j)$ into that compressed store.

**Classification given in the lecture:**

1. **Triangular matrices** — all data lie on **one side of a diagonal** (either the main diagonal, top-left→bottom-right, or the anti-diagonal, top-right→bottom-left). Four sub-types:
   - **Upper-left triangular** – elements above/on the **anti-diagonal**, filled toward the left (row 1 full, each following row one shorter, hugging the left edge).
   - **Upper-right triangular** – elements on/above the **main diagonal** (row $i$ occupies columns $i \ldots n$; a right-leaning staircase).
   - **Lower-left triangular** – elements on/below the **main diagonal** (row $i$ occupies columns $1 \ldots i$; a left-leaning staircase, row 1 has one element, row $n$ has $n$).
   - **Lower-right triangular** – elements below/on the **anti-diagonal**, hugging the right edge (row 1 has one element at column $n$, row $n$ is full).

2. **Band matrices** — data confined to a band along a diagonal:
   - **Diagonal matrix** – only $i=j$ positions occupied (or only the anti-diagonal; both count as "diagonal matrix").
   - **Tridiagonal matrix** – the diagonal plus **one sub-diagonal and one super-diagonal** (again possible along either diagonal direction).
   - **$\alpha$–$\beta$ band matrix** – the band is $\alpha$ columns wide (counting the diagonal) to one side and $\beta$ rows deep (counting the diagonal) to the other side. Row 1 therefore holds $\alpha$ elements, column 1 holds $\beta$ elements.

### 2.8 Lower-left triangular matrix — index derivation

Structure (1-based, $n \times n$): row 1 has 1 element, row 2 has 2, …, row $i$ has $i$ elements ($a_{ij}$ exists for $j \le i$).

1-D **row-major** layout of a lower-left triangular matrix:

```
a11 | a21 a22 | a31 a32 a33 | a41 ...
 1     2   3     4   5   6     7
```

**Row-major derivation:** elements in the first $i-1$ rows $= 1+2+\cdots+(i-1)$. Using the sum of the first $n$ natural numbers, $1+2+\cdots+n = \dfrac{n(n+1)}{2}$, with $n = i-1$:

$$1+2+\cdots+(i-1) = \frac{(i-1)\,i}{2}$$

Then add $j$ elements from row $i$:

$$\boxed{\;\text{Index}(a_{ij}) = \frac{i(i-1)}{2} + j\;}$$

$$\text{Address}(a_{ij}) = B + \left[\frac{i(i-1)}{2} + j - 1\right]\cdot w$$

**Worked check:** $a_{3,2}$ → $\dfrac{3\cdot 2}{2} + 2 = 3+2 = 5$. Indeed in the layout above $a_{32}$ is the 5th cell. (Note: 5 is the **index**, not the address; the address is $B + (5-1)w$.)

**Column-major derivation (the "tricky" one done at length in class):**
- Column 1 has $n$ elements (0 missing), column 2 has $n-1$ (1 missing), column 3 has $n-2$ (2 missing) … so **column $k$ has $n-k+1$ elements**, i.e. $k-1$ missing.
- Hence **column $j-1$ has $n-j+2$ elements**, i.e. $j-2$ missing. (This was the point of a long clarification: for column $j-1$ the number missing is $(j-1)-1 = j-2$.)
- Elements before column $j$:
$$n + (n-1) + (n-2) + \cdots + \big(n-(j-2)\big) \;=\; n(j-1) - \frac{(j-1)(j-2)}{2}$$
- Inside column $j$, the column starts at row $j$, so $a_{ij}$ is the $(i-j+1)$-th entry.

$$\boxed{\;\text{Index}(a_{ij}) = n(j-1) - \frac{(j-1)(j-2)}{2} + (i-j+1)\;}$$

$$\text{Address}(a_{ij}) = B + \big[\text{Index}(a_{ij}) - 1\big]\cdot w$$

**Verification (3×3 lower-left, column-major order = $a_{11},a_{21},a_{31},a_{22},a_{32},a_{33}$):** $a_{3,2}$ → $3(1) - 0 + (3-2+1) = 3+2 = 5$ ✔ (5th cell).

**Edge-case clarified in class ($j=1$):** substituting $j=1$ gives "columns before column 1" $=0$, so no elements are counted from the summation term and the index reduces to $i$. A $j=0$ column does not exist — if you ever derive $j=0$ it simply means "out of range / nothing to count", not an error in the formula.

### 2.9 Upper (right) triangular matrix

Structure: row $i$ occupies columns $i \ldots n$, so **row $i$ has $n-i+1$ elements**; **column $j$ has $j$ elements**. This is the mirror image of the lower-left case with the roles of $i$ and $j$ interchanged.

**Column-major** (columns have $1,2,3,\ldots$ elements — same pattern as rows in the lower-left case):

$$\text{Index}(a_{ij}) = \frac{j(j-1)}{2} + i$$

**Row-major** (rows have $n, n-1, n-2, \ldots$ elements — same pattern as columns in the lower-left case):

$$\text{Index}(a_{ij}) = n(i-1) - \frac{(i-1)(i-2)}{2} + (j-i+1)$$

$$\text{Address} = B + \big[\text{Index}-1\big]\cdot w$$

> Principle stated by the instructor: *"index will be changed with respect to this formula — $i$ will be $j$, $j$ will be $i$."* Once you know the per-row / per-column occupancy pattern, the same counting argument produces the formula.

### 2.10 Diagonal matrix

- Only positions with $i = j$ are stored. Each row (and each column) contributes **exactly one** element.
- $$\text{Index}(a_{ii}) = i \quad (\text{equivalently } = j)$$
- $$\text{Address} = B + (i-1)\cdot w$$
- **Row-major and column-major give the same result** for a diagonal matrix.

### 2.11 Tridiagonal matrix

- Row 1 has **2** elements, rows $2 \ldots n-1$ have **3** elements each, row $n$ has **2**. (Same pattern column-wise: first and last columns have 2, others 3.)
- **Row-major derivation:** elements in the first $i-1$ rows $= 2 + \underbrace{3+3+\cdots+3}_{(i-2)\text{ terms}} = 2 + 3(i-2)$.
  Row $i$ starts at column $i-1$, so within row $i$ the element $a_{ij}$ is the $\big(j-(i-2)\big)$-th entry.
- $$\text{Index}(a_{ij}) = \big[2 + 3(i-2)\big] + \big(j - (i-2)\big) \;=\; 2i + j - 2$$
- **Column-major:** swap the roles of $i$ and $j$:
  $$\text{Index}(a_{ij}) = 2j + i - 2$$
- $$\text{Address} = B + \big[\text{Index}-1\big]\cdot w$$

*Quick check (row-major):* $a_{11}\to 1$, $a_{12}\to 2$, $a_{21}\to 3$, $a_{22}\to 4$, $a_{23}\to 5$ ✔.

### 2.12 $\alpha$–$\beta$ band matrix — three-case index derivation

**Shape:** row 1 holds $\alpha$ elements (columns $1 \ldots \alpha$); the band then slides down-right. Row $i$ holds columns $\max(1,\,i-\beta+1)$ through $\min(n,\,i+\alpha-1)$. Three regions:

1. **Rows $1$ to $\beta$**: the band's left edge is still pinned at column 1, so the row length **grows by 1 each row** — row $k$ has $\alpha + k - 1$ elements.
2. **Rows $\beta+1$ to $n-\alpha+1$**: full band width, **constant** $\alpha + \beta - 1$ elements per row.
3. **Rows $n-\alpha+2$ to $n$**: the right edge has hit column $n$, so the row length **shrinks by 1 each row**.

Within any row of region 2 or 3 the row starts at column $i-\beta+1$, so $a_{ij}$ is the $(j-i+\beta)$-th element of that row.

**Case 1: $1 \le i \le \beta$**
$$\text{Index}(a_{ij}) = \sum_{k=1}^{i-1}\big(\alpha + k - 1\big) + j \;=\; (i-1)\alpha + \frac{(i-1)(i-2)}{2} + j$$

**Case 2: $\beta < i \le n-\alpha+1$**
$$\text{Index}(a_{ij}) = \underbrace{\left[\beta\alpha + \frac{\beta(\beta-1)}{2}\right]}_{\text{rows }1..\beta} \;+\; \underbrace{(i-\beta-1)(\alpha+\beta-1)}_{\text{rows }\beta+1..i-1} \;+\; \underbrace{(j-i+\beta)}_{\text{inside row }i}$$

> The row-count term was derived explicitly in class: the number of rows from $\beta+1$ to $i-1$ is
> $$(i-1) - (\beta+1) + 1 = i-\beta-1$$
> using the rule **"last index − first index + 1"** (illustrated with: rows 5 to 10 contain $10-5+1 = 6$ rows).

**Case 3: $n-\alpha+1 < i \le n$** — same idea, one more block:
$$\text{Index}(a_{ij}) = \underbrace{\left[\beta\alpha + \frac{\beta(\beta-1)}{2}\right]}_{\text{rows }1..\beta} + \underbrace{(n-\alpha+1-\beta)(\alpha+\beta-1)}_{\text{rows }\beta+1..\,n-\alpha+1} + \underbrace{\sum_{k=n-\alpha+2}^{i-1}\big(n-k+\beta\big)}_{\text{shrinking rows}} + \underbrace{(j-i+\beta)}_{\text{inside row }i}$$

(The instructor sketched this last case as "first compute rows 1 to $\beta$, then $\beta+1$ to $n-\alpha+1$, then $n-\alpha+2$ to $i-1$, then position within row $i$" and left the algebraic simplification to the students.)

**Numerical example posed in class:** $n = 15$ (a $15\times15$ band matrix), $\alpha = 3$, $\beta = 4$; find the index of $a_{10,11}$.
- Check the case: $\beta = 4 < i = 10 \le n-\alpha+1 = 13$ → **Case 2**.
- Rows 1–4: $\beta\alpha + \frac{\beta(\beta-1)}{2} = 4\cdot 3 + \frac{4\cdot3}{2} = 12 + 6 = 18$.
- Rows 5–9: $(i-\beta-1)(\alpha+\beta-1) = (10-4-1)(3+4-1) = 5 \times 6 = 30$.
- Inside row 10: $j-i+\beta = 11-10+4 = 5$.
- $\text{Index} = 18 + 30 + 5 = 53$; $\text{Address} = B + (53-1)\cdot w$.

### 2.13 Why bother? (cost/benefit discussion)

- **Memory saving:** for a $10{,}000 \times 10{,}000$ array with data only in a narrow band, storing the full array at 8 bytes/element costs $10^8 \times 8$ bytes; with $\alpha = \beta = 10$ the band store is dramatically smaller (roughly (number of band elements) $\times 8$).
- **Access cost:** the index formula is just **one multiplication plus additions**, so converting $(i,j)$ to a location is **$O(1)$ time**. You pay essentially nothing for the compression.
- **When you see this:** data distributed along a particular direction/diagonal — e.g. matrices arising in PCA and other data-analysis workloads.
- **Historical remark:** these optimisations mattered when machines had 512 MB of RAM (or less) and ~20 GB hard disks; today desktops used for data analysis commonly have 16 GB+ of RAM, so this kind of hand optimisation is less commonly applied.

---

## 3. Algorithm / Procedure Summaries

**Mapping a 2-D logical array to 1-D physical memory (general recipe used for every case above):**

1. Identify the **storage order** (row-major or column-major) and the **occupancy pattern** (how many stored elements each row/column contains).
2. Count all stored elements in the **complete rows (or columns) before** the one containing $a_{ij}$.
3. Add the **offset of $a_{ij}$ within its own row (or column)** (= position counted from the first *stored* element of that row/column, not from column 1).
4. That sum is the **1-D index** (1-based).
5. Convert to an address:
 $$\text{Address}(a_{ij}) = B + \big(\text{Index}(a_{ij}) - 1\big)\times w$$
 where $B$ = base address, $w$ = bytes/words per element.
6. Complexity: **$O(1)$ time, $O(1)$ extra space** per access.

---

## 4. Formula Sheet (all 1-based indexing, $B$ = base address, $w$ = size per element)

| Matrix type | Order | Index of $a_{ij}$ |
|---|---|---|
| Full $m\times n$ | Row-major | $(i-1)n + j$ |
| Full $m\times n$ | Column-major | $(j-1)m + i$ |
| Lower-left triangular $n\times n$ | Row-major | $\dfrac{i(i-1)}{2} + j$ |
| Lower-left triangular $n\times n$ | Column-major | $n(j-1) - \dfrac{(j-1)(j-2)}{2} + (i-j+1)$ |
| Upper-right triangular $n\times n$ | Row-major | $n(i-1) - \dfrac{(i-1)(i-2)}{2} + (j-i+1)$ |
| Upper-right triangular $n\times n$ | Column-major | $\dfrac{j(j-1)}{2} + i$ |
| Diagonal | Either | $i$ (= $j$) |
| Tridiagonal | Row-major | $2i + j - 2$ |
| Tridiagonal | Column-major | $2j + i - 2$ |
| $\alpha$–$\beta$ band, Case 1 ($i \le \beta$) | Row-major | $(i-1)\alpha + \dfrac{(i-1)(i-2)}{2} + j$ |
| $\alpha$–$\beta$ band, Case 2 ($\beta < i \le n-\alpha+1$) | Row-major | $\beta\alpha + \dfrac{\beta(\beta-1)}{2} + (i-\beta-1)(\alpha+\beta-1) + (j-i+\beta)$ |
| $\alpha$–$\beta$ band, Case 3 ($i > n-\alpha+1$) | Row-major | Case-2 prefix $+ \displaystyle\sum_{k=n-\alpha+2}^{i-1}(n-k+\beta) + (j-i+\beta)$ |

**In all cases:** $\text{Address}(a_{ij}) = B + \big(\text{Index}-1\big)\cdot w$.

**Supporting identities used:**
$$1+2+\cdots+n = \frac{n(n+1)}{2}$$
$$\text{number of rows from } p \text{ to } q = q - p + 1$$

---

## 5. Homework / Exam-Relevant Items

- **Homework (explicitly assigned):** derive the **row-major and column-major index (and address) formulas** for
 1. the **lower-right triangular matrix** (row 1 has one element at column $n$, row $n$ is full), and
 2. the **upper-left triangular matrix** — the one written on the board as
 $a_{11}\,a_{12}\,\ldots\,a_{1n}$ / $a_{21}\,a_{22}\,\ldots\,a_{2,n-1}$ / … / $a_{n1}$.
- **"You must practice this $\alpha$–$\beta$ band matrix"** — the instructor singled out the $\alpha$–$\beta$ band derivation (and warned that $\alpha$ and $\beta$ are *different* parameters, so don't collapse them) as the thing to drill.
- Be able to state clearly the difference between **index** (position number in the 1-D store) and **address** (index converted using $B$ and $w$) — this distinction was repeatedly corrected in class.
- Know the **1-based indexing assumption** and how the formulas behave at edges (e.g. $j = 1 \Rightarrow$ zero preceding columns, index reduces to $i$).

---

## 6. Administrative Notes

- The next scheduled lecture (**Thursday**) is likely to be **cancelled** due to the instructor's travel; confirmation to be sent **by Tuesday**. Thursday and Saturday sessions were both mentioned as potentially affected.