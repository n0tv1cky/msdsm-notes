# DSM-102 — Programming Fundamentals for Data Science
## Session 3 — 2026-08-27 (Instructor: Saurabh Das)
### Topic: Control Flow — `if/elif/else`, loops, `break`/`continue`/`pass`, exceptions

---

## 1. Overview

This session moves from "straight-line" programs (the simple arithmetic/area calculations of the previous class) to **control flow**: making a program decide what to do and repeat work automatically. It opens with a short recap of number formatting in `print` (`%f`, `%.2f`, `%d`, `%02d`, `.format()`), then introduces conditional branching (`if` / `elif` / `else`) and stresses Python's **indentation rule** as the mechanism that decides which statements belong to a block. Next come loops: the `for` loop driven by `range()` (including start/stop/step and negative steps), and the `while` loop for cases where the number of iterations is unknown. Loop control keywords `continue`, `break` and `pass` are demonstrated with worked examples (odd numbers from 2–10, factorising 64, nested `i`/`j` loops). The class then covers exception handling with `try` / `except` (`ZeroDivisionError`) and why physically/numerically invalid inputs (negative triangle base, divide by zero) should raise flags rather than silently return wrong answers. An in-class exercise — *print every power of 2 less than 10,000* — is solved, a common off-by-one bug is diagnosed live, and the session closes with a preview of user-defined **functions** (`def`, `return`) and **modules** for the next class.

---

## 2. Topics in order taught

### 2.1 Recap: formatted printing (carry-over from last session)

Four example strings were printed to show the difference between plain text, `%`-formatting, and `.format()`:

```python
string1 = "A: hi"
string2 = "B: %f %s %d" % (3.14159, "hello", 5)
string3 = "C: {}".format(3.14)
string4 = "D: %.2f %s %02d" % (1.0, "hello", 5)

print(string1)
print(string2)
print(string3)
print(string4)
```

> *(Reconstructed: the exact literal values/labels the instructor used were spoken loosely; the formatting specifiers and their behaviour below are what he actually explained.)*

Rules stated:

| Specifier | Meaning | Example result |
|---|---|---|
| `%f` | float; **Python prints 6 decimal places by default** | `3.14159` → `3.141590` |
| `%s` | string / text, printed as is | `hello` → `hello` |
| `%d` | integer — **takes only the integer part**, truncating the fraction | `3.14` → `3` |
| `%.2f` | float forced to **2 decimal places** (the `.` marks the decimal point, `2` = number of decimals) | `1.0` → `1.00` |
| `%02d` | integer padded to **2 characters**, **padded with leading zeros** if shorter | `5` → `05` |
| `"{}".format(x)` | curly-brace placeholder replaced by `x` | `"{}".format(3.14)` → `3.14` |

---

### 2.2 Why we need control flow

* Programs written so far had **no control**: e.g. the triangle-area program would happily accept a **negative base or negative height** and multiply them out, even though a negative base/height is **physically impossible**.
* Goal of control flow: *check* the values first — if a value is negative, raise an error; otherwise compute the area.
* "Control flow" = the algorithm has control/checks over the different paths the program can take.

---

### 2.3 `if` / `elif` / `else`

English form: *"If the base or height is negative, raise an error; if not, calculate the area."*

Python form (demonstrated with three variables):

```python
x = 10
y = 5
z = 3

if x == y:
    print("hello")
elif x == z:
    print("goodbye")
elif x == 1:
    print("something")
else:
    print("?")
```

> *(Reconstructed. The instructor's exact strings/values for the third branch were not clear in the audio; the structure and the traced outputs below are as he described them.)*

Key points:

* `==` is the **comparison** (logical equality) operator — "double equal". (`=` is assignment.)
* The **colon `:` at the end of the condition line is mandatory** — it tells Python "a block follows; do something".
* **Flow rule:** conditions are tested top to bottom; the *first* condition that is satisfied runs its block and **the rest are skipped** — the `if/elif/else` chain stops there. If nothing matches, `else` runs.

Traced outputs:

| Values | Output | Why |
|---|---|---|
| `x=10, y=5, z=3` | `?` | no condition matches → `else` branch |
| `x=10, y=10` | `hello` **only** | first condition true → chain stops, later branches never tested |
| `x=10, z=10` (y ≠ 10) | `goodbye` | first false, second true |

---

### 2.4 Indentation — the big Python pitfall

Indentation is **not cosmetic**; it defines what is inside a block.

```python
if 2 == 3:
    print("this runs")
print("this runs too")
```

* Output: `this runs too` **only**.
* Reason: `print("this runs")` is indented → it belongs to the `if`, and `2 == 3` is false, so it is skipped. `print("this runs too")` starts at the **same alignment as `if`**, so the `if` block has already ended; Python treats it as a separate, always-executed statement.
* Change the condition to `if 2 == 2:` → **both lines** print (the block runs, then the statement after the block runs).
* Common mistake called out: writing the body at the same indentation as the `if` — it will either be an error or, worse, **silently mean something else** (as above).

---

### 2.5 Loops and `range()`

Motivation: so far values were typed in manually and changed by hand. Real work means sweeping over **series of values** — e.g. fetching every element of a table (row 1 col 1, row 1 col 2, …) and adding them up.

**`range()`**
* `range(5)` generates the 5 values `0, 1, 2, 3, 4` (an "array" = a row of numbers) held in memory.
* **Python always starts counting at 0, never 1** — remember this or you will hit many bugs.
* Default step (separation between consecutive values) is **1** unless specified.
* `range` controls *how many times* a piece of code is repeated.

**`for` loop, example 1**

```python
for i in range(5):
    print(i)
```
Output:
```
0
1
2
3
4
```
With `range(10)` → prints 10 elements, `0` through `9`.

**`for` loop, example 2 — start, stop, step (negative step)**

```python
for i in range(10, 2, -2):
    print(i)
```
Output: `10, 8, 6, 4` — starts at 10, decrements by 2, and **stops before 2** (the stop value is not printed).
General form: `range(start, stop, step)`; `range()` can generate essentially any arithmetic series.

---

### 2.6 `while` loops

* Use a **`for` loop when you know how many iterations** you need.
* Use a **`while` loop when you do NOT know the number of iterations** but you have a **condition** that must hold.
* Unlike a `for` loop, you must **initialise the loop variable yourself** before the loop.

Worked example — print all squares less than 100:

```python
i = 1
while i**2 < 100:
    print(i**2)
    i += 1
```

Output: `1, 4, 9, 16, 25, 36, 49, 64, 81`
(The instructor read off `1`, `4`, … `36`, … `64` while tracing.)

* `**` = power operator (`i**2` = i squared).
* `i += 1` is **shorthand for `i = i + 1`** (generally `a += b` ⇔ `a = a + b`).

---

### 2.7 `continue` and `break`

Inside a loop you can put an `if` to stop or skip work once a desired condition is met. Two keywords:

* **`continue`** — skip the *rest of the loop body* for this iteration and jump to the **next iteration**. Does **not** leave the loop.
* **`break`** — **exit the loop immediately**.

**Example A — odd numbers between 2 and 10 (uses `continue` and `%`)**

```python
for num in range(2, 10):
    if num % 2 == 0:
        continue
    print("Found an odd number {}".format(num))
```

* `%` is the **modulo / remainder** operator. `num % 2 == 0` ⇒ even.
* Even numbers hit `continue` and go straight to the next value; odd numbers fall through to the `print`.
* Note: the `print` is **outside** the `if` block (one indentation level back) — the effect of an `else` is achieved purely by indentation.
* Output: the odd numbers **3, 5, 7, 9** (formatted with `.format()` from the previous lecture).

**Example B — first divisor pair of 64 (uses `break`)**

```python
n = 64
for x in range(2, n):
    if n % x == 0:
        print("{} equals {} * {}".format(n, x, n // x))
        break
```

> *(Reconstructed print statement; the instructor described "it is equal to that particular value and the integer division by that thing".)*

* `//` = **integer division**.
* Logic: scan `x` from 2 upward; if `64 % x == 0` then `x` and `64 // x` are a factor pair.
* Because of `break`, only the **first** factor pair is printed (`64 equals 2 * 32`); remove the `break` and you would get all divisors.

---

### 2.8 Nested loops

* `for` and `while` loops can be **mixed and nested** (a loop inside a loop, to any depth).
* Essential when working with **matrices/tables**: outer loop runs over rows, inner loop over columns, so you can address element (row 1, col 2), (row 2, col 1), etc.

```python
for i in range(5):
    for j in range(5):
        print(i, j, end=" ")
        if j == i:
            break
```

> ⚠️ **Reconstructed with low confidence.** The ASR gives the inner condition as "if j == 10" but the traced output he read out (`… 4 0 4 1 4 2 4 3 4 4`) is only consistent with the inner loop running `j = 0 … i` — i.e. a break when `j` reaches `i` (or an inner `range(i+1)`). Treat the *concepts* below as the takeaway, not the literal condition.

Traced output pattern: `0 0 | 1 0 1 1 | 2 0 2 1 2 2 | 3 0 3 1 3 2 3 3 | 4 0 4 1 4 2 4 3 4 4`

Key teaching points:
* **`break` only exits the loop it is written inside** — here the *inner* loop. The outer loop continues with the next `i`. If loops are nested 3–4 deep, `break` leaves only that one level.
* `end=" "` in `print()` replaces the default newline with a space, so values are printed on one line separated by spaces. It is purely cosmetic and has nothing to do with the logic.

---

### 2.9 `pass`

* `pass` is a **placeholder that does nothing**. Used when syntax requires a statement but you have nothing to do in that branch.

```python
if False:
    pass
else:
    print("True")
```

* As written, output is `True` (the `else` branch runs).
* If the condition is changed to `if True:` → **nothing at all is printed**, because the `pass` branch does nothing.

**Summary of the three loop-control keywords (as stated in class):**

| Keyword | Effect |
|---|---|
| `pass` | do nothing; placeholder, typically inside an `if`/`else` you want to leave empty |
| `break` | leave **the loop in which it is written** (innermost containing loop only) |
| `continue` | skip everything below it in the loop body and go back to run the **next iteration** |

---

### 2.10 Exceptions — `try` / `except`

Motivation: situations we do not want to hit — e.g. a negative triangle base/height (*physically* unrealistic) or division by zero (*numerically* unstable/undefined). Rather than returning a wrong answer, the program should **raise a flag/error** to the user.

```python
try:
    print(1 / 0)
except ZeroDivisionError:
    print("You divided by zero!")
```

> *(Reconstructed body; the structure `try: … except ZeroDivisionError: print(...)` is exactly what was described.)*

* `try:` — keyword, needs a **colon**; put the risky code inside.
* `except <ErrorName>:` — runs only if that error occurs inside the `try`.
* Embedding this in your main code means that when the situation arises you get a **flagged exception instead of a silently wrong answer**.

**Student Q&A (important):** *Why is `ZeroDivisionError` written without spaces? Can I write it in my own words?*
* Answer: an exception name is an identifier — it must be a **single word, no spaces**. `ZeroDivisionError` is a **built-in** name with fixed spelling; several exceptions are built in.
* You may also **define your own custom exceptions** — both the built-in names and user-defined ones are allowed.

---

## 3. Worked in-class exercise

> **Problem: "Print every power of 2 less than 10,000."**
> Requirements stated: use a loop (any kind), use a condition, and use loop control to break out.

### 3.1 The (wrong) solution analysed live

```python
i = 0
n = 0
while i <= 10000:
    n = n + 1
    i = 2 ** n
    print(i)
```

* Logic is essentially right: `n` counts the exponent (0, 1, 2, 3, …), `i = 2**n` is the power, and `while` is a good choice because we don't know the iteration count in advance. Since it is a `while` loop, both `i` and `n` must be **initialised before the loop**.
* Output starts correctly: `2, 4, 8, 16, 32, …` but ends with **16384 (= 2^14)**, which is **greater than 10,000** — the program does not stop at 10,000.
* **Diagnosis (given by a student, confirmed by instructor):** the `print` happens *before* the condition is re-tested. After printing 8192 (2^13), the condition `8192 <= 10000` is still true, so the loop increments again, computes 16384 and **prints it**, and only *then* fails the test. The value is already printed by the time the condition becomes false.
* (The instructor noted `<=` vs `<` is **not** the bug here — 16384 is far above 10,000 either way.)

### 3.2 A working fix

```python
i = 0
n = 0
while i <= 10000:
    n = n + 1
    i = 2 ** n
    if i < 10000:
        print(i)
```

* Guard the print with a condition so the over-shooting value is computed but not printed.

### 3.3 Discussion points

* **Q: why not include 2^0?** You *can* — `2**0 = 1`; this version simply starts from `n = 1`. Another student's version started at 0. Starting point is the only difference.
* **"There is nothing called the one good way to write a program."** Several correct variants were posted in chat; every code that produces the correct final result is correct. Programming is an artistic/multi-solution activity.

---

## 4. Preview of next session (functions & modules)

We have been *using* built-in functions all along (`print`, `range`, `.format()`); as scientists we also need to **create our own**. In Python terminology a user-defined function is created with a **definition**, keyword `def`.

**Cooking analogy used:** small jars (onion powder, turmeric, salt) = individual functions → combined into gravy/marination = bigger functions made of functions → the whole spice box = a **module** that stores all the functionality neatly in sections. Functions are the way to **abstract components of a program** and to reuse the same piece of code in different programs.

Form: a function is like a mathematical function — it takes **inputs**, does something, and **returns** a result.

```python
def triangle_area(base, height):
    area = 0.5 * base * height
    return area

print(triangle_area(2, 2))   # -> 2.0
```

> *(Reconstructed: instructor described `def`, function name, arguments (base, height), the body, and `return`; he stated calling it with base = 2 and height = 2 gives area 2.)*

Syntax elements introduced:
* `def name(arg1, arg2):` — define a function; the arguments are the inputs; colon + indented body as usual.
* `return <value>` — hands the value back out of the function so the main program can use it.

Noted limitation to be fixed next class: this function has **no control** — pass it a negative base and it still computes. Next session will put **`if/else` checks, loops and exceptions inside functions** to build more complex, safe functions, and then move on to modules.

---

## 5. Reference list — everything introduced this session

**Keywords**
* `if` — test a condition; run the indented block if true.
* `elif` — "else if"; tested only if all previous conditions failed.
* `else` — runs when no previous condition was satisfied.
* `for` — loop a known number of times over a sequence (e.g. a `range`).
* `while` — loop as long as a condition remains true (unknown iteration count).
* `continue` — skip the remainder of this iteration; go to the next iteration.
* `break` — exit the innermost enclosing loop immediately.
* `pass` — do nothing (placeholder statement).
* `try` — mark a block whose errors you want to catch.
* `except` — handle the specified error raised inside the `try`.
* `def` — (preview) define your own function.
* `return` — (preview) send a value back from a function.

**Built-ins / functions**
* `print(...)` — display output; `end=" "` argument changes the line terminator to a space.
* `range(stop)` / `range(start, stop, step)` — generate an integer sequence; start inclusive, **stop exclusive**, default step 1; step may be negative.
* `"...".format(x, y)` — substitute values into `{}` placeholders in a string.
* `ZeroDivisionError` — built-in exception raised on division by zero.

**Operators**
* `==` — equality test (distinct from `=` assignment).
* `%` — modulo / remainder (`n % 2 == 0` ⇒ even); also the string-formatting operator in `"%d" % x`.
* `//` — integer (floor) division.
* `**` — exponentiation (`2 ** n`).
* `+=` — augmented assignment: `i += 1` ⇔ `i = i + 1`.
* `<`, `<=` — comparison operators used in loop conditions.

**Format specifiers**: `%f`, `%.2f`, `%s`, `%d`, `%02d`, `{}` (see table in §2.1).

---

## 6. Syntax rules, common mistakes & debugging tips called out

1. **Colon `:` is mandatory** at the end of `if` / `elif` / `else` / `for` / `while` / `try` / `except` / `def` lines.
2. **Indentation defines the block.** A line written at the same alignment as the `if`/`for` is *outside* it and will run unconditionally — a silent logic bug, not always an error.
3. **Python indexes/counts from 0**, not 1. `range(5)` = 0,1,2,3,4; `range(10)` ends at 9. Forgetting this causes many bugs.
4. **`range(a, b, s)` never includes the stop value** — `range(10, 2, -2)` stops at 4.
5. In a **`while` loop you must initialise the loop variable yourself** and make sure something inside changes it, or the condition will never become false.
6. **Order of `print` vs. condition test matters** — the powers-of-2 bug: a value can be computed and printed *before* the loop condition gets re-checked. Either guard the print with an `if`, or restructure the loop.
7. **`break` exits only the loop it sits in**, not all enclosing loops.
8. `continue` does not exit the loop — it just skips the statements below it for that pass.
9. Exception names are **single words with no spaces** (`ZeroDivisionError`). You can use built-in ones or define your own.
10. Watch out for physically/numerically invalid inputs (negative lengths, division by zero) — handle them with `if` checks and/or `try`/`except`.

---

## 7. Announcements — exams / assignments / logistics

* **Next class: same time (≈7:00/8:15 pm as usual), next day.** Topic: creating **functions (`def`, `return`)**, then **modules**.
* **An assignment will be shared over the weekend** — but **do not wait for it**: invent your own problems and code them; use the many internet resources; working ahead is "highly appreciated".
* **Saturday: an online mini-assignment / "surprise quiz"** (announced in advance, so "not a surprise any more") — small coding tasks to be done live so the instructor can see how you are doing. Everyone was asked to be OK with this. **Practise before Saturday.**
* **Do NOT use ChatGPT or similar tools** for the coding exercises — stated twice, explicitly ("that is not correct and that should not be done"). Attempt everything yourself; solutions may be shared in the chat window.
* Pace is deliberately slow because many students are new to programming — the emphasis is on **practice**.