# DSM-102 — Programming Fundamentals for Data Science
## Session 2 — 2026-08-26 (Instructor: Saurabh Das)
### Topic: Variables, Data Types, Operators, String Manipulation & Formatting, Intro to Modules

---

## 1. Overview

This session is a hands-on continuation of the introduction to Python, aimed at students with no prior programming background. It begins by revisiting the core philosophy of programming — store data in **named variables** rather than hard-coded values, so the program can be manipulated and reused — and reviews Python's four basic value types (string, float, integer, Boolean). It then covers the ASCII ↔ character conversion functions `ord()` and `chr()`, Python **keywords** (why you must not use them as variable names), the complete set of **arithmetic, comparison and logical operators** (including `//`, `%`, `**`), and how Python **automatically infers and promotes types** (e.g. why `4/2` gives `2.0` and not `2`). Two in-class exercises are done (multiply two numbers; compute the area of a triangle) which lead into a discussion of why some students got `int` results and others got `float`. The second half covers **string manipulation**: concatenation with `+`, `.lower()`, `.upper()`, `.replace()`, f-strings, `%`-style formatting (`%s`, `%d`, `%f`), `.format()`, and using `?` in Colab to pull up a function's docstring/help. The session closes by motivating **modules** — Python doesn't know `pi` by itself, so you must `import math` and use `math.pi` — with a preview of NumPy/SciPy and user-written modules for the next class.

---

## 2. Topics & Concepts in Order of Teaching

### 2.1 Recap: Why variables?
- A program = objects called **variables**, which you name (name is up to the user/coder) and to which you **assign values**.
- Reason to use variables instead of literal values: easier to manipulate throughout the program; **avoid hard-coding** numbers; the variable can adapt and change value as the situation demands.
- Syntax: `variable_name = value` (a name, an `=` sign, a value).
- Values can come from the user, from another computation, or be given directly.

**Worked example (recap from last session):**
```python
x = 10
y = 5
sum_xy = x + y
print(sum_xy)      # 15
```
- `print()` — built-in function that takes a variable (or value) and displays its value.

### 2.2 The four basic types
| Type | Description | Example |
|---|---|---|
| `str` (string) | Text. **Anything inside quotes** is stored as-is and is *not* manipulated mathematically. | `x = "hello"` |
| `float` | Fractional / decimal numbers. | `x = 2.5` |
| `int` | Whole numbers. | `x = 10` |
| `bool` | Result of comparisons: `True` / `False`. | `a == b` |

- **Key point (vs. C/Java):** you do **not** pre-declare the type. Python assigns the type automatically from the value you give. Assign `10` → `int`; assign `10.0` → `float`; assign `"10"` → `str`.
- `type(x)` — built-in that reports the current type of a variable.

### 2.3 Characters and ASCII — `ord()` and `chr()`
- Computers never work with alphabets directly; they work with **binary numbers (0/1)**. Every character has a numeric (ASCII) code.
- `ord(ch)` — built-in function: returns the ASCII/Unicode code point of a character.
- `chr(n)` — built-in function: returns the character corresponding to code `n`.

```python
ord('a')          # 97
chr(97)           # 'a'
'a' == chr(97)    # True
ord('A')          # 65
'A' == chr(65)    # True
```
- Note: `'a'` and `'A'` are **distinct** in ASCII space, so `'a' == 'A'` → `False`.
- Practical note: you normally don't need to work in ASCII space — `ord()`/`chr()` convert for you when required.

### 2.4 Keywords (reserved words)
- **You cannot name a variable `chr`, `print`, `f`, etc.** Keywords have a fixed, pre-defined meaning in the language.
- Instructor stated: **"Python has 29 keywords"** that cannot be used as variable names. *(Note: modern Python 3 actually has 35 keywords — treat 29 as the figure quoted in the lecture; you can verify with `import keyword; print(keyword.kwlist)`.)*
- Function names (like `chr`, `print`) are *technically* usable as variable names but **will create conflicts** — never do it.

**Keywords explicitly named and explained:**
| Keyword | One-line meaning |
|---|---|
| `True` / `False` | Boolean literals — the two outcomes of a Boolean operation. |
| `def` | Short for "definition" — used to define/create a new function. |
| `for` | Used to run a loop. |
| `return` | Returns a value from a function back to the calling (main) program. |
| `is` | Checks identity / whether something is the case (`is True`, `is False`). |
| `in` | Specifies the range/collection over which a loop works (membership). |
| `class` | Defines the structure of a class. |
| `and`, `or`, `not` | Logical operators (see §2.6). |
| `import` | Brings in a module (see §2.11). |

### 2.5 Two programming conventions to always follow
1. **Prefer variables over raw values.** Manipulate variables, not numbers; values update automatically per the program's rules.
2. **Use meaningful variable names** so that you (later) and teammates can understand the code just by reading it.

### 2.6 Operators

**Arithmetic:**
| Operator | Meaning | Example from class |
|---|---|---|
| `+` | Addition | `x + y` |
| `-` | Subtraction | |
| `*` | Multiplication | |
| `/` | Division (true division) | `5/2 → 2.5` |
| `//` | Floor / integer division — returns only the integer (floor) part | `4//2 → 2` |
| `%` | Modulo — remainder of integer division | `5 % 3 → 2` |
| `**` | Exponentiation ("powering up") | `4 ** 3 → 64` |

> Instructor's caution: `%` (modulo/remainder) was described as an **integer-only** operation, unlike `+ - * / **` which also work on floats. *(In real Python `%` does work on floats too, e.g. `5.5 % 2` → `1.5`; note the lecture's stricter statement, but be aware of the actual behaviour.)*

**Comparison (yield `True`/`False`):**
- `=` → **assignment** (single equals puts a value into a variable)
- `==` → **comparison** (double equals tests equality) ← *classic beginner mistake to confuse these two*
- `!=` → "does not equal"
- `>`, `<`, `>=`, `<=`

**Logical:**
- `and` — **all** the listed conditions must be satisfied to proceed.
  - Example form given: `5 == a and c == d` (both sides must be true)
- `or` — **any one** of the conditions being true is enough.
- `not` — negates; proceeds only if the condition is *not* true.
- The keywords `True` / `False` can be used directly in such expressions.

### 2.7 In-class exercises

**Exercise 1 — multiply two numbers** (posted answers in chat; ~50% responded)
```python
a = 4
b = 7
product = a * b
print(product)      # 28    (values chosen by each student)
```

**Exercise 2 — area of a triangle**
- Formula stated: **Area = ½ × base × height**
```python
base = 10
height = 5
area = 0.5 * base * height
print(area)         # 25.0
print(type(area))   # <class 'float'>
```
- Related point: area of a **rectangle** = length × height; halve it to get the triangle's area.

**Discussion that followed — why did some students get `25` (int) and others `25.0` (float)?**
- If **any** operand in the expression is a float (e.g. writing `0.5`), the whole result is promoted to **float**.
- If you write it as `base * height / 2`, the `/` makes it a float anyway.
- If **all** operands are integers *and* the operation yields an integer, the result stays `int`.
- `25` and `25.0` are **numerically identical**; only the *type* differs.
- This is called out as "the beauty of Python" — you don't have to manage types manually.

### 2.8 Reassignment and variable-name case sensitivity

```python
a = 2
b = 5
print(a == b)   # False  -- values differ
print(a, b)     # 2 5    -- comma prints multiple variables in one command
b = 5
a = b           # a now takes the VALUE of b
print(a)        # 5
```
- Syntax point: **`print(a, b)`** — separate multiple items with a comma to print them in one command.
- Semantics: `a = b` does **not** make `a` become `b`; it copies `b`'s *value* into `a`.
- Instructor flagged that Python has some **intricacies in how reassignment/copying really works** (mutable objects / references) — "we will come to that later".

```python
print(A)        # ERROR -- capital A was never defined
```
- **Python is case-sensitive**: `a` and `A` are different variables. Referring to an undefined variable raises an error (`NameError`).

### 2.9 Division / type traces done live
```python
5 / 2            # 2.5
4 / 2            # 2.0     <- true division ALWAYS returns float
type(4 / 2)      # float
4 // 2.1         # 1.0     <- floor division, but float because 2.1 is a float
4 // 2           # 2
type(4 // 2)     # int
5 % 3            # 2       <- remainder: 3 goes into 5 once, remainder 2
4 ** 3           # 64
4 ** 3.0         # 64.0    <- one float operand forces a float result
```
**Rule distilled:** any operation involving at least one `float` produces a `float`. All-`int` operands with an integer-valued result stay `int` — *except* `/`, which always gives `float` (because the answer may be fractional). `float` is "more versatile" — it carries an integer part *and* a fractional part.

### 2.10 Boolean examples traced live
```python
5 == 5           # True
5 == 5.0         # True    <- numeric VALUE matters, type does not
not 5 == 5       # False
5 != 5.0         # False   <- equivalent to the line above
True and True    # True
True and False   # False
True or False    # True
not True         # False
```
- Motivation given: when you have many conditions, `and` checks that **all** hold simultaneously, `or` checks whether **any** holds, `not` checks that a condition does **not** hold. Fuller examples will come when longer programs (with `if`/loops) are written.

### 2.11 String manipulation

**Case conversion methods (called with the dot operator):**
```python
'A'.lower()              # 'a'
'a'.lower() == 'a'       # True
'a'.upper()              # 'A'
```

**Syntax rule emphasised (very important):**
- The text goes inside quotes; then a **dot**; then the **method name with parentheses** — and the method name must **NOT** be inside the quotes.
- If you write `"a.lower()"` (everything inside quotes), Python treats the **entire thing as plain text**, not a function call, so a comparison like `"a.lower()" == 'a'` returns **False**.
- General rule: *anything in quotes is a string and is never manipulated; anything that is a function/method is written bare, without quotes.*
- Instructor: "Till now I keep saying Python syntax is flexible — but there ARE rules, and you must be careful about them."

**Concatenation with `+`:**
```python
string1 = "hello"
string2 = "world"
string3 = string1 + string2
print(string3)            # helloworld
```
- `+` on strings does **not** add ASCII values — it **concatenates** (joins) the text.
- You can chain as many strings as you like:
```python
string4 = string3 + "b"   # (variable name inferred; instructor added a further text "b")
print(string4)            # helloworldb
```
- *Why it matters:* building output messages such as `"<name> has age of 43"` where the name/number change per record.

**f-strings (formatted string literals):**
```python
x = 23
y = 52
name = "Alice"
string1 = f"{name} numbers are {x} and {y} and their sum is {x + y}"
print(string1)
# Alice numbers are 23 and 52 and their sum is 75
```
- `f` before the opening quote = "format". **Do not use `f` as a variable name** — it will create conflict.
- Whatever is inside `{ }` (curly braces) is treated as a **variable/expression and evaluated**; everything else inside the quotes is literal text.
- If you drop the braces, e.g. `f"... their sum is x + y"`, the output literally prints `x + y` — no evaluation.
- `type(string1)` → **`str`**: the final result is pure text and cannot be manipulated numerically any more, even though the numbers *inside* it were computed before being inserted.

**`%`-style formatting with `print()`** (used when you want explicit control over the output format):
| Specifier | Means |
|---|---|
| `%s` | string |
| `%d` | integer |
| `%f` | float |

```python
print("A is %s" % ("hi"))
# A is hi

print("B is %f %s %d" % (1.0, "hello", 5.2))
# B is 1.000000 hello 5     <- 5.2 forced to %d prints only the integer part
```
*(Exact wording of the literal text portions is inferred; the specifiers, the `%` separator and the tuple of values are as demonstrated.)*
- Structure: `"literal text %spec more text" % (value1, value2, ...)` — the `%` sign after the closing quote separates the format template from the values supplied.

**`.format()` method:**
```python
print("C is {}".format(3.14))
# C is 3.14
```
*(Reconstructed — the instructor said the third example used no type specifier inside, and that `3.14` was supplied via the `.format()` method.)*

**Student Q&A — controlling number of decimal places:**
> *Q: For something like 22/7, how do we set the number of digits after the decimal?*
> A: Specify it in the format itself — instead of a plain `%f`, write the precision, e.g. `%.7f`, `%.8f`, to get that many decimal digits.

**Whole-string case conversion:**
```python
s = "Hello World"
print(s)            # Hello World  (original, mixed case)
print(s.upper())    # HELLO WORLD
print(s.lower())    # hello world
```

**`.replace()`:**
```python
string1 = "hello world"
string1.replace('l', 'k')     # 'hekko workd'
```
- `.replace(old, new)` — returns a new string with **every** occurrence of `old` swapped for `new`.

### 2.12 Getting help inside Colab/Jupyter — the `?` operator
```python
string1.replace?
'a'.lower?
```
- Appending `?` to a function/method name opens a help pane showing the **signature, usage and docstring** (the description of what the function does).
- Instructor's tip: *"No one knows everything in Python; new packages and functionality come out every day."* If you forget how a function works or you're using a new package, use `name?` — you don't need to leave the notebook and Google it.

### 2.13 Modules (preview of the next session)
- Everything used so far (`print`, `type`, `ord`, `chr`, `.upper()`, …) is a **built-in** — always available with no setup.
- **Motivating problem:** area of a circle = **π r²**. You can supply `r`, but writing `pi` alone gives an **error** — Python does not know `pi` by default.
- Constants (π, speed of light, …) and advanced functions live in **modules**.
- Importing:
```python
import math
print(math.pi)      # 3.141592653589793
area = math.pi * r**2   # (r must be defined)
```
- Syntax: `import <module_name>`; then access its contents as `module.thing`.
- Other modules named for later: **NumPy**, **SciPy** (mentioned on day 1).

**Student Q&A — "How big is a module? Does `math` contain everything mathematical?"**
- No. A module carries only *some* basic/related functionality. If what you need isn't there, you import a different module; if it doesn't exist anywhere, **you write your own module** (this will be taught later).
- **Analogy used:** a module is like a *book*. Different books for different subjects; even within one subject you may need several books, because each carries different things. This is how Python's functionality is organised.

---

## 3. Functions / Keywords / Operators Introduced — quick reference

| Item | One-line explanation |
|---|---|
| `print()` | Displays the value of a variable/expression; multiple items separated by commas. |
| `type()` | Returns the data type of a variable (`int`, `float`, `str`, `bool`). |
| `ord(ch)` | Returns the ASCII/Unicode code of a single character (`ord('a')` → 97). |
| `chr(n)` | Returns the character for an ASCII/Unicode code (`chr(97)` → `'a'`). |
| `.lower()` | String method — converts to lowercase. |
| `.upper()` | String method — converts to uppercase. |
| `.replace(old, new)` | String method — replaces every occurrence of `old` with `new`, returns a new string. |
| `.format(...)` | String method — substitutes values into `{}` placeholders. |
| `f"..."` | f-string; `{}` inside are evaluated as variables/expressions. |
| `%s`, `%d`, `%f` | Format specifiers for string / integer / float in `%`-style formatting; precision as `%.Nf`. |
| `import` | Keyword to load a module (`import math`). |
| `math.pi` | The constant π provided by the `math` module. |
| `name?` | (Colab/IPython) opens help/docstring for that function or method. |
| `=` | Assignment operator. |
| `==`, `!=`, `>`, `<`, `>=`, `<=` | Comparison operators → return `True`/`False`. |
| `+ - * /` | Add, subtract, multiply, divide (`/` always returns float). |
| `//` | Floor (integer) division. |
| `%` | Modulo — remainder of division. |
| `**` | Exponentiation. |
| `and`, `or`, `not` | Logical AND (all true), OR (any true), NOT (negation). |
| `True`, `False` | Boolean literals/keywords. |
| `def`, `for`, `return`, `is`, `in`, `class` | Keywords named for later sessions (function definition, loops, returning values, identity check, membership/range, class definition). |

---

## 4. Syntax Rules, Common Mistakes & Debugging Tips Called Out

- **`=` vs `==`**: single `=` assigns a value to a variable; double `==` compares two things and returns `True`/`False`.
- **Python is case-sensitive**: `a` ≠ `A`. Using an undefined name (e.g. `print(A)` when only `a` exists) always throws an error — check spelling/case first when debugging.
- **Never use a keyword as a variable name** (29 reserved keywords per the lecture). Avoid also using built-in function names (`chr`, `print`) or the format prefix `f` — legal but causes conflicts.
- **Method-call syntax**: `"text".method()` — the dot and the method name must be **outside** the quotes. Putting them inside (`"a.lower()"`) makes the whole thing a literal string, silently producing wrong results (e.g. a comparison returning `False` instead of `True`).
- **Quotes rule**: anything in quotes = string, never evaluated. Anything meant as a function/method/variable = written without quotes.
- **f-string braces**: forgetting `{}` around a variable prints the variable *name* as text instead of its value.
- **Type promotion**: mixing a float into any arithmetic makes the result a float; `/` always produces a float. `25` and `25.0` are numerically the same — don't panic if your output "type" differs from a classmate's.
- **`%d` truncates**: forcing a float like `5.2` through `%d` prints only the integer part (`5`).
- **Use `?`** on any function/method to read its docstring without leaving the notebook — the primary debugging/learning aid recommended.
- Instructor's stated (lecture-level) restriction: `%` (mod) is for integers; the other arithmetic operators work with floats as well.

---

## 5. Housekeeping / Exam & Assignment Notes

- No graded assessment was announced in this session. The only explicit "flags":
  - **Practice is mandatory for mastery** — the instructor repeatedly urged students to type and run each example *live, alongside him*, rather than waiting for the uploaded notebook. "Unless you exercise, unless you practice, you'll not be able to get mastery over this."
  - **"Play with the data / play with the formats"** — experiment with precision specifiers, types and string methods on your own.
  - In-class chat exercises (multiply two numbers; area of a triangle) were participation checks, not graded.
- **The Google Colab notebook used in class will be uploaded to the LMS portal** within a day or two.
- **Next session (tomorrow, ~7:00 p.m.):** modules in detail — what the important modules are (`math`, NumPy, SciPy…), how to import them, and later, how to write your own module.
- Environment: Google Colab is fine; a local desktop Python environment is equally acceptable.