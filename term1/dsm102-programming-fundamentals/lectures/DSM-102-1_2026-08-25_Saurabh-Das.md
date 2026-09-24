# DSM-102 — Programming Fundamentals for Data Science
## Session 1 — 2026-08-25 — Instructor: Prof. Saurabh Das
*(Dept. of Astronomy, Astrophysics & Space Engineering, IIT Indore — works with remote-sensing satellite data)*

---

## 1. Overview

This is the **first, introductory session** of the course. The instructor first motivates *why* a data scientist must program — using a "spot-the-difference" camouflaged-image demo to show that human vision/brain is a slow, inefficient "biological computer", while a machine can find changes in huge volumes of data quickly and repeatably. He then defines **learning** (a system improving its performance from experience) with everyday analogies (classifying fruits vs. flowers, catching a cricket ball, reverse-parking a car → artificial neural networks / autonomous vehicles), and explains that programming languages are simply the vocabulary + rules by which we instruct a computer. He surveys **Python** (easy, intuitive, flexible, huge ecosystem — but less control, poorer raw performance, fewer safety checks), explains installation options (Anaconda/pip, Jupyter) versus the cloud-based **Google Colab** used in class, walks through the **three-module course structure** (Python basics + NumPy/SciPy/Matplotlib → data exploration & ML with scikit-learn/TensorFlow → advanced topics + R), and finally moves into live Colab coding: the `print()` "Hello World" program, string quoting rules, the four value types (bool, str, int, float), the `type()` function, variables, dynamic typing / reassignment, case sensitivity, and `==` vs `=`.

---

## 2. Topics & Concepts, in Order Taught

### 2.1 Class logistics / audience survey
- Roughly **10 students out of the class already know some programming**; roughly the same number know Python. Backgrounds mentioned: architecture (B.Arch), finance & capital markets (uses Alteryx and Tableau, not code), computer science engineering.
- The class will be **interactive**: passive attendance ≠ learning. Students are expected to type along in Colab.

### 2.2 Why programming? (the camouflage-image demo)
- An animated/generated image was flipped repeatedly; objects were deliberately **camouflaged against the background**.
- First viewing: students spotted only the **cat** and the **dog** (highest contrast with background). Later viewings revealed an **owl**, a **parrot**, a **rabbit/rat**, a **bird (green, blending with background)**, and something in a nest.
- **Takeaway:** the human eye + brain is a computer, but a slow and inefficient one. A program can detect all changes in a short time span, with reproducible recording of results.
- **Purpose of a data scientist:** *extract information from data* — which requires "playing with" data at volume, only feasible via programming.

### 2.3 What a programming language *is*
- We interact with a computer via **instructions**. Analogy: to teach a child `a + b`, you first teach the *language of mathematics*.
- **Definition given:** *A programming language is a vocabulary and a collection of rules that command a computer, device or application to work according to the written code.*
- The computer does **exactly and only** what you instruct:
  - instruct it to find changes → it finds changes;
  - instruct it to count leaves → it counts leaves, ignoring changes;
  - instruct it to detect parrots → across many images it reports only parrots.
- Hence the burden is on the **coder** — efficiency of the solution depends on how well you write the instructions.

### 2.4 Definition of "learning" (theme of the whole MSc programme)
- **Learning = a process in which a system improves its performance based on experience.**
- Two routes, mirroring supervised/unsupervised ideas:
  1. **With a teacher** — a known object is given a name/label (child in school).
  2. **Without a teacher** — the learner observes objects/phenomena and infers structure on its own.
- **Worked analogies:**
  - *Classification:* give a student mixed objects — some fruits, some flowers — with a few labelled examples; the student then classifies a **new, unseen** object as fruit or flower.
  - *Catching a ball:* perceive the ball → estimate its **speed** and **angle** → position hand. Great cricketers have strong hand–eye coordination. Practice matters because **each error is fed back and minimised next time**, converging on a robust solution.
  - Note: humans do **no explicit mathematical calculation** while catching a ball — learning is not always mathematical modelling. But to communicate with a computer we **do** need a mathematical model, and that model is built **from data** → this is where data science enters.
  - *Reverse parking a car:* mathematically it involves turning-angle limits (tyres can't rotate infinitely), vehicle dimensions, and a tight space. In practice a human iterates — swing left (overshoot), swing right (hit boundary), tilt, correct again — until the car fits. This iterative correction is done by the brain's neural function; its computational counterpart is the **Artificial Neural Network**, used in autonomous vehicles.
- **Three dimensions in which a program/agent improves:**
  1. **Range / scope** — the agent can *do more* things.
  2. **Accuracy** — the agent can do things *better*.
  3. **Speed** — the agent can do things *faster* (depends on how efficiently you code).

### 2.5 How to learn programming
- **Practice is the only way.** Don't restrict yourself to the assignments given; implement your own ideas.
- Python is "almost like English" — syntax is flexible and user-friendly.
- If you know **C, C++, Java, MATLAB**, the **logic and algorithms are identical**; only the **syntax** changes, and Python's syntax is easier.
- The instructor promises the skill is essential for **every other course in the MS-DSM programme**.

### 2.6 Python: pros and cons
**Pros**
- Easy to learn — you can write your first program within one class.
- Intuitive syntax.
- Broad application: data science, animation/video generation, control applications, etc.
- Very vibrant community; new packages every day; large GitHub ecosystem.

**Cons**
- **Less control** over the machine than C/C++ → performance can be worse if you are careless.
- **Less safety handling**: a small change in syntax or logic can produce *completely wrong output without an error*. It is the **user's responsibility to cross-check every line**.

### 2.7 Installation, environments and package management
- **Linux / macOS:** Python can be invoked from the command line; install via command-line tools.
- **Windows:** download a distribution package (e.g. Anaconda-type distributions).
- **Jupyter Notebook:** lets you invoke Python and store code, results and visualisations on a single page. **Strongly recommended** to install locally — it will matter later for machine-learning/deep-learning work.
- **For this class:** **Google Colab** — cloud-based, nothing to install, log in with a Google account, notebooks stored in the cloud.
- **Package manager: `pip`**
  - Packages do **not** all come bundled; you must **install** and then **import** them.
  - Syntax demonstrated verbally:
    ```bash
    pip install pandas      # Python 2 era / default pip
    pip3 install pandas     # for Python 3
    ```
- **Python 2 vs Python 3**
  - Python 3 is now mainstream, but a lot of legacy code is still Python 2.
  - Differences are **mostly syntactic**; a Python 2 program will not run under Python 3 unless the syntax is corrected. Run Python 2 code with Python 2, Python 3 code with Python 3, or you will get version-mismatch failures.
  - Use `pip` for Python 2 packages, `pip3` for Python 3 packages.

### 2.8 Course structure (three modules)
1. **Module 1 — Python basics** (≈ 6–7 classes, taught by this instructor)
   - Jupyter/Colab, language basics, simple computation
   - **NumPy** — arrays and vectors; matrix multiplication, linear algebra
   - **SciPy** — e.g. curve fitting
   - **Matplotlib** — plotting
2. **Module 2 — Exploring data**
   - Descriptive statistics, distributions
   - Time-series analysis and prediction
   - Classification, clustering, regression
   - ML libraries: **scikit-learn** and **TensorFlow**
   - Goal: Python not as programming for its own sake, but as a **tool to explore data and extract meaningful information**
3. **Module 3 — Advanced topics**
   - Databases, GUIs, object-oriented applications, advanced packages
   - Brief introduction to **R** — widely used for exploratory analysis; same concepts, different syntax (how to call, how to write functions, etc.)

### 2.9 Resources
- Many good **YouTube videos** and online tutorials.
- Recommended **books** (titles shown on slide, not read out).
- **Official documentation** of each package — the go-to when stuck.
- Internet + GitHub for examples.

---

## 3. Live Coding in Google Colab

> *Note: the transcript describes the notebook verbally; the code blocks below are best-effort reconstructions. Where exact spelling/values were ambiguous I flag it.*

### 3.1 Getting into Colab
- Google-search "Colab", or find it inside your Google account's app list; log in with your Gmail ID.
- Create a **New notebook**. A notebook mixes **text cells** (markdown notes, images) and **code cells**.
- Running the first cell → the notebook **connects to a cloud server** ("Connecting…"), which takes some seconds the first time, then shows the **RAM and disk allocated** to your session. After connecting it runs fast.

### 3.2 First program — "Hello World"

```python
print("hello world tomorrow")
```
*(Output: `hello world tomorrow`. The exact string spoken was "hello world tomorrow" — likely "Hello World" plus an extra word typed by the instructor.)*

- `print` is a **function**; its purpose is to display something.
- Whatever is inside the parentheses **under quotation marks** is printed **as-is** — no processing is done on quoted text.
- The quotation marks are what tell Python "treat this as literal text".

### 3.3 Quoting rules (flexibility vs. strictness)

```python
print("hello world tomorrow")   # works — double quotes
print('hello world tomorrow')   # works — single quotes
print("hello world tomorrow')   # ERROR — mixing quote styles
```

- **Rule:** single quotes and double quotes are **interchangeable** in Python (unlike C/C++, where `'a'` is a character and `"a"` is a string and they are *not* interchangeable).
- **But** you must **not mix** them for one literal — open and close with the *same* type.
- **Lesson:** Python is more flexible than C/C++, but not *every* restriction can be bypassed.

### 3.4 Function vs. value
- In `print("hello world")`:
  - `print` → the **function** (defines the purpose/functionality).
  - `"hello world"` → the **value** passed to it (what's inside the parentheses).
- A **value** is the fundamental thing a program manipulates. It can be text, a number, a fraction, or a logical/Boolean value.

### 3.5 The four types of values
| Type | Meaning | Example |
|---|---|---|
| **Boolean** (`bool`) | logical | `True`, `False` |
| **String** (`str`) | anything written inside quotes | `"hello"`, `'2.1'` |
| **Integer** (`int`) | whole number | `2` |
| **Float** (`float`) | fractional / decimal number | `2.1` |

> The instructor stated these are **the only four types of value** that can be passed through a program at this level. (More types — lists, dicts, classes — come later; "class" was explicitly deferred to class 3 or 4.)

### 3.6 The `type()` function — worked examples

```python
a = 2
type(a)          # -> int
```

```python
a = 2.1
type(a)          # -> float     ("float means it is a fractional number")
```

```python
a = "2.1"        # quotation marks put around the number
type(a)          # -> str       (no longer a number at all — it's text)
```

### 3.7 **No type casting / dynamic typing** (key difference from C/C++)
- In C/C++ you must **declare** a variable's type first (`int a;`, `float a;`) and only that type of value may be stored in it.
- In Python **you do not declare a type**. The value you assign *determines* the type, and you may reassign a different type any number of times.
- **Student Q:** "If `a = 2.8` (float), can I later change it to a string?" → **Yes**, freely; no error is raised.
- **Why this is dangerous:** because there is no type checking, a **wrong value assigned by mistake is silently accepted** — nothing stops the program, and you may get wrong results with no error. *Be careful what you pass into a variable.*

### 3.8 Variables — the core idea

```python
x = 1
print(x)         # -> 1
```
```python
x = 10
print(x)         # -> 10   (same print statement, different output)
```

- A **variable** is a named store for a value; the value may be of any of the four types.
- Variables are the **most important thing in any programming language**, because a program is pointless if values are fixed — the whole purpose is to change/manipulate values and get new output. The `print(x)` line never changes; only `x` does.

### 3.9 Good practice — meaningful variable names

```python
x = 10
y = 5
sum_of_xy = x + y        # meaningful name
print(sum_of_xy)         # -> 15
```
*(The instructor spoke of a variable named as "the sum of x and y" — exact spelling, e.g. `sum_xy` / `sumofxy`, inferred.)*

- **Rule/advice:** do **not** use `a`, `b`, `c`, `x`, `y`, `z` in real code. In a program of thousands of lines, where a variable is used 50–70 lines after it is defined, a descriptive name makes it easy to find out what it does.

### 3.10 Reassignment — "the program only remembers the last assignment"

```python
x = 1
x = "a"          # reassigned to a string — no error
print(x)         # -> a
```
- The original value `1` is **lost**. Python remembers only the **most recent** assignment and **does not care whether it was correct or wrong**.
- This is a very common real-world bug source when assigning values repeatedly in long programs.

```python
x = 1
type(x)          # -> int
x = "1"
type(x)          # -> <class 'str'>
x = 1.5          # (value inferred)
type(x)          # -> <class 'float'>
```

### 3.11 `print(type(x))` and the word "class" — student question
- **Observation:** `type(x)` alone shows the type, but `print(type(x))` prints something like `<class 'str'>` — an extra word "class".
- **Instructor's answer:** inside `print()` you are calling the *object* `type`, so the output is reported as an **object class** plus the type name. **What a class and an object are will be covered in class 3 or 4.**

### 3.12 Boolean / comparison operations

```python
'a' == "a"       # -> True   (single vs double quotes make no difference to the string)
'a' == "b"       # -> False
'a' == "A"       # -> False
```

- **`=` (single equals) = assignment** — gives a variable a value.
- **`==` (double equals) = comparison/equality test** — checks whether two things are equal; returns `True` or `False`.
- **Case sensitivity:** lowercase and uppercase letters have **different binary values**, so `'a' == 'A'` is `False`. Consequently, if you define a variable as `x` and later call `X`, **it will not work — you will get an error.**

### 3.13 Open question left as homework (not answered)
- **Student Q:** In C++ there is a `char` type using single quotes, which can be equated to an ASCII number. Can this be done in Python, and how?
- **Instructor:** "Try it, experiment — programming is learned only through experimentation." He deliberately withheld the answer. **Worth investigating yourself** (hint: look up `ord()` / `chr()`).

---

## 4. Complete list of things introduced

| Item | Kind | One-line explanation |
|---|---|---|
| `print()` | built-in function | Displays the value(s) inside the parentheses; quoted text is printed literally. |
| `type()` | built-in function | Returns the data type of the value/variable passed to it. |
| `"..."` / `'...'` | string literals | Double or single quotes mark text; interchangeable, but must not be mixed on the same literal. |
| `=` | operator | Assignment — binds a value to a variable name. |
| `==` | operator | Equality comparison — returns `True` or `False`. |
| `+` | operator | Addition (used in `x + y`). |
| `int` | value type | Whole numbers, e.g. `2`. |
| `float` | value type | Fractional/decimal numbers, e.g. `2.1`. |
| `str` | value type | Text created by quoting, e.g. `"2.1"`. |
| `bool` | value type | Logical values `True` / `False`. |
| variable | concept | A named container whose type is set by the value assigned; re-assignable to any type. |
| `pip` / `pip3` | package manager (shell) | Installs Python packages: `pip install pandas`, `pip3 install pandas` (3 = Python 3). |
| `import` | keyword (mentioned) | Required to bring an installed package (e.g. NumPy) into your program. |
| NumPy | package (preview) | Arrays/vectors, matrix multiplication, linear algebra. |
| SciPy | package (preview) | Scientific computing, e.g. curve fitting. |
| Matplotlib | package (preview) | Plotting/visualisation. |
| scikit-learn | package (preview) | Classical machine-learning algorithms. |
| TensorFlow | package (preview) | Deep learning. |
| Jupyter Notebook | tool | Local notebook interface for Python; code + output + plots in one page. |
| Google Colab | tool | Cloud-hosted Jupyter notebook; no installation, runs on Google's server, tied to your Google account. |
| `class` / object | deferred concept | Why `print(type(x))` shows `<class '...'>`; to be taught in class 3–4. |

---

## 5. Syntax rules, common mistakes & debugging tips (explicitly flagged)

1. **Quotes must match** — open and close with the *same* quote character; `"text'` fails.
2. **Quoted digits are strings, not numbers** — `"2.1"` has type `str`, and arithmetic will not behave as you expect.
3. **No type declaration / no type casting** in Python. Convenient, but a **pitfall**: a wrong-typed value is accepted silently and your program may produce nonsense without raising an error.
4. **Only the last assignment survives** — earlier values of a variable are permanently lost; a common source of bugs in long scripts.
5. **Python is case-sensitive** — `x` and `X` are different variables; mismatched case → error.
6. **`=` is not `==`** — assignment vs. comparison.
7. **Python has weak safety handling** → *cross-check every line you write*; don't assume "no error message" means "correct".
8. **Version mismatch**: Python 2 code will not run under Python 3 without syntax fixes (and vice versa).
9. **Use descriptive variable names** so you can trace their purpose 50+ lines later.
10. **Debug by experimenting** — when unsure whether something works, type it into Colab and run it. Consult official package documentation and the internet/GitHub when stuck.

---

## 6. Exam / assignment information mentioned

- **Assessment plan (as stated):**
  - **Two assessments** in this module: **one take-home** and **one in-class problem-solving** assessment.
  - An **assignment set** will be given after roughly **three or four classes**, possibly sooner depending on pace.
- **Do not limit yourself to the assignments** — implement your own ideas to build fluency; practice is the stated key to passing/benefiting.
- **Expectations for next session:**
  - Bring a **computer with Google Colab open** and follow along, typing the examples *simultaneously* with the instructor — "just listening will not help".
  - **Recommended** (not mandatory) to install Python + Jupyter Notebook locally; it will be needed later for ML/DL work.
- The instructor will **upload the Colab notebooks** after class.
- Classes are being held **daily this week**, at 7 or 8 (pm, presumably).
- **Deferred topics to expect:** `class` and objects (≈ class 3–4); NumPy, SciPy, Matplotlib later in Module 1.