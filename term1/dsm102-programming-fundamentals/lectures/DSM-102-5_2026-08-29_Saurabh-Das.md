# DSM-102 — Programming Fundamentals for Data Science
## Session 5 — 2026-08-29 (Instructor: Saurabh Das)

---

## 1. Overview

This session finishes the material on **function arguments** and then opens up Python's **built-in collection types**. On the function side it covers default (keyword) arguments, the rules for mixing positional and keyword arguments, arbitrary-length argument lists with `*args`, one-line `lambda` functions, and documentation via **docstrings** (`"""..."""`) retrieved with `help()`. Two in-class exercises are worked: a function `a + 2b` with a default value and a docstring, and generation of the **Fibonacci series below n** (`for`-loop, `while`-loop and tuple-swap versions). The second half introduces the **list** as an ordered, indexed, mutable collection: creation, indexing from 0, iteration, element replacement, nesting (lists and even functions inside lists), and the methods `.append()`, `.pop()`, `.insert()`, `.remove()`, `.extend()` plus `+` concatenation. Python's **class / object / method** terminology is defined, and a heavily emphasised warning is given about **shallow vs. deep copying** (`b = a` aliases the list; use `a.copy()`). The lecture closes with **list comprehensions** (single-line replacements for loop + condition, including nested loops) and a comparison of the four container types — **list, tuple, set, dictionary** — by ordered / indexed / mutable / duplicates-allowed.

---

## 2. Topics in the order taught

### 2.0 Admin
- Slides + **three Google Colab notebooks** uploaded to the shared **Google Drive → `IIT Indore` → `PFDS DSM 102`** folder (not on the LMS).
- A **practice assignment** will be uploaded "today or tomorrow".
- A **short/surprise quiz** was planned for this session, postponed; likely **Monday/Tuesday** next class.

---

### 2.1 Recap: functions and `return`
- Inputs are passed to a function as **arguments**; the function manipulates them and sends a result back to the main script using the keyword **`return`**.
- Without `return`, nothing comes back to the caller.

---

### 2.2 Default (keyword) argument values
- You can give a parameter a **default value** in the `def` line. Then the caller may omit it.
- If a parameter has **no** default and you omit it → **error**.

Example discussed (exact strings inferred — the spoken output was "how do you do"):

```python
def greet(name, message="How do you do"):
    print(message, name)

greet("Amit")                          # uses the default message
greet("Amit", "Good morning")          # both supplied (positional)
greet(message="Good morning", name="Amit")   # keyword args → order does NOT matter
```

**Rules demonstrated:**
1. With **positional arguments**, position decides which parameter gets the value (1st = `name`, 2nd = `message`).
2. With **keyword arguments** (`name=`, `message=`), the **order is irrelevant**.
3. **A positional argument cannot follow a keyword argument.** Once you start using keywords, every argument after that must also be a keyword → otherwise Python raises an error.

#### Worked numeric example (4-parameter function)
Spoken as: define a function of `a, b, x, y` returning `a*x + b*y`, with defaults on `x` and `y`; called as `h(1, 1, y=1)`, which is *equivalent to* `h(1, 1, 3, 1)` because `x` defaults to 3.

```python
# defaults inferred from the spoken walkthrough (x default = 3)
def h(a, b, x=3, y=2):
    return a*x + b*y

h(1, 1, y=1)     # same as h(1, 1, 3, 1)  -> 1*3 + 1*1 = 4
```

```python
def g(a, x, b=0):
    return a*x + b

g(1, 2, 3)   # all three given
g(1, 2)      # b takes its default 0
```

**Take-away:** defaults give flexibility; no default ⇒ every argument must be supplied, and position matters when you aren't using keywords.

---

### 2.3 Arbitrary arguments — `*args`
- Put an **asterisk `*`** before the parameter name so the function accepts **any number** of arguments.
- Inside the function the parameter behaves like a **list/collection** of all the values passed; you iterate over it.

```python
def greet(*names):
    for name in names:
        print("Hello", name)

greet("Amit", "Neha", "Rakesh", "Megha")          # 4 arguments
greet("Amit", "Neha", "Rakesh", "Megha", "ABC")   # 5 arguments — same function, no change needed
```
- **Student Q:** must the call use round brackets, not square? **A:** Yes — a *call* always uses round brackets `()`. The values inside are the arguments; `*names` just collects however many there are.
- **Why bother?** You could equally write an external loop calling a 1-argument function — that is *not wrong*, just less compact. This is the "compact way" to write it.

---

### 2.4 `lambda` — single-line (anonymous) functions
- Same idea as `def`, but the whole function body must fit on **one line**.

```python
cube = lambda x: x**3

cube(4)   # 64
cube(5)   # 125
```
- **Student Q:** can any function be written as a lambda? **A:** Only if it can be expressed in one line. An `if ... else` spread over two lines cannot be crammed in directly. Later, using list/tuple/dict features and **comprehensions**, more things *can* be squeezed into one line — but not everything, and very long one-liners are impractical.
- Use lambdas for simple single computations (square, add, multiply).
- Difference: `def` → unlimited lines; `lambda` → one line.

---

### 2.5 Docstrings and `help()`
- A **docstring** is a text description placed **inside the function**, inside **triple quotes** `"""..."""`.
- Purpose: describe what the function does, who wrote it, when, how to use it — useful when you or colleagues reuse the function later.
- Retrieved with **`help(function_name)`**; it prints exactly what is inside the triple quotes.

```python
def nothing():
    """
    This function does nothing.
    Author: ...   Date: ...   Usage: ...
    """
    pass

help(nothing)
# Help on function nothing in module __main__:
# nothing()
#     This function does nothing.
```
*(the `pass` body is inferred — the instructor only said "it is not doing anything".)*

---

### 2.6 Exercise 1 — `a + 2b` with a default and a docstring
Task: write a function taking `a` and `b`, returning `a + 2*b`, give a **default value** so it can be called with a single argument, and include a **docstring**.

```python
def f(a, b=1):
    """
    Returns a + 2*b.
    b has a default value, so f(a) also works.
    """
    return a + 2*b

f(3, 4)          # positional
f(b=4, a=3)      # keyword, any order
f(3)             # uses default b
help(f)          # prints the docstring
```
*(default value `b=1` is inferred; the instructor only said "put some default value".)*

---

### 2.7 Exercise 2 — Fibonacci numbers less than `n`
Definition given: start with two numbers; each next number = sum of the previous two (0, 1, 1, 2, 3, 5, 8, ...).

**`while`-loop version** (the standard one, prints all Fibonacci numbers < n):

```python
def fib(n):
    """Print Fibonacci numbers less than n."""
    f1, f2 = 0, 1
    while f1 < n:
        print(f1)
        f1, f2 = f2, f1 + f2

fib(10)   # 0 1 1 2 3 5 8
```

**Version using a dummy loop variable** (taken from the chat during class):

```python
a, b = 0, 1
for _ in range(10):      # '_' is a dummy variable, only used to run the loop
    print(a)
    a, b = b, a + b      # 0 1 1 2 3 5 ...
```
*(Both reconstructions follow the spoken logic: "store the value, add the next value, print, keep updating"; exact variable names in the student solutions were `f1`, `f2`, `a`, `b`.)*

- Instructor note: if you couldn't do this yet, **practise more** — it isn't complicated.

---

### 2.8 Lists — definition
- A **list** is an **ordered, indexed collection of objects** (everything in Python is an object).
- Created with **square brackets `[ ]`**; elements may be of **mixed types**.
- **Indexing starts at 0.**

```python
a = ['x', 1, 3.5]
print(a)      # ['x', 1, 3.5]
a[0]          # 'x'   (zeroth position)
a[2]          # 3.5   (index 2)
```

**Iteration** (natural, no index arithmetic needed):

```python
for item in a:
    print(item)
```

**Replacing an element** (lists are **mutable**):

```python
a[0] = 1
print(a)      # first element overwritten -> [1, 1, 3.5]
```
*(the replacement value is inferred; the point made was "the new list is overwritten at that index".)*

**Nesting — lists can contain functions and other lists:**

```python
def f(x):
    return x

b = [f, [1, 2, 2.1]]
print(b)
b[0]    # the function object
b[1]    # the inner list [1, 2, 2.1]
```
- Student Q about nested lists: the **inner list also starts at index 0**; you reach it by first indexing the outer list, e.g. `b[1][0]`.
- Practical value: you can dump many different variables/outputs into one list and retrieve them by position.

---

### 2.9 List methods

| Method / operator | Meaning |
|---|---|
| `.append(x)` | add `x` to the **end** of the list |
| `.pop()` | remove and return the **last** element |
| `.insert(i, x)` | insert `x` **at index `i`**, shifting everything right |
| `.remove(x)` | remove the **first occurrence** of value `x`; raises **ValueError** if not present |
| `.extend(b)` | append all elements of list `b` onto `a` |
| `a + b` | returns a new list = concatenation |
| `.copy()` | **deep** copy (see §2.10) |
| `remove?` / `help(list.remove)` | opens the help for the method |

**Append example (triangular printing):**

```python
a = []
print(a)              # []
for i in range(10):
    a.append(i**2)
    print(a)
# []
# [0]
# [0, 1]
# [0, 1, 4]
# [0, 1, 4, 9]
# ... up to [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Pop example (reverses the build-up):**

```python
while a:
    print(a.pop())    # removes 81, then 64, then 49, ...
```
*(loop form inferred; the demonstrated behaviour was successive removal of the last element, printing the "reverse triangle".)*

**Insert example:**

```python
a = [1, 2, 3]
a.insert(1, 'new')
print(a)      # [1, 'new', 2, 3]  — element 0 unchanged, everything else shifts right
```
*(the inserted value was unclear in the audio; the mechanism — insert at position 1, shift right — is what matters.)*

**Extend / concatenation:**

```python
a = [1, 2, 3]
b = ['x', 'y']
a.extend(b)
print(a)          # [1, 2, 3, 'x', 'y']

# equivalent with '+'
a = [1, 2, 3]
a = a + b         # [1, 2, 3, 'x', 'y']

print(a + [1, 2]) # [1, 2, 3, 'x', 'y', 1, 2]
```

- **Emphasis:** get *highly familiar* with lists — much of what you do with loops can be done with lists, more efficiently and more elegantly.

---

### 2.10 Python terminology: class / object / method
- **Class** — the *type*, e.g. `list`, `int`, `float`. (This is why `type(x)` prints `<class 'int'>`.)
- **Object / instance** — the actual variable or element belonging to that class (numbers, strings, functions inside a list are all objects).
- **Method** — a function attached to an object, called with a **dot**: `.append()`, `.pop()`, `.insert()`, `.copy()`.
- Don't confuse the three terms.

---

### 2.11 ⚠ Shallow copy vs. deep copy (flagged as "very very important")
- A list stores only **pointers** to locations in memory. `b = a` does **not** create a new list — it makes `b` point to the same object; changing one changes the other (**shallow copying / aliasing**).

```python
a = [1, 2, 3, 'x', 'y']
b = a
print(a)   # [1, 2, 3, 'x', 'y']
print(b)   # [1, 2, 3, 'x', 'y']

b[0] = 'edited'
print(a)   # ['edited', 2, 3, 'x', 'y']   <-- A ALSO CHANGED!
print(b)   # ['edited', 2, 3, 'x', 'y']
```

**Correct way — `.copy()` (deep copy):**

```python
a = [1, 2, 3, 'x', 'y']
b = a.copy()

b[0] = 'edited'
print(a)   # [1, 2, 3, 'x', 'y']          <-- original intact
print(b)   # ['edited', 2, 3, 'x', 'y']
```

**Rule to remember:** *A list cannot be copied by simple assignment. Use `.copy()`.* (`help(list.copy)` / `a.copy?` shows usage.)

---

### 2.12 List comprehensions
A compact, "English-like" single line that replaces a loop (+ optional condition) that builds a list.

**Syntax pattern taught:**
```
[ <expression>  for <var> in <iterable>  if <condition> ]
```
i.e. *value to compute* → *the loop(s)* → *the filtering condition*.

**Worked example — square roots of multiples of 3 below 21:**

Explicit version:
```python
import math

s = []
for x in range(21):
    if x % 3 == 0:
        s.append(math.sqrt(x))
print(s)
```

Comprehension version (identical result):
```python
import math
s = [math.sqrt(x) for x in range(21) if x % 3 == 0]
print(s)
```
- Needs the **`math`** module for `math.sqrt()`.
- `x % 3 == 0` ⇒ `x` divisible by 3 with zero remainder (`%` = modulus).

**Nested-loop comprehension:**

```python
out = [(i, j, k)
       for i in range(2)
       for j in range(2)
       for k in range(2)
       if (i + j + k) % 2 == 0]
print(out)
```
Instructor read out the result as `(0,0,1)?`… the values spoken were **0 0 1 / 1 0 1 / 1 1 0**; note that mathematically the full correct output is
`[(0,0,0), (0,1,1), (1,0,1), (1,1,0)]` — the `(0,0,0)` triple appears to have been skipped in speech. Verify by running it.

- Loop order in a comprehension is **outer → inner**, left to right (`for i` outermost, then `for j`, then `for k`).
- Comprehensions need **a lot of practice**; the underlying philosophy is simple.

---

### 2.13 The four container types: list, tuple, set, dictionary

| Type | Literal | Ordered | Indexed | Mutable | Duplicates |
|---|---|---|---|---|---|
| **list** | `[ ]` | Yes | Yes | Yes | Yes |
| **tuple** | `( )` | Yes | Yes | **No (immutable)** | Yes |
| **set** | `{ }` | **No** | **No** | Yes | **No** |
| **dictionary** | `{key: value}` | **No** | Yes — **by key** | Yes | **No duplicate keys** |

**Tuple:**
```python
t = (1, 2, 3, 4)
t[0] = 10      # ERROR — tuples do not support item assignment
```

**Set:**
```python
s = {5, 3, 2, 5}
print(s)       # {2, 3, 5}  — duplicate 5 dropped, original order lost
s.add(6)       # add a new element
s.remove(3)    # remove a specified element
```

**Dictionary:**
```python
d = {5: 12, 2: 27, 3: 'lbs'}   # key: value pairs
d[5] = 28                      # replace the value stored under key 5
print(d)                       # {5: 28, 2: 27, 3: 'lbs'}
```
*(the exact keys/values were partly garbled in audio — the structure "key 5 → value 12, key 2 → value 27, key 3 → 'lbs'", then value under key 5 changed to 28, is the reconstruction.)*
- Dictionaries can also be copied and manipulated like lists.
- These four structures are "quite native to Python" — other languages don't organise data exactly this way, so **practise them**.

---

## 3. Functions / keywords / operators introduced

| Item | One-line meaning |
|---|---|
| `def` | defines a (multi-line) function |
| `return` | sends a value back from a function to the caller |
| default parameter `x=3` | gives a parameter a fallback value so callers may omit it |
| keyword argument `name="Amit"` | passes an argument by parameter name; order-independent |
| positional argument | argument matched to a parameter by its position |
| `*names` (`*args`) | collects an arbitrary number of positional arguments into one iterable |
| `lambda x: x**3` | single-line anonymous function |
| `"""..."""` docstring | in-function description text |
| `help(obj)` / `obj?` | prints the docstring / usage of a function or method |
| `range(n)` | produces 0 … n-1, used to drive `for` loops |
| `for` / `while` | loop constructs |
| `_` (underscore) | conventional dummy loop variable when the value isn't used |
| `[ ]` | list literal / indexing |
| `( )` | tuple literal / function-call brackets |
| `{ }` | set literal, or dict literal with `key: value` |
| `.append(x)` | add to end of list |
| `.pop()` | remove & return last element |
| `.insert(i, x)` | insert at index `i` |
| `.remove(x)` | remove first occurrence; `ValueError` if absent |
| `.extend(b)` | append all of `b` onto the list |
| `.copy()` | create an independent (deep) copy |
| `.add(x)` (set) | add element to a set |
| `+` (lists) | concatenate two lists into a new one |
| `%` | modulus (remainder) |
| `==` | equality test |
| `**` | exponentiation (`i**2`, `x**3`) |
| `import math` | import the math module |
| `math.sqrt(x)` | square root |
| `type(x)` | shows the class of an object |
| `print()` | output |

---

## 4. Syntax rules, common mistakes, debugging tips

1. **Positional arguments cannot follow keyword arguments.** Once you write `f(a, x=1, 2)` you get an error — after the first keyword, all remaining arguments must be keywords.
2. Parameters **without defaults must always be supplied**; omitting them is an error.
3. Function **calls always use round brackets**, regardless of how many arguments (`*args`) are passed.
4. `lambda` must fit on **one line** — no multi-line `if/else` bodies; commas won't rescue a two-statement body.
5. **Never copy a list with `b = a`** — it creates an alias (shallow copy) and edits to `b` mutate `a`. Use **`a.copy()`**.
6. **Tuples are immutable** — `t[0] = ...` raises an error.
7. **Sets silently drop duplicates and lose the insertion order** — don't rely on order or on repeated values.
8. Python indexing **starts at 0**, including for lists nested inside lists.
9. `.remove(x)` raises a **ValueError** if the value is absent.
10. Debugging tip: if you don't remember how a method works, type **`help(list.remove)`** or **`a.remove?`** in the notebook to open the help text.
11. Write **docstrings** in every function — for yourself and for colleagues reusing your code.

---

## 5. Flagged for exams / assignments / practice

- **"Very very important lesson"**: list copying — `b = a` (shallow, aliased) vs `b = a.copy()` (deep, independent). Expect this to be tested.
- Two in-class exercises to be able to reproduce:
  1. Function returning `a + 2*b` **with a default argument and a docstring**, callable positionally, by keyword, or with one argument; demo `help()`.
  2. **Fibonacci series less than n** — `for`-loop version, `while`-loop version, and the `a, b = b, a+b` tuple-swap version.
- Instructor said students who could not write the Fibonacci generator "need to put a bit more effort / practise more."
- **List comprehension requires a lot of practice** — know the `[expr for var in iterable if cond]` pattern and the nested-loop form.
- Become **highly familiar with list operations**; they replace many loops and are more efficient.
- A **practice assignment** will be posted on the Google Drive folder; a **short quiz** is expected in the next session (Monday/Tuesday).
- Know the Python vocabulary: **class, object/instance, method** — and the list/tuple/set/dictionary comparison table (ordered / indexed / mutable / duplicates).