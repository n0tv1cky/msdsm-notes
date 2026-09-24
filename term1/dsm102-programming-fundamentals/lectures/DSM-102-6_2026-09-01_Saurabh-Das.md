# DSM-102 — Session 6 (2026-09-01, Saurabh Das)
## Classes, Writing Your Own Modules, NumPy & Matplotlib

---

## 1. Session Overview

This session closes out the "core Python" part of the course and opens the "data science tooling" part. It begins with a quick recap of lists / tuples / dictionaries from the previous class, then introduces **classes** as containers that bundle functions together (called via the dot operator on an instance). From there it generalises to **modules** — the different import forms (`import math`, `import math as mx`, `from math import sqrt`, `from math import *` and why the last is bad practice) — and then the instructor live-writes his **own module** to a `.py` file from inside Google Colab using the `%%writefile` magic, demonstrating the crucial distinction between code *inside* a function (only runs when called) and code at *module level* (runs on import), plus the `if __name__ == "__main__":` idiom, `%run`, `dir()` and `__doc__`. The second half is a rapid tour of **NumPy**: array creation, element-wise vs. matrix operations, `np.dot`, the huge speed advantage of vectorised operations over Python loops (demonstrated with `%timeit`: ~181 µs vs ~3.67 ms), array-generating helpers (`zeros`, `ones`, `arange`, `linspace`, `reshape`, `diag`, random generators), random seeding for reproducibility, and dtypes (`int64`, `float64`, `bool`, `complex128`). It ends with a short **Matplotlib (`pyplot`)** demo — plotting `y = x²`, plotting multiple random series, legends, axis labels and titles — plus housekeeping about the 36-question assignment and an upcoming quiz.

---

## 2. Topics Covered (in teaching order)

### 2.1 Recap of the previous lecture (containers)
- **List** — the most frequently used container; holds objects of different types; indexed; can be built in one line via *list comprehension* (replaces many loops).
- **Dictionary** — stores **key : value** pairs; can hold many different object types; elements accessed by **key**.
- **Tuple** — elements are accessed differently; instructor stated (as spoken) that tuples "do not have repetitive elements and are not indexed" — ⚠️ *this appears to be a slip in the recap; in standard Python a **set** is unordered/unique and unindexed, while tuples ARE ordered and indexable. Check the previous session's notes.*
- All three serve different purposes; all are "very handy" once you write more programs.
- Already covered previously: functions, loops, `if` conditions, algebraic manipulation.

### 2.2 Classes

**Definition given:** a class is essentially the first step of *compacting / organising* different functions — "think of it as a container". A class can contain **many** functions, not just one.

```python
class Animal:
    def say_hi(self):
        print("hello")

x = Animal()      # bind the class to a variable (create an object)
x.say_hi()        # call the function inside, using the dot operator
# output: hello
```

- The function takes no user argument, "so instead of leaving it empty we just mention (`self`)" — *inferred: the spoken text says the parentheses are not left empty; the standard Python token here is `self`.*
- You call methods with the **dot operator**: `object.method()`.
- *Note: the exact class name (`Animal`) and method name (`say_hi`) are reconstructed from speech; the structure is certain, the names are best-effort.*

### 2.3 Modules — the four import forms

> "Class and module are kind of the same thing. The only difference: a class lives in your working environment; a module is stored in some other file."

Some functions are built in (no import needed); advanced functionality requires importing a module.

```python
# 1. plain import  -> must use dot notation
import math
math.sqrt(4)

# 2. import with an alias -> give a short/meaningful name
import math as mx
mx.sqrt(4)          # the alias can be anything: mx, ny, s, ...

# 3. import only the piece you need -> no dot operator needed afterwards
from math import sqrt
sqrt(4)

# 4. wildcard import -> imports EVERYTHING
from math import *
sqrt(4)
```

- **Why aliases are useful:** a meaningful short name makes it easier to remember what the imported code is doing in your program.
- **Why `from module import *` is BAD PRACTICE** (explicitly flagged):
  1. It pulls in many functions that are irrelevant to you.
  2. **Name conflicts** — you don't know what names the module uses; they may clash with your own variable/function names.
  - Only use it if you *consciously* intend to use all the functionality of that module directly.

### 2.4 Writing your own module

**Step 1 — write a file from inside Colab with the cell magic `%%writefile`:**

```python
%%writefile first_module.py

def hello_world():
    print("hello world")
    print("this is my first module")

print("this is a script")
```

- `%%writefile <name>.py` must be the **first line of the cell** ("at the top of this thing"); it writes the rest of the cell to a file in your workspace.
- `.py` is the normal Python extension. Colab's default workspace contains only a `sample_data` folder until you create files; after running, `first_module.py` appears.
- *Inferred:* exact strings printed are reconstructed from speech ("hello world", "this is my first module", "this is a script").

**Step 2 — import it and call the function:**

```python
import first_module            # the module-level print runs here -> "this is a script"
first_module.hello_world()     # -> hello world
                               #    this is my first module
```

**Key teaching point (asked as a question in class):**
> *"My file has three print lines — why did I only get two when I called `hello_world()`?"*
> Because the third print is **outside the function** — look at the **indentation**: `print("this is a script")` is aligned with `def`, so it is module-level code, not part of the function.

**Step 3 — run the same file as a *script* instead:**

```python
%run first_module.py
```
- You must give the **full file name including the `.py` extension**.
- Output: only `this is a script`. The function is *defined* but never *called*, so it produces no output.
- **Rule stated:** *any file can be treated as a module (imported) or run as a script — it depends on how you choose to use it.* Nothing in the file itself marks it as one or the other.

**Step 4 — `if __name__ == "__main__":`**

> "By default Python executes all code in a module when we import it. However, we can make code run **only** when the file is the main file."

```python
%%writefile first_module.py

def hello_world():
    print("hello world")
    print("this is my first module")

if __name__ == "__main__":
    hello_world()
```
- Now `import first_module` does **not** auto-run `hello_world()`; `%run first_module.py` does.
- To get the functionality you must **either import the module and call the function, or run it as a script.**

### 2.5 Inspecting a module: `dir()` and `__doc__`

A second, richer module (spoken as `simple_module.py`) was written, containing a **docstring**, a variable `x = 2`, a function, and a `__main__` block:

```python
%%writefile simple_module.py
"""
This is a simple function containing a module
"""

x = 2

def simple_func():
    print("hi this is from within the module")

if __name__ == "__main__":
    print("running as a script")
    simple_func()
```
*(Inferred: function name, the exact `__main__` print text, and formatting. The docstring text "this is a simple function containing a module" is as spoken.)*

```python
import simple_module

print(dir(simple_module))   # list everything inside the module
simple_module.x             # -> 2   (module-level variables are accessible)
simple_module.simple_func() # -> hi this is from within the module
simple_module.__doc__       # -> "This is a simple function containing a module"

%run simple_module.py       # runs the module-level code AND the __main__ block
```

- `dir(module)` shows many objects **you never created** — these are the *default structure* of every module:
  `__builtins__`, `__cached__`, `__doc__`, `__file__`, `__loader__`, `__name__`, `__package__`, `__spec__`, followed by your own functions and variables.
- `__doc__` automatically picks up the triple-quoted **docstring** at the top of the file.
- **Q&A clarification (important conceptual point):** the double underscores are **not** a class-only or method-only convention. They are simply the naming style used for these *default/built-in* attributes. "This underscore has nothing to do with class or function — it's a way of writing by default, because these are default values." You *may* name your own variables with a leading underscore, but that's up to you.
- Everything up to `__spec__` will be present in **any** module you check or write.

### 2.6 NumPy

**Motivation:** until now we manipulated numbers and lists. Linear algebra / matrix notation makes a huge amount of algebraic manipulation easy — NumPy gives you that.

- 1-D array = vector; 2-D array = **matrix**; 3-D array = **tensor**; you can go to 4, 5, 7, … dimensions. Visualising >3-D is hard, but you can still create and manipulate them algebraically.

```python
import numpy as np        # np is the conventional short alias
```

#### Creating arrays and element-wise algebra

```python
x = np.array([[0, 1],
              [1, 5]])
y = np.array([[4, 0],
              [0, 4]])
```

| Operation | Code | Result |
|---|---|---|
| Addition | `x + y` | `[[4, 1], [1, 9]]` |
| Element-wise power | `x ** 2` | `[[0, 1], [1, 25]]` |
| Element-wise product | `x * y` | `[[0, 0], [0, 20]]` |
| **Matrix** product | `x @ y` | `[[0, 4], [4, 20]]` |
| Sum of all elements | `np.sum(x)` | `np.int64(7)` |

- Worked arithmetic shown on the board: `0+4=4, 1+0=1, 1+0=1, 5+4=9`; `0*4=0, 1*0=0, 0*1=0, 5*4=20`; total sum `0+1+1+5 = 7`.
- **Why the output prints as `np.int64(7)` and not just `7`:** everything in Python is an *object*; the sum creates a NumPy object whose type is 64-bit integer. `int64` = integer stored in 64 bits.

#### Random numbers

```python
x = np.random.rand(10000)   # 10000 random numbers, uniform in [0, 1)
y = np.random.rand(10000)

z = 0
for i in range(10000):
    z = x[i] * y[i] + z

print(z)     # e.g. np.float64(2537.xxx) -- changes every run
```
- Structure explained in Q&A: `np` = the module → `random` = a sub-module for random-number generation → `rand` = the function that draws from **[0, 1)**.
- Because it's random, the *same command* produces a *different* array each time.
- `x` printed shows the first three and last three values with `...` in between (10 000 elements).

**Same thing without a loop — the dot product:**
```python
np.dot(x, y)      # multiplies element-by-element AND sums, in one vectorised call
```

#### `%timeit` — speed comparison (key demonstration)

```python
%timeit np.dot(np.random.rand(10000), np.random.rand(10000))
# ~181 µs ± 9.67 (per loop)

%timeit  # the explicit Python for-loop version of the same computation
# ~3.67 ms per loop
```
- `%timeit` = magic command that measures execution time of a command.
- **Conclusion:** the explicit loop is roughly an *order of magnitude* (µs → ms) slower, because it multiplies and accumulates one element at a time. NumPy's built-in does it as a matrix operation.
- **This is the main reason to prefer NumPy arrays over plain lists**: with a list you *must* walk element by element; with an array you get matrix operations directly and much faster.

#### Array-generating functions

```python
np.zeros((10, 10))          # 10x10 matrix of zeros
a.shape                     # -> (10, 10)  ; .shape gives the dimensions

np.ones((10, 10))           # 10x10 matrix of ones
np.ones((10, 10)) * 2 + 3   # scalar algebra broadcasts -> every entry becomes 5

np.random.rand(5, 5)        # 5x5 uniform random in [0,1)
np.random.randn(5, 5)       # 5x5 "normalised" random  (described in class as values ~ -1 to +1)

np.arange(1, 100, 2)        # like range() but produces an ARRAY: 1,3,5,...  (start, stop, step)
x = np.arange(100)          # default step = 1 -> 100 elements
x.shape                     # -> (100,)  i.e. a 1-D array of 100 elements

np.linspace(0, 5, 10)       # 10 EQUALLY SPACED points from 0 to 5 (endpoints included)

x.reshape(10, 10)           # turn the 100-element 1-D array into a 10x10 matrix
np.ones(9).reshape(3, 3)    # ones reshaped to 3x3   (inferred exact form)
np.zeros((2, 4, 2))         # 3-D array: 2 stacks x 4 rows x 2 elements (inferred shape order)

np.diag(M)                  # extract / generate the diagonal of a matrix
np.random.uniform(3, 6, size)   # uniform random numbers in a chosen RANGE (3 to 6), not just 0-1
```

**`linspace` vs `arange` (explained in detail after a student question):**
- `arange`: you specify **start, stop and the increment** — you know the step, you don't directly control how many points.
- `linspace`: you specify **start, stop and how many divisions** — you know the count, the step is computed for you. Start and end points stay fixed and the space between is divided equally.
- Analogy given: planting markers at equal spacing in a field between a start and an end point.
- Worked example from class: `np.linspace(1, 5, 4)` → `1, 2.33, 3.67, 5`, i.e. spacing of ≈ **1.33** between consecutive points (1→2.33 is 1.33, 2.33→3.67 is 1.33, 3.67→5 is 1.33). *(Student initially expected 1,2,3,4 — that would be `np.arange(1,5)`.)*

#### Random seeding / reproducibility

```python
np.random.seed(1234)
np.random.normal(mu, sigma, size)    # Gaussian / normal draws
```
- **Problem:** random results change on every run, which is bad when you need to demonstrate or reproduce a specific result.
- **Solution:** fix the **seed**. The numbers are still random, but the *series* produced is reproducible — same seed ⇒ same sequence every time. Change the seed ⇒ different (but again reproducible) sequence.
- **Gaussian / normal distribution** (revised in class): bell-shaped curve; **`mu` = mean**, **`sigma` = standard deviation** (controls the width/shape).
- Q&A: *"Does seeding mean the numbers aren't truly random?"* — Answer: the numbers are generated randomly from the distribution; the seed only pins down *which* series you get. Analogy used: watching a watch's second hand — whether it lands on 5 or 6 is random, but the rule "odd ⇒ output X" is deterministic. So there's always an inherent deterministic mechanism, while the distribution stays random.

#### Data types (dtypes)

```python
a = np.array([1, 2, 3])
a.dtype                          # -> int64

b = np.array([1., 2., 3.])       # note the decimal points
b.dtype                          # -> float64

c = np.array([1, 2, 3], dtype=np.int64)   # force the type
c.dtype                          # -> int64

np.array([True, False, True, False]).dtype     # -> bool

d = np.array([1, 2, 3], dtype=np.complex128)   # -> 1.+0.j, 2.+0.j, 3.+0.j
```
- Arrays handle **integers, floats, booleans and complex numbers**.
- **Q&A — `int32` vs `int64` (memory & performance):** `int32` uses less memory and is somewhat faster; `int64` uses more memory but gives better **precision**. Which you want depends on the precision your calculation requires. *"This is not peculiar to Python — it's the same in any programming language."*

### 2.7 Matplotlib

```python
import matplotlib.pyplot as plt     # matplotlib is the package, pyplot the module we need
import numpy as np

x = np.linspace(-5, 5, 100)
y = x ** 2

plt.plot(x, y)      # simple x-y line plot -> a PARABOLA (y = x²)
```
- **Debugging note from the live demo:** calling `plt.plot(...)` *before* importing matplotlib raised an error — the fix was simply to run the import first. (Classic "I forgot the import" bug.)

```python
plt.plot(y)                         # only one argument -> x-axis becomes the INDEX
                                    # of each element (0 to 99 in Python)

plt.plot(np.random.rand(100))       # plot 100 random numbers -> fluctuating curve,
                                    # different every run (no seed set)
```
- Calling `plt.plot()` **two or three times in the same cell** puts all curves in the **same figure**, and Python automatically assigns each a **different colour**.

**Labelling:**
```python
plt.plot(x, y)
plt.legend(["y = x^2"])   # legend = the name(s) of the curve(s)
plt.xlabel("x")           # x-axis label
plt.ylabel("y")           # y-axis label
plt.title("Parabola")     # figure title
```
*(Exact label strings inferred — the instructor only said "we put a legend, xlabel, ylabel and title".)*

- **Q&A:** *Can the figure be exported (to Word, etc.)?* — Yes. Just as you can write text from Python to a file, you can export the image as **JPEG / PNG** or other formats. *(Standard call: `plt.savefig("figure.png")` — inferred, not spoken verbatim.)*

### 2.8 Ecosystem of useful modules (asked by a student)

> *"Is there a command that lists all modules available?"* — **No**, new modules appear constantly; anyone can write one.

Most commonly used, as ranked by the instructor:
- **NumPy** — arrays/matrices, numerical work. (Covered today, "only scratching the surface".)
- **math** — basic math functions (`sqrt`, etc.).
- **Matplotlib** — plotting. (Covered today.)
- **pandas** — handles similar data but in a **DataFrame** (like a table with text column names plus values). **Will be covered later in the course.**
- *NumPy + Matplotlib + pandas = the three main modules for all basic manipulation and basic statistics.*
- **SciPy** — sophisticated statistical analysis, integration, differentiation.
- **scikit-learn** and **TensorFlow** — machine learning.
- Specialised/domain packages: **astropy** (astronomical data), climate-data packages, etc.

---

## 3. Function / keyword / operator reference (everything introduced today)

| Item | One-line meaning |
|---|---|
| `class` | Keyword that defines a class — a container bundling functions (methods) together. |
| `self` | First parameter of a method; refers to the instance (used because the method takes no user argument). |
| `.` (dot operator) | Accesses a function/variable inside an object, class instance, or module. |
| `import <module>` | Loads the whole module; access members with `module.name`. |
| `import <module> as <alias>` | Loads the module under a shorter/meaningful name. |
| `from <module> import <name>` | Loads only one function/object; call it directly without the dot. |
| `from <module> import *` | Imports everything — **bad practice** (irrelevant names + name conflicts). |
| `%%writefile name.py` | Colab/IPython **cell magic**; writes the rest of the cell into a file `name.py`. Must be the first line of the cell. |
| `%run name.py` | IPython magic; executes a `.py` file as a script (full filename with extension required). |
| `%timeit <statement>` | IPython magic; measures average execution time of a statement (reports mean ± spread per loop). |
| `if __name__ == "__main__":` | Block that runs only when the file is executed as the main script, not when it's imported. |
| `__name__` | Module attribute holding the module's name (`"__main__"` when run as a script). |
| `__doc__` | Module/function attribute holding its docstring. |
| `__file__`, `__loader__`, `__package__`, `__spec__`, `__builtins__`, `__cached__` | Other default attributes present in every module (seen via `dir()`). |
| `dir(obj)` | Lists all names/attributes contained in a module or object. |
| `def` | Defines a function. |
| `print()` | Prints to output. |
| `math.sqrt(n)` | Square root, from the `math` module. |
| `np.array([...])` | Creates a NumPy array from nested lists. |
| `+`, `-`, `*`, `**` on arrays | **Element-wise** arithmetic. |
| `@` | **Matrix multiplication** operator for arrays. |
| `np.sum(a)` | Sum of all elements of an array. |
| `np.dot(x, y)` | Dot product: element-wise multiply then sum (vectorised, fast). |
| `np.random.rand(n)` / `rand(m, n)` | Uniform random numbers in [0, 1). |
| `np.random.randn(m, n)` | Random numbers from the standard normal distribution. |
| `np.random.uniform(low, high, size)` | Uniform random numbers in an arbitrary range (e.g. 3 to 6). |
| `np.random.normal(mu, sigma, size)` | Gaussian random numbers with mean `mu`, std-dev `sigma`. |
| `np.random.seed(n)` | Fixes the random series so results are reproducible. |
| `np.zeros(shape)` | Array filled with zeros. |
| `np.ones(shape)` | Array filled with ones. |
| `np.arange(start, stop, step)` | Array of evenly spaced values by **step** (default step 1). |
| `np.linspace(start, stop, num)` | Array of **num** equally spaced values, endpoints included. |
| `a.reshape(r, c)` | Rearranges an array into a new shape (e.g. 100 → 10×10). |
| `a.shape` | Tuple giving the array's dimensions. |
| `a.dtype` | The data type of the array's elements. |
| `np.int64 / np.int32 / np.float64 / bool / np.complex128` | NumPy data types (integer, float, boolean, complex). |
| `dtype=` argument | Forces an array to a particular data type. |
| `np.diag(M)` | Diagonal of a matrix. |
| `import matplotlib.pyplot as plt` | Imports the plotting sub-module, conventionally aliased `plt`. |
| `plt.plot(x, y)` / `plt.plot(y)` | Line plot; with one argument the x-axis becomes the element index. |
| `plt.legend([...])` | Names/labels for the curves. |
| `plt.xlabel()`, `plt.ylabel()`, `plt.title()` | Axis labels and figure title. |

---

## 4. Syntax rules, common mistakes & debugging tips flagged in class

1. **Indentation decides scope.** A `print` aligned with `def` is *outside* the function and therefore runs at import/script time, not when the function is called. This was the cause of the "why did I only see two lines?" question.
2. **A `.py` file is neither inherently a module nor a script** — how you use it (import vs `%run`) determines its role.
3. **Importing a module executes all its module-level code.** Wrap script-only code in `if __name__ == "__main__":` to prevent that.
4. **Defining a function is not calling it.** Running the script produced no function output until the function was actually called.
5. **`%run` needs the full filename with the `.py` extension.**
6. **`%%writefile` must be the first line of the cell.**
7. **Never use `from module import *`** unless you deliberately want everything — risk of name collisions with your own variables/functions.
8. **Forgot the import ⇒ error.** The `plt.plot` call failed purely because `matplotlib` had not been imported yet; check your imports first when a name is undefined.
9. **Avoid Python loops for array math.** Use NumPy vectorised operations / `np.dot` — demonstrated to be ~an order of magnitude faster (181 µs vs 3.67 ms).
10. **Random output changes every run** unless you set `np.random.seed(...)`. Set a seed whenever you need reproducible demos/results.
11. **`int32` vs `int64`:** trade memory/speed against precision — choose according to the precision your computation needs.
12. **Double-underscore names are conventional defaults, not class-only syntax.**

---

## 5. Exams / Assignments / Admin

- **Assignment already uploaded to Google Drive: ~36 questions.**
  - Early questions are simple (familiarisation); later ones get progressively complex.
  - ⚠️ **"You should try that without using ChatGPT."** You may use ChatGPT/Google for *small portions*, but **not to generate the whole program**.
  - **Submission format: Python `.py` files — individual file per question** (as confirmed when a student asked whether to submit notebooks or code snippets).
  - Upload location to be confirmed; instructor agreed (after student request) to **post the assignment on the LMS** within a few days, since all other subjects use the LMS.
- **Quiz:** was planned for the end of this session; deferred — "maybe **Friday** we can have this quiz" (explicitly *a quiz, not an exam*).
- **Course handover:** the Python basics are essentially complete; **from next week Prof. Dutta takes over the classes**.
- Topics still to come later in the course: **pandas** (DataFrames), and more depth in NumPy/Matplotlib — today was "just scratching the surface".