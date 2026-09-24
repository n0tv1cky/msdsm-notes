# DSM-102 — Programming Fundamentals for Data Science
## Session 4 — 2026-08-28 — Instructor: Saurabh Das
### Topic: User-Defined Functions in Python (definition, return vs print, scope, recursion, arguments)

---

## 1. Overview

This session is a deep dive into **user-defined functions in Python**, building on the previous lecture's coverage of loops, `if/else` conditions, and loop control (`break`, `continue`, `pass`). The instructor starts by recapping that we have already been *using* built-in functions like `print()`, and then shows how to write our own using the `def` keyword. Core themes covered: how to define a function with a name and arguments; why meaningful names matter for collaboration; embedding validation/exception logic (`raise ValueError`) inside a function; the crucial distinction between **`print` (displays only, nothing stored)** and **`return` (hands a value back to the program for further manipulation)**; local vs. global variables and the `global` keyword; passing functions as arguments to other functions; recursion (illustrated with factorial, compared side-by-side against a `while`-loop factorial); the dummy variable `_` for loops where the counter is irrelevant; and finally keyword arguments with default values. The class ends with a warning that a **surprise in-class live-coding quiz** may happen the next session.

---

## 2. Topics & Concepts, in Order Taught

### 2.1 Recap of previous session
- Loops for handling many values/inputs.
- `if` conditions to control output of a function/program.
- Loop control: `break` (exit loop), `continue` (skip to next iteration), `pass` (do nothing / placeholder).
- Functions were introduced at the end of last class.

### 2.2 What a function is / why use it
- A function is a way to **abstract a big program into small chunks**.
- Once defined, a function can be **called any number of times**.
- `print()` is itself a function that is already defined (built-in) — that's why "the program knows how to print".
- **Naming rule of thumb:** the name is up to the user; there is no strict rule, but *give meaningful names*, because you will collaborate and others will reuse your function.

### 2.3 Syntax of a function definition
Structure taught:
```
def function_name(argument1, argument2):
    # body: whatever the function has to do
    return value
```
- Keyword: `def`
- Then the **name** (this is what you call later).
- Then **input arguments inside parentheses**.
- Then the body (indented).
- `return` sends the value out.

### 2.4 Worked Example 1 — Triangle area (basic version)

> *Reconstructed from the spoken walkthrough; the formula `0.5 * base * height` and the return statement are explicitly stated, variable names `base`, `height` are as spoken.*

```python
def triangle_area(base, height):
    area = 0.5 * base * height
    return area
```
- **Formula used:** `area = 0.5 × base × height`
- Problem identified: this will happily accept a negative base/height and return a value. **An area cannot be negative.** So the function has no control over bad input.

### 2.5 Worked Example 2 — Triangle area with validation (`raise ValueError`)

> *Reconstructed; the error message text "base and height must be non-negative" was spoken verbatim.*

```python
def triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("base and height must be non-negative")
    else:
        return 0.5 * base * height
```
Calling it with a negative value, e.g. `triangle_area(-1, 5)`, raises:
```
ValueError: base and height must be non-negative
```
Key points made:
- `ValueError` is a **built-in** — so you are calling a built-in inside your own custom function.
- This is a form of **exception handling specific to this program** (general exception handling was covered earlier).
- **Why this matters:** in a long program made of many small functions, having exceptions built into each specific function tells you **exactly which part of the code the problem occurred in**.

### 2.6 Worked Example 3 — A function that "does nothing" / returning multiple values

```python
def simple(a, b):
    return a, b
```
Calling `simple(1, 2)` gives:
```
(1, 2)
```
Discussion (student question about the brackets):
- The student asked: "there were no brackets, we wrote `return a, b` — why does the output show brackets?"
- **Answer:** because you haven't told Python *how* to treat/unpack it, so it comes back as a **single grouped object** (instructor called it "a single array"; in Python this is actually a **tuple**). Output is a single combined object unless you explicitly assign individual variables.
- **Follow-up:** if after calling you ask for the value of `a` → **you get an error / `a` is not defined.** `a` and `b` exist **only inside the function**. → This is the **local variable** concept.
- **Positional arguments:** the function assigns by position — 1st value → first parameter, 2nd value → second parameter — and only *inside* the function.

### 2.7 Worked Example 4 — `loop1()`: print vs return inside a loop

> *Reconstructed from the spoken trace; the function name `loop1`, `range(10)`, and condition `x == 3` are as spoken.*

```python
def loop1():
    for x in range(10):
        print(x)
        if x == 3:
            return x
```
Trace of behaviour:
- `range(10)` → values **0 to 9**.
- Prints 0, then 1, then 2, then 3.
- At `x == 3` the `if` condition is satisfied → `return x` → the loop **stops immediately** and the function exits.
- Output on screen when you just call `loop1()`: `0 1 2 3` (printed) **and** `3` (the returned value echoed by the interpreter).

**Then the key demonstration:**
```python
y = loop1()
print(y)
```
- Screen shows `0 1 2 3` (from `print` inside the function) — but the extra `3` does **not** appear as a value.
- `print(y)` → `3`
- **Explanation given:** the `print()` inside the function only pushed text to the display; nothing is stored. The `return`ed `x` is the only thing that survives, and it has been stored in `y`. Only `y` (= 3) is **available for manipulation in the rest of the program.**

> Student's follow-up understanding, confirmed correct by instructor: if 3 was returned and stored, then something like `y + 6` would give `9`, because the value is genuinely available.

Contrast made with a simpler function that only does `for x in range(10): print(x)` — that one has **no** value available to the outside world at all.

### 2.8 **KEY CONCEPT — `print` vs `return`**
| `print()` | `return` |
|---|---|
| Only **displays** on screen | **Hands a value back** to the caller |
| Value is **not stored anywhere** | Value can be stored in a variable |
| **Not available** for later manipulation | **Available** for manipulation by the rest of the program / other functions |
| Useful for checking whether your function works (for *our* sake) | This is what the program actually "knows" |

- Instructor's summary: *"function by default does not do anything. The `return` is what actually dictates what output you will get."* Whatever you do inside the function, unless you return the desired value, **you get no usable output**.

### 2.9 Class exercise — two small functions
**Task 1 (static):** write a function that always prints `Hello World`.
**Task 2 (parameterised):** write a function that takes a variable `name` and prints/returns `Hello <name>` (e.g. `hello_name("Subroto")` → `Hello Subroto`).

Reconstructed solutions consistent with the discussion:
```python
# Task 1 – no arguments needed, output never changes
def hello_world():
    print("Hello World")

hello_world()        # -> Hello World
```
```python
# Task 2 – takes an argument
def hello_name(name):
    return "Hello " + name

hello_name("Subroto")   # -> 'Hello Subroto'
hello_name()            # -> ERROR: missing required argument
```
Points made:
- Task 1 needs **no arguments/parameters in the brackets** because the output does not depend on any input — instructor called it "void". Calling `hello_world()` with some extra variable produces no meaningful output / it just does its fixed thing.
- Task 2 **must** declare the argument, because we want to manipulate an input. Calling it **without** an argument → **error**, since the function is expecting an argument inside the brackets.
- When you must manipulate input, you must tell the function **explicitly what kind and how many inputs you expect.**
- Version that only `print`s ⇒ nothing available to the program. Version that `return`s ⇒ available:
```python
x = hello_name("Subroto")
x          # -> 'Hello Subroto'  (now available for further use)
```

### 2.10 Text concatenation with `+` (student question)
- Two strings joined with `+` are **concatenated**: `"Hello " + name` → `Hello Subroto`.
- No special formatting needed for this simple case. (Instructor noted this was covered in the very first class.)

### 2.11 Everything in Python is an **object**
- Text, numbers, and **even functions** are objects.
- Any object can be **passed into a function as an argument**.
- Terminology: whatever sits inside the parentheses is the **argument**; the first part is the **function**; the function may **return** a value as its output.

### 2.12 Worked Example 5 — Passing a function as an argument

> *Reconstructed; the arithmetic (`x+2`, calling `f(f(x))`, result 7 from input 3) is as spoken. Exact parameter names inferred.*

```python
def f(x):
    return x + 2

def twice(f, x):
    return f(f(x))

twice(f, 3)     # -> 7
```
Trace:
- Input `x = 3` → inner `f(3)` = **5** → outer `f(5)` = **7**.
- General result: `f(f(x)) = (x + 2) + 2 = x + 4`.
- Instructor: "this is a bit complicated to understand but it is very useful."
- Motivating use case mentioned: **factorisation / factorial-style problems** where you call a routine repeatedly (divide successively to find all factors).

### 2.13 Worked Example 6 — Returning multiple values into multiple variables

> *Reconstructed. The instructor said the function adds/returns 1, 2, 3 and four numbers, stored into a, b, c, d, with output 1 2 3 4.*

```python
def simple1():
    return 1, 2, 3, 4

a, b, c, d = simple1()
print(a, b, c, d)     # -> 1 2 3 4
```
- Because four numbers are returned, you need **four variables** to store them individually.
- Alternatively you can store them **all in one variable as a single array/tuple**.
- Afterwards `a`, `b`, `c`, `d` hold 1, 2, 3, 4 and are available to the rest of the program.

### 2.14 Recursion — the function calls itself

**Definition given:** In earlier examples we defined one function and called it *inside another* function. In a **recursive function**, the function calls **itself** before returning its value.

**Factorial definition stated in class:**
```
factorial(x) = x × (x-1) × (x-2) × (x-3) × ... × 1
```

**Recursive factorial (reconstructed):**
```python
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

factorial(4)     # -> 24
```
Trace given in class: `4 × 3 × 2 × 1 = 24`.
- Base case: `factorial(1) = 1`.
- Otherwise multiply `x` by the factorial of `x - 1`.
- "Remember `x` is just a variable — **the position of the variable is what is important**."
- A single function generates the factorial by calling itself "again and again until `x` becomes 1" — **no explicit loop used**.

### 2.15 Exercise + Worked Example 7 — Factorial **without** a function, using a `while` loop
Students were given ~5 minutes; the instructor then gave the solution.

> *Reconstructed. Instructor states `num = 4`, `factorial = 1`, a negative check, `factorial *= num`, decrementing num, loop condition spoken as "num greater than equal to zero", result 24. Note: as literally spoken the condition `num >= 0` would multiply by 0 and give 0 — the correct condition is `num > 0`; this is almost certainly an ASR/verbal slip. The corrected version is shown, with the spoken version noted.*

```python
num = 4
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    while num > 0:            # instructor said "as long as num >= 0"
        factorial *= num      # same as: factorial = factorial * num
        num -= 1              # decrement: 4 -> 3 -> 2 -> 1 -> 0, then stop
    print(factorial)          # -> 24
```
Steps as described:
1. Fix the number (`num = 4`) since no function argument is used.
2. Initialise an accumulator `factorial = 1`.
3. Check for negative input → factorial not available → raise/print an exception message.
4. Otherwise loop while `num` is positive: multiply the accumulator by `num`, then **decrement** `num`.
5. Loop stops once `num` becomes 0/negative.
6. Print `factorial` → **24** (same answer as the recursive version).

**Shorthand introduced:** `factorial *= num` is short for `factorial = factorial * num`.

### 2.16 Loop vs Recursion — efficiency discussion
- **Benefit of the functional/recursive form:** you don't have to go inside the code and edit it; just change the input argument `x` and you get any factorial.
- The recursive version still "loops" internally, but not as a `while` loop — it calls itself.
- **Performance claim made:** for long ranges, a loop that iterates many times makes programs **very slow**; the functional form is "much faster to handle this kind of situation."
- **Instructor's caveat:** *"Writing a program is always an art, not a science."* Whatever solution works is correct, but some are more efficient. **A loop is sometimes unavoidable but not always preferable** because of run time.

### 2.17 Local vs Global variables

**Local variable:** a variable used inside a function, from the point it's defined. It has **no bearing on anything outside** the function. You can safely reuse the same name inside and outside for different purposes — **they will not conflict**.

**Worked Example 8 — demonstrating locality**

> *Reconstructed. Instructor states x = 2 outside, a function that adds 1 to x and returns it, output stored in y becomes 5, and x outside remains 2. The exact internal arithmetic producing 5 was not fully spelled out; the "+1 used multiple times" is inferred. Treat the internal body as illustrative.*

```python
x = 2
x1 = 4

def add_stuff(x):
    x = x + 1
    x = x + 1
    x = x + 1
    return x

print(x)             # -> 2   (value before calling)
y = add_stuff(x1)    # inside, x is local
print(y)             # -> 5
print(x)             # -> 2   (UNCHANGED - local work has no effect outside)
```
Key takeaways:
- Whatever manipulation happened **inside** the function does **not** change the outer `x`. Outer `x` still = 2.
- The result lives in the **new variable `y`**, not in the outer `x`.

**Worked Example 9 — the classic scope error**

> *Reconstructed; the error message text was read out by the instructor.*

```python
x = 0

def increment():
    x = x + 1
    print(x)

increment()
```
→ Error:
```
UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
```
**Why:** even though `x = 0` exists in the main program, the function **was not given `x` as an argument**, so *this function does not know what `x` is*. Checking `x` outside still shows `0`.
**Rule stated:** *"You need to give the function all the required values of a variable, otherwise your function will not work irrespective of whether that variable is available outside."*

**Worked Example 10 — the `global` keyword (the workaround)**
```python
x = 0

def increment():
    global x
    x = x + 1
    print(x)

increment()    # -> 1
```
- `global x` declares that the `x` of the main program is also available inside the function.
- Now the function works without being passed `x` explicitly.
- **Strong warning given:** the instructor "would not normally recommend" this unless you are very sure what you are doing — it can **randomly pick up some value from the main program and you may lose control over your program's functionality**. Use with care to avoid conflicts.

**Summary table:**
| Local variable | Global variable |
|---|---|
| Exists only inside the function | Available to both the function and the main program |
| No bearing on the outside world | Function will take the main program's value |
| Safe, no name conflicts | Risky — use with care |

### 2.18 The dummy variable `_` in iteration
- Often we write `for i in range(...)` or `for x in range(...)` but the **loop counter is never used** — it's redundant.
- In that case use an **underscore `_`** as the loop variable. The loop still runs, but we don't care about the variable.

**Worked Example 11 — repeated application using a dummy variable**

> *Reconstructed. Instructor describes `def` with three inputs `f`, `x`, `n`, `for _ in range(n)`, `x = f(x)`, `print(x)`, `return x`, with `f` being the earlier `x+2` function, starting x = 1 and outputs 3, 5, 7, 9, 11, returning 11 (so n = 5).*

```python
def apply_n_times(f, x, n):
    for _ in range(n):
        x = f(x)
        print(x)
    return x

apply_n_times(f, 1, 5)
```
Trace (with `f(x) = x + 2`, starting `x = 1`):
```
3
5
7
9
11
```
Returned value: **11**
- What matters: the function `f`, the starting value `x`, and **how many times** the loop runs (`n`).
- What does **not** matter: the loop counter itself → hence `_`.
- `_` can be used **inside or outside** functions — it's not restricted to the functional form.

### 2.19 Keyword arguments & default values
Motivation: sometimes we don't know how many input arguments will be supplied, or we want an argument to be optional.

**Worked Example 12 — default argument**

> *Reconstructed. Instructor states two parameters `name` and `message`, default message "Good morning", output format "Hello <name>, <message>", with examples giving "Hello Alpura, Good morning" and "Hello Ravi, How do you do?".*

```python
def greet(name, message="Good morning"):
    print("Hello " + name + ", " + message)

greet("Alpura")                        # -> Hello Alpura, Good morning
greet("Ravi", "How do you do?")        # -> Hello Ravi, How do you do?
```
- `message="Good morning"` is the **default value**. If the caller omits `message`, the function still works because the program knows the second value has a default.
- If the caller supplies both, **both** the name and the message change.
- This is the **keyword-argument pair** in a function.
- **Next class preview:** more on flexible numbers of inputs and different ways of passing information into a function.

---

## 3. Full list of functions / keywords / operators / built-ins introduced

| Item | One-line explanation |
|---|---|
| `def` | Keyword that begins a function definition. |
| `return` | Sends a value out of the function so it can be stored and manipulated; without it the function gives no usable output. |
| `print()` | Built-in that only **displays** to screen; stores nothing, returns nothing usable. |
| `raise` | Keyword used to deliberately trigger an exception from inside your code. |
| `ValueError` | Built-in exception type, raised here for invalid (negative) input. |
| `if` / `else` | Conditional branching, used here for input validation and recursion base cases. |
| `for` | Loop over a sequence, e.g. `for x in range(10):`. |
| `while` | Loop that repeats as long as a condition holds (used in the loop-based factorial). |
| `range(n)` | Built-in producing values `0` to `n-1`; `range(10)` → 0…9. |
| `in` | Membership/iteration keyword used in `for x in range(...)`. |
| `global` | Declares that a variable inside a function refers to the main-program (global) variable. |
| `_` (underscore) | Conventional **dummy variable** for loops where the counter is never used. |
| `==` | Equality comparison, e.g. `if x == 3:`. |
| `<` | Less-than comparison, e.g. `if base < 0:` / `if num < 0:`. |
| `>` / `>=` | Greater-than / greater-or-equal, used in the `while` loop condition. |
| `+` | Addition for numbers; **concatenation** for strings (`"Hello " + name`). |
| `*` | Multiplication (`0.5 * base * height`, `x * factorial(x-1)`). |
| `*=` | Compound assignment: `factorial *= num` ≡ `factorial = factorial * num`. |
| `-=` | Compound assignment for decrementing: `num -= 1`. |
| `or` | Logical OR used in the validation condition. |
| `break` / `continue` / `pass` | (Recap) exit loop / skip to next iteration / do nothing placeholder. |
| Argument | Whatever is passed inside the function's parentheses. |
| Parameter with default | e.g. `message="Good morning"` — makes that argument optional. |
| Recursion | A function calling itself, with a base case to stop. |
| Object | In Python everything (text, numbers, functions) is an object and can be passed to a function. |

---

## 4. Syntax rules, common mistakes & debugging tips called out

- **A function does nothing useful without `return`.** Printing inside a function is for *your* verification only; the program can't use printed text.
- **Store the return value**: `y = loop1()` — otherwise the returned value is lost.
- **Local variables are invisible outside the function.** Asking for `a` after `simple(1,2)` gives "not defined."
- **`UnboundLocalError: cannot access local variable 'x' where it is not associated with a value`** — happens when a function uses a variable it was never passed and never defined locally. Fix: pass it as an argument (preferred) or declare `global x` (use with caution).
- **A function that expects an argument will error if called with none** (e.g. `hello_name()`).
- **A function that takes no parameters ignores/rejects extra input** — define parameters only when the output depends on input.
- **Arguments are matched by position**: first value → first parameter, second → second.
- **`return a, b` returns a single grouped object (tuple), not two loose values** — unpack it into separate variables if you want them separately.
- **Multiple return values need matching variables**: four returned numbers → four variables, or store them all as one array.
- **Always validate inputs inside a function** (e.g. reject negative base/height, negative factorial input) so that when a big program breaks, you know *which small function* failed.
- **Use meaningful function names** — others will read and reuse your code.
- **`global` is discouraged** unless you're certain — it can silently pick up values from the main program and you lose control.
- **Recursion needs a base case** (`if x == 1: return 1`) or it won't stop.
- **Performance tip:** long loops slow programs down; the functional/recursive form was presented as faster for such repeated work. But "programming is an art, not a science" — any working solution is correct; some are just more efficient.
- **Watch the `while` condition in the loop-factorial:** the loop must stop once `num` reaches 0 (use `num > 0`), otherwise multiplying by 0 destroys the result. *(Instructor's spoken condition was ambiguous here.)*

---

## 5. Exam / Assignment notes

- **A SURPRISE QUIZ may be held in the next class (tomorrow).**
  - **Not on the LMS portal** — it is conducted **live in the class**.
  - The instructor will **randomly pick a student**, ask them to **write a small piece of code and share their screen**, to confirm the work isn't copied.
  - **Bring your laptop to class.**
  - Expected scope: "the small codes we have seen so far" — e.g. **write a small function, run a loop, do something, manipulate some text**, etc.
- **Recursion was explicitly flagged as "one of the critical things"** — the instructor stopped and set a live exercise (write factorial with a loop) specifically to make sure recursion was understood. Be able to write factorial **both** ways (loop and recursion).
- Next class: more on flexible argument passing (variable number of arguments, different ways to pass information into a function).
- Next session time: **4:00**.