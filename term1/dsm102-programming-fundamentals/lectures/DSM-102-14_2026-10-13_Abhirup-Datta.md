---
course: DSM 102
date: 2026-10-13
start: 7:00pm
session: "14"
faculty: Abhirup Datta
---

# DSM-102 Lecture 14: Linear Algebra with NumPy (Vectors, Matrices, Transformations, Least Squares)

**Instructor:** Abhirup Datta  **Date:** 2026-10-13

---

## 1. Overview

The session opened with a Q&A about how to read Python/Jupyter help pop-ups for plotting functions, specifically what can go inside `*args` and `**kwargs`. The main lecture was an introduction to linear algebra for data science, implemented in NumPy. It began with scalars, vectors, matrices and tensors, then covered vector addition and scalar multiplication, a "houses × features" data matrix, the dot product and the angle between vectors, norms (L2 and L1) and the distance between vectors, and linear independence via matrix rank. It then moved to matrix operations: addition, scalar multiplication, matrix multiplication (and why order matters), and linear transformations (scaling, rotation, shear) visualised on a grid. After that came the determinant as an area-scaling factor, transpose and inverse, solving a linear system with `np.linalg.solve`, and eigenvalues and eigenvectors with `np.linalg.eig`. The session closed with least-squares fitting of a straight line, derived with calculus and compared with seaborn's `regplot`.

---

## 2. Topics in the Order Taught

### 2.0 Opening Q&A: reading `*args` / `**kwargs` in help pop-ups

**The student's question.** In the help text for a plotting function (e.g. a histplot or bar plot), the signature ends with `*args, **kwargs`. How do you know which extra arguments are allowed there? For example, `linestyle=` may be accepted, but `legend=` in a bar plot may raise an error, so the legend has to be added separately.

**The instructor's answer.**
- There is **no thumb rule**.
- Look at the help or pop-up text using `help(func)`, `func?` in Jupyter, or hovering in VS Code/Jupyter.
- Otherwise, Google the function's documentation.
- Keyword arguments are key–value pairs. You can build them first and pass them into the plot call.
- The student indicated the question was not fully answered, and it was deferred to offline discussion.

**Supplementary clarification (not stated in lecture, added for completeness).**
- `*args` collects extra positional arguments into a tuple.
- `**kwargs` collects extra `key=value` arguments into a dict.
- In plotting libraries, the docstring usually says where `**kwargs` are **forwarded**. For example, seaborn functions often pass them to an underlying matplotlib function, and `plt.bar` passes them to the `Rectangle` patch properties.
- The valid extra keywords are therefore the parameters of that downstream function. Follow the "passed to …" link in the docs.
- This is why `label=` works inside `plt.bar(...)` but the legend itself is drawn with a separate `plt.legend()` call.

```python
# Building kwargs first, then unpacking them into a call (illustrative)
style = {"color": "steelblue", "edgecolor": "black", "alpha": 0.7}
plt.bar(x, heights, label="sales", **style)   # extra keys go to the bar patches
plt.legend()                                    # legend added separately
```

---

### 2.1 Why linear algebra in data science

- Datasets are naturally stored as matrices:
  - **Rows** are observations (samples).
  - **Columns** are features.
- Linear algebra is used to analyse large datasets and is central in machine learning.
- Planned topics for the session: scalars, vectors, matrices, dot product, normalisation (norms), linear combinations, least-squares fitting, and `regplot`.

### 2.2 Scalars, vectors, matrices, tensors

| Object | Dimension | Description / example |
|---|---|---|
| Scalar | 0-D | A single number with no direction. Examples: temperature $t$, flat price $P$, the number $5$. |
| Vector | 1-D | A list of numbers. It can be seen as a point, or as an arrow from the origin to that point. It has magnitude and direction. |
| Matrix | 2-D | A table of rows × columns. |
| Tensor | 3-D and higher | A collection of matrices, used for more than 2 dimensions. |

Points raised in class discussion:
- Vectors can be multi-dimensional and follow vector-algebra rules, such as component-wise vector addition.
- Scalars add directly.

### 2.3 Vector addition and scalar multiplication

Worked example: $u = (3, 1)$, $v = (1, 2)$.

$$u + v = (3+1,\; 1+2) = (4, 3)$$

$$2u = (2\cdot 3,\; 2\cdot 1) = (6, 2)$$

- Addition requires the **same shape**, and the result has the same shape.
- Multiplying by a scalar keeps the shape and scales each entry.

```python
import numpy as np

u = np.array([3, 1])
v = np.array([1, 2])

print(u + v)    # [4 3]
print(2 * u)    # [6 2]
```

**Plot.** The instructor drew $u$ (blue arrow, 3 in $x$, 1 in $y$), $v$ (1 in $x$, 2 in $y$) and $u+v$ as arrows from the origin. The exact plotting code was not dictated. A likely form:

```python
import matplotlib.pyplot as plt
plt.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='blue', label='u')
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='orange', label='v')
w = u + v
plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='green', label='u+v')
plt.xlim(-1, 5); plt.ylim(-1, 4); plt.grid(); plt.legend(); plt.show()
```

### 2.4 Data matrix example: three houses × three features

- The data is 3 houses stacked into a $3\times 3$ matrix.
- Each row is a house. The columns are the features **area, rooms, age**.
- Checking `.shape` gives `(3, 3)`.
- Indexing is **0-based**, so the **second house is row index 1**.
- The numbers $10, 25, 2$ were read out while indexing the matrix. The transcript does not make clear whether these were the second house's row or one column, and the full matrix was not read out. The values below are placeholders.

```python
# Values are illustrative; only "10, 25, 2" was audible
houses = np.array([[ 8, 20, 5],
                   [10, 25, 2],
                   [12, 30, 9]])
print(houses.shape)   # (3, 3)
print(houses[1])      # second house -> row index 1
print(houses[:, 1])   # a full column (one feature for all houses)
```

### 2.5 Dot product

**Definition.** Multiply matching entries, then sum:

$$u \cdot v = \sum_{i=1}^{n} u_i v_i$$

**Geometric form:**

$$u \cdot v = \lVert u \rVert \, \lVert v \rVert \cos\theta$$

The result is a **scalar**.

**Worked example:**

$$u \cdot v = 3\cdot 1 + 1\cdot 2 = 5$$

**Interpreting the sign.**
- $u\cdot v > 0$: the vectors point in broadly the same direction.
- $u\cdot v = 0$: the vectors are perpendicular (orthogonal).
- $u\cdot v < 0$: the vectors point in broadly opposite directions.
- The audio here was garbled ("zero means opposite"). The correct rule is that a **negative** dot product means opposite directions, and **zero** means orthogonal.

**Angle between vectors:**

$$\cos\theta = \frac{u\cdot v}{\lVert u\rVert\,\lVert v\rVert} = \frac{5}{\sqrt{10}\,\sqrt{5}} = \frac{5}{\sqrt{50}} = \frac{1}{\sqrt{2}} \;\Rightarrow\; \theta = 45^\circ$$

**Orthogonal example.** Two vectors $a$ and $b$ were shown to have $a\cdot b = 0$, so they are perpendicular. Their values were not audible; $a=(1,2)$, $b=(-2,1)$ below is an assumed example.

```python
print(u @ v)          # 5   (@ operator; transcript said "ampersand")
print(np.dot(u, v))   # 5

cos_theta = (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))
theta = np.degrees(np.arccos(cos_theta))
print(theta)          # 45.0 (approx., floating point)

a = np.array([1, 2]); b = np.array([-2, 1])   # assumed values
print(a @ b)          # 0 -> perpendicular
```

> **Transcription note:** the instructor said "ampersand", but the operator is `@`, which performs matrix multiplication or dot products in NumPy. `&` is bitwise AND and is a different operator.

### 2.6 Norms (length/magnitude) and distance

**L2 (Euclidean) norm.** This comes from Pythagoras: square each entry, add, take the square root.

$$\lVert u\rVert_2 = \sqrt{\sum_i u_i^2}, \qquad \lVert (3,1)\rVert_2 = \sqrt{3^2 + 1^2} = \sqrt{10} \approx 3.162$$

**L1 norm.** This is the sum of absolute values.

$$\lVert u\rVert_1 = \sum_i |u_i| = |3| + |1| = 4$$

**Distance between vectors.**

$$d(u,v) = \lVert u - v\rVert_2 = \lVert (2,-1)\rVert_2 = \sqrt{5} \approx 2.236$$

The lecture showed this as 2.23.

**Normalisation (unit vector).** This was mentioned as a topic. The standard definition is:

$$\hat{u} = \frac{u}{\lVert u\rVert}$$

The instructor flagged that distance computations like this are the basis of **k-Nearest Neighbours (KNN)**, which will be taught in a later class.

```python
print(np.linalg.norm(u))          # 3.1623  (L2, default)
print(np.linalg.norm(u, ord=1))   # 4.0     (L1)
print(np.linalg.norm(u - v))      # 2.2361  (distance u to v)
u_hat = u / np.linalg.norm(u)     # unit vector (normalisation)
```

### 2.7 Linear independence and rank

**Example:** $v_1 = (1,2)$, $v_2 = (2,4)$.

- **Question:** Does $v_2$ add new information? No, because $v_2 = 2v_1$. The vectors are **dependent**.
- **Rank** is the number of truly independent columns (or rows).
- The matrix $[v_1 \; v_2]$ has 2 columns but **rank 1**.
- The two vectors are independent only if the rank equals the number of vectors.

```python
v1 = np.array([1, 2])
v2 = np.array([2, 4])
M = np.column_stack([v1, v2])     # instructor "stacked" them; column_stack/vstack inferred
print(M.shape)                    # (2, 2)
r = np.linalg.matrix_rank(M)
print(r)                          # 1
print("independent" if r == M.shape[1] else "dependent")   # dependent
```

### 2.8 Matrices: definition, addition, scalar multiplication

- A matrix of size $m\times n$ has $m$ rows and $n$ columns.
- In a data matrix, rows are samples and columns are features.
- A vector is a matrix with one row or one column.

**Worked example matrices:**

$$A = \begin{pmatrix} 2 & 1\\ 1 & 3\end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0\\ 4 & 1\end{pmatrix}$$

**Addition and scalar multiplication** (both require the same shape for addition):

$$A + B = \begin{pmatrix} 3 & 1\\ 5 & 4\end{pmatrix}, \qquad 3A = \begin{pmatrix} 6 & 3\\ 3 & 9\end{pmatrix}$$

```python
A = np.array([[2, 1],
              [1, 3]])
B = np.array([[1, 0],
              [4, 1]])
print(A.shape, B.shape)  # (2, 2) (2, 2)
print(A + B)             # [[3 1] [5 4]]
print(3 * A)             # [[6 3] [3 9]]
```

### 2.9 Matrix multiplication

**Definition.** For $C = AB$:

$$C_{ij} = \sum_{k} A_{ik} B_{kj}$$

That is, row $i$ of $A$ is multiplied pairwise with column $j$ of $B$, and the products are summed.

**Shape rule.** The number of columns of $A$ must equal the number of rows of $B$:

$$(m\times n)(n\times p) \to (m\times p)$$

**Worked example.** The lecture began with the first entry, $2\cdot 1 + 1\cdot 4 = 6$:

$$AB = \begin{pmatrix} 2\cdot1+1\cdot4 & 2\cdot0+1\cdot1\\ 1\cdot1+3\cdot4 & 1\cdot0+3\cdot1\end{pmatrix} = \begin{pmatrix} 6 & 1\\ 13 & 3\end{pmatrix}$$

**Does $AB = BA$?** This was asked in class. A student answered that they are equal "if it is commutative". The important fact is that **matrix multiplication is generally NOT commutative**. Here:

$$BA = \begin{pmatrix} 2 & 1\\ 9 & 7\end{pmatrix} \neq AB$$

```python
print(A @ B)   # [[ 6  1] [13  3]]
print(B @ A)   # [[2 1] [9 7]]  -> order matters
```

> **Common mistake:** `A * B` in NumPy is **element-wise** multiplication, not matrix multiplication. Use `A @ B` or `np.matmul` / `np.dot` for matrix multiplication.

### 2.10 Linear transformations

A matrix acts as a function $T$ that maps a vector $(x, y)$ to $(x', y')$. $T$ is linear if it satisfies two rules:

$$T(u + v) = T(u) + T(v), \qquad T(c\,u) = c\,T(u)$$

**Basis vectors:**

$$\hat{i} = \begin{pmatrix}1\\0\end{pmatrix}\ (x\text{-axis}), \qquad \hat{j} = \begin{pmatrix}0\\1\end{pmatrix}\ (y\text{-axis})$$

The columns of a matrix show where $\hat{i}$ and $\hat{j}$ land after the transformation.

**Types of transformation:**

| Type | Matrix | Effect in the lecture's 4-panel plot |
|---|---|---|
| Scaling | $\begin{pmatrix}2 & 0\\ 0 & 0.5\end{pmatrix}$ | The $x$-direction is stretched ×2 (red arrow to $(2,0)$). The $y$-direction is squeezed to half (green arrow to $(0, 0.5)$). |
| Rotation by $\theta$ | $\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}$ | With $\theta = 30^\circ$, the whole grid rotates like a sheet of graph paper. |
| Shear | $\begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}$ | Red $\hat i$ does not move. Green $\hat j$ is pushed to $(1,1)$. The grid leans like pushing the top of a stack of books. Shear shifts one coordinate in proportion to the other. |
| General | $A = \begin{pmatrix}2 & 1\\ 1 & 3\end{pmatrix}$ | A mix of stretch and slant. Red goes to $(2,1)$ and green goes to $(1,3)$. |

**How to read the plot.**
- Light grey shows the original grid.
- Blue shows the grid after the transformation.
- The red arrow is the image of $(1,0)$.
- The green arrow is the image of $(0,1)$.

**Rotation by 90°:**

$$\begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}0\\1\end{pmatrix}$$

```python
theta = np.radians(30)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
S = np.array([[2, 0], [0, 0.5]])     # scaling
H = np.array([[1, 1], [0, 1]])       # shear

R90 = np.array([[0, -1],
                [1,  0]])
print(R90 @ np.array([1, 0]))        # [0 1]
```

### 2.11 Determinant as an area-scaling factor

- The unit square spanned by $(1,0)$ and $(0,1)$ has area $1$.
- After applying $A$, the area becomes $5$.
- **Correct rule:**

$$\text{new area} = |\det A| \times \text{old area}$$

**2×2 determinant:**

$$\det\begin{pmatrix}a & b\\ c & d\end{pmatrix} = ad - bc, \qquad \det A = 2\cdot 3 - 1\cdot 1 = 5$$

The determinant (5) matches the transformed area (5).

> The verbal explanation of the area in the transcript ("square of diagonal terms then square root") was garbled. Use $|\det A|$.

### 2.12 Transpose, identity, determinant, inverse

**Transpose.** Flip rows and columns:

$$(A^T)_{ij} = A_{ji}$$

The transpose of a product reverses the order:

$$(AB)^T = B^T A^T$$

**Identity** $I$. Ones on the diagonal and zeros elsewhere, so $AI = IA = A$.

**Inverse** $A^{-1}$. It satisfies $AA^{-1} = I$ and exists only if $\det A \neq 0$. If $\det A = 0$, the matrix is called **singular** and has no inverse. For a $2\times2$ matrix:

$$A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b\\ -c & a\end{pmatrix}$$

For the example matrix:

$$A^{-1} = \frac{1}{5}\begin{pmatrix}3 & -1\\ -1 & 2\end{pmatrix}$$

```python
print(A.T)                  # transpose
print(np.eye(2))            # identity
print(np.linalg.det(A))     # 5.000000000000001 (floating point)
print(np.linalg.inv(A))     # [[ 0.6 -0.2] [-0.2  0.4]]
```

**Debugging tip shown in VS Code/Jupyter.** Hovering over a function such as `np.linalg.inv` shows its parameters (e.g. `a`) and its return value.

### 2.13 Solving linear systems $Ax = b$

**Method.**
- Write the equations in matrix form, with unknown vector $x = (x, y)^T$.
- The solution is:

$$x = A^{-1} b$$

- In practice, use `np.linalg.solve(A, b)`. It is more stable than computing the inverse.

**Example.**
- The first equation was $2x + y = 5$, drawn as the blue line.
- The second equation was drawn as the orange line, but it was not stated in the audio.
- The lines intersect at **$x = 1$, $y = 3$**.
- If the coefficient matrix was the same $A$, the second equation would be $x + 3y = 10$, which is consistent with $(1,3)$. This is an **assumption**.

```python
A = np.array([[2, 1],
              [1, 3]])
b = np.array([5, 10])        # second entry inferred
sol = np.linalg.solve(A, b)
print(sol)                   # [1. 3.]
```

**Visual check.** Plot both lines. Their intersection point is the solution.

### 2.14 Eigenvalues and eigenvectors

- An eigenvector is a direction that the matrix only stretches, without rotating it.
- **Definition:**

$$A v = \lambda v$$

  Here $\lambda$ is the eigenvalue and $v$ is the eigenvector.
- The eigenvalues are the roots of the characteristic equation:

$$\det(A - \lambda I) = 0$$

- **NumPy:** `lam, V = np.linalg.eig(A)`. `lam` holds the eigenvalues, and the **columns** of `V` are the eigenvectors.

```python
lam, V = np.linalg.eig(A)
print(lam)    # for A=[[2,1],[1,3]]: approx [1.382, 3.618], i.e. (5 ± sqrt(5))/2
print(V)      # eigenvectors as columns
# check: A @ V[:,0] ≈ lam[0] * V[:,0]
```

The lecture did not say which matrix was used here. The sample output assumes it was $A$.

### 2.15 Least-squares line fitting

**Model:**

$$y = \beta_0 + \beta_1 x + \varepsilon$$

- $\beta_0$ is the intercept (the shift from the origin, "$c$").
- $\beta_1$ is the slope ("$m$").
- $\varepsilon$ is noise.

**Goal.** Find the best-fit line by minimising the sum of squared vertical distances (residuals) from the points to the line:

$$S(\beta_0, \beta_1) = \sum_{i=1}^{n} \big(y_i - \beta_0 - \beta_1 x_i\big)^2$$

**Calculus approach.**
- Set $\dfrac{\partial S}{\partial \beta_0} = 0$ and $\dfrac{\partial S}{\partial \beta_1} = 0$.
- A positive second derivative means a minimum. A negative one means a maximum.

**Result:**

$$\beta_1 = \frac{\operatorname{Cov}(x,y)}{\operatorname{Var}(x)} = \frac{\sum_i (x_i-\bar{x})(y_i-\bar{y})}{\sum_i (x_i-\bar{x})^2}, \qquad \beta_0 = \bar{y} - \beta_1 \bar{x}$$

The instructor suggested doing this derivation **by hand**. The data values used in class were not read out, so the arrays below are placeholders.

```python
x = np.array([1, 2, 3, 4, 5])        # placeholder data
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])

beta1 = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean())**2)
beta0 = y.mean() - beta1 * x.mean()
y_hat = beta0 + beta1 * x

plt.scatter(x, y)
plt.plot(x, y_hat, color='red')
plt.show()

# Same thing with seaborn (shows a 95% confidence band by default)
import seaborn as sns
sns.regplot(x=x, y=y)
plt.show()
```

`sns.regplot` (the transcript said "ray plot" / "rake plot") draws the scatter, the fitted line, and a **95% confidence interval** band. The instructor suggested experimenting with it.

---

## 3. Functions, Operators and Built-ins Introduced

| Item | One-line explanation |
|---|---|
| `np.array(...)` | Creates a NumPy vector or matrix from a list or nested lists. |
| `.shape` | Returns a tuple of dimensions, e.g. `(3, 3)`. |
| `arr[i]`, `arr[:, j]` | Row $i$ and column $j$ indexing (0-based). |
| `+`, `*` with a scalar | Element-wise addition and scalar multiplication. |
| `@` | Matrix multiplication or dot product (the transcript's "ampersand"). |
| `np.dot(x, y)` | Dot product of vectors or matrix product. |
| `np.linalg.norm(v)` | L2 norm (length). Use `ord=1` for the L1 norm. |
| `np.arccos`, `np.degrees`, `np.radians` | Inverse cosine and angle unit conversion. |
| `np.cos`, `np.sin` | Used to build rotation matrices. |
| `np.column_stack` / `np.vstack` | Stack vectors into a matrix (exact function inferred). |
| `np.linalg.matrix_rank(M)` | Number of independent columns. |
| `A.T` | Transpose. |
| `np.eye(n)` | $n\times n$ identity matrix. |
| `np.linalg.det(A)` | Determinant. |
| `np.linalg.inv(A)` | Inverse (fails if the matrix is singular). |
| `np.linalg.solve(A, b)` | Solves $Ax=b$. |
| `np.linalg.eig(A)` | Returns eigenvalues and an eigenvector matrix (columns). |
| `plt.quiver` | Draws arrows (vectors). Assumed for the vector plots. |
| `plt.scatter`, `plt.plot` | Scatter points and draw the fitted line. |
| `sns.regplot` | Scatter plus regression line plus 95% CI band. |
| `help(f)`, `f?`, hover pop-up | Shows a function's parameters and return value. |
| `*args`, `**kwargs` | Extra positional and keyword arguments, often forwarded to an underlying function. |

---

## 4. Syntax Rules, Common Mistakes and Tips

- **`A * B` is element-wise multiplication. `A @ B` is matrix multiplication.**
- **Order matters:** in general $AB \neq BA$.
- **Shapes:** addition needs identical shapes. Multiplication needs (columns of $A$) = (rows of $B$).
- **Indexing is 0-based:** the "second house" is row `1`.
- **Singular matrices** ($\det = 0$) have no inverse. `np.linalg.inv` raises `LinAlgError`.
- Prefer `np.linalg.solve` over `inv(A) @ b`.
- **Floating point:** expect values like `det = 5.000000000000001` and an angle of `45.00000000000001`.
- To discover a function's parameters, use `help()`, `?`, or hover in VS Code/Jupyter.
- For what goes in `**kwargs`, check where the docstring says they are "passed to".
- Some options cannot be passed as kwargs and need separate calls. For example, `plt.legend()` is a separate call after setting `label=`.

---

## 5. Exam / Assignment Notes and Admin

- No items were explicitly flagged for exams.
- The instructor suggested **deriving the least-squares formulas by hand** and **experimenting with `sns.regplot`**.
- Distance and norm ideas will be reused in an upcoming **k-Nearest Neighbours** lecture.
- **Admin:** a student asked for slides and PDFs for this and previous sessions. The instructor said recordings and materials will be on the **LMS portal**. The student reported they were not yet visible, and the instructor said they would follow up.