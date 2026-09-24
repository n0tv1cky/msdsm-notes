# DSM-103 (Data Structures) — Session 1
**File:** DSM-103-1_2026-08-18 · **Instructor:** Prof. Somnath Dey, Dept. of CSE, IIT Indore

---

## 1. Overview

This is the opening lecture of the Data Structures course. Because the class has students from mixed backgrounds (B.Tech CS, architecture, etc.), the instructor starts from first principles: *why* a data-science student needs data structures at all, motivated by real applications (stock tickers, printer queues with priorities, social-media follower graphs, sparse/symmetric term–document matrices). He then builds the vocabulary of the subject — **data vs. information**, **entity and attributes**, **Abstract Data Type (ADT)** vs. **data structure**, **primitive data types**, and the three classification axes (**linear vs. non-linear**, **homogeneous vs. non-homogeneous**, **static vs. dynamic**). The second half is devoted to the **array**: its formal definition, terminology (size, type, base, index, range, word), and the **indexing / address-mapping formula** for a one-dimensional array, worked out numerically. The lecture closes with course logistics (co-teaching plan, LMS, evaluation components).

---

## 2. Topics and Concepts, in Order Taught

### 2.1 Motivation — why data structures for data science
- **Data science** (class definition agreed on): given a set of data, we want to **infer some decision / answer queries** from it (e.g., "how many members survived an earthquake"), usually via models with an associated accuracy.
- The practical questions that data structures answer:
  1. **How do you store** the data? (integer, floating point, unstructured: image, video)
  2. **How do you manipulate** it?
  3. **How do you answer queries efficiently?**
- **Real-time constraint example:** autonomous driving — a decision produced after 1 minute is useless; the application is *time-critical*, decisions needed within a fraction of a second.
- **Key principle stated on day 1:** *No single storage structure is good for all applications.* You choose the structure based on (a) the application and (b) the operations you need to perform.

### 2.2 Motivating application examples
- **Stock market:** you want the stock with the **highest value shown first**, accessible in (almost) no time. If it were stored at the end and you had to scan all data, by the time you reach it another stock may have become the highest. So the "highest valued" item must always be **kept ready at the front**, and items must be able to move to the front dynamically. → motivates heaps / priority structures.
- **Printer (plain):** fire 10 print commands on one computer → printouts come out **one by one, in the order fired** → **Queue** (FIFO).
- **Printer (organizational, with authority levels):** high / medium / low priority users all fire jobs; the **highest-priority job must print first**. A low-priority job gets pushed toward the **end**; a high-priority job is placed at the **front**. A normal queue cannot do this → **Priority Queue**.
- **Social media:** "follow / follower" relationships → **Graph**.
- **Document processing:** computing **term frequency (TF)** and **inverse document frequency (IDF)**. Such data can be stored as a matrix (m × n), but often **only the triangular part is needed** — the matrix is **symmetric**, so whatever is below the diagonal is repeated above it. Storing both halves is **redundant** → **sparse / triangular matrix representations**.
- **Conclusion:** when choosing a data structure for an application, judge it on **time complexity** *and* **space (memory) requirement**; there is usually a **trade-off** between the two, resolved by the application's needs.

### 2.3 Source / textbook
- Slides prepared from **"Classic Data Structures", 2nd edition, PHI Learning, by Prof. Debasis Samanta**. (If you reuse the slides, acknowledge the book.)
- Additional example of an ADT operation list taken from **DataFlair**.

### 2.4 Data vs. Information
- A bare value such as **34** is **data**. It could mean anything — it has **no meaning until associated with an attribute**.
- **Entity:** something with certain characteristics / attributes. Example: **Employee** in an organization.
  - Attributes: **Name, Date of Birth, Sex, Designation**.
  - Mapping values to attributes yields **information**, e.g. Name = "Surya Prakash" (a string, but now it *means* the employee's name), DOB = **20 August 1976** (stored in some date format), Sex = **'M' / 'F'** (a single character), Designation = a string.
- Another example: the value **0.95** is data; saying "this is the **accuracy of prediction**" turns it into information.
- **Data science aims to obtain information (decisions) from data.**

### 2.5 Abstract Data Type (ADT)
- **Definition:** an ADT is a **logical description** — a **collection of data together with a set of operations to be performed on that data** — specified **without regard to how it will be implemented**.
- **Worked illustration:** let the data set be **{5, 12, 16, 7, 10}**. Define an operation `max` that returns the maximum element. *How* the data is stored (array, linked list, queue, …) does not matter at the ADT level.
- Typical operations listed (DataFlair example):
  - `isEmpty()` — is the structure empty?
  - `isFull()` — is it full? (if full, an **insert must raise an error**)
  - `get()` — get the first / an element
  - `insert(x)`
  - `remove(position)`
  - `replace(...)`
  - `size()`
  - plus application-specific ones like `max()`
- Requirements on an ADT: operations must be **defined per application requirement**, must be **performed efficiently**, and the data must be stored with **minimum memory**.

### 2.6 Data Structure (as implementation of an ADT)
- **Definition:** a **data structure is the implementation of an ADT** — it is a **construct used to store a collection of data**, giving the **physical view** of the data using **programming constructs and primitive data types**.
- Implementation involves **choosing a particular structure**. Examples given:
  - To support `max` efficiently → use a **priority queue / heap**, where the first element is always the maximum (or minimum).
  - To support `isEmpty` → simply **check the pointer value(s)**.
- **Primitive data types:** `int`, `float`, `char`, `double` — the basic elements able to store the smallest unit of data.

### 2.7 Classification axis 1 — Linear vs. Non-linear (organization method)
- **Linear:** data maintains a **particular sequence**; elements accessed one after another.
  - Examples: **array, linked list, stack, queue**.
- **Non-linear:** **random order**; you must **jump from one place to another through links**; no sequence maintained in memory.
  - Examples: **tree, graph, dictionary, heap** (a heap is a kind of tree), **trie** (also a kind of tree).
  - *Diagram described:* a **family tree** — one node is the head of the family, with children hanging below it, and their children below them. Nodes at the same level have no ordering between them; the structure is defined by parent–child links, not by sequence.
- **Course scope:** array, linked list, stack, queue, tree, graph, heap.

#### Arrays as the canonical linear structure (visual description)
- **1-D array** = a **1 × n matrix**: a single row of cells, e.g. `5 | 10 | 12 | 13`, accessed in sequence.
- **2-D array** = an **m × n grid** (m rows, n columns).
  - **Row-major order:** rows are accessed one after another (all of row 1, then all of row 2, …).
  - **Column-major order:** columns are accessed one after another (all of column 1, then column 2, …).
- **3-D array** = **multiple planes of 2-D arrays** stacked.
- **4-D array** = "cannot be visualized" — think of it as a **collection of multiple 3-D arrays**.

### 2.8 Classification axis 2 — Homogeneous vs. Non-homogeneous (type of data)
- **Homogeneous:** all elements of the **same type** (e.g. all integers). Examples: **array, linked list** (of one type).
  - In a classical array you **cannot mix int, float, char**.
  - **Modern languages (e.g. Python) appear to allow mixed types in a "list/array"**, but that is handled by **back-end libraries** that manage the conversion/storage internally.
- **Non-homogeneous (structure):** different field types stored together, e.g. employee record = {name (string), age (int), DOB, salary (float), designation (string)}. Internally you must **allocate memory for each different type and keep track of all those memories together** → `struct` / structured data type.

#### Why type matters: internal binary representations (as sketched on the board)
- **Integer:** e.g. **5 → binary 101**; stored as 0/1 bits. An `int` was quoted as taking **4 bytes**.
- **Signed integer:** one bit reserved as a **sign bit** — **0 = positive, 1 = negative**; the remaining bits hold the binary magnitude.
- **Floating point:** e.g. **5.5 = 55 × 10⁻¹**. Memory is partitioned into three fields:
  1. **Sign bit** (0 = +, 1 = −)
  2. **Exponent** field (here the value −1, converted to binary)
  3. **Mantissa** field (here 55)
- **Character:** characters have a **code (Unicode/ASCII)**, i.e. an associated binary value, so an integer-like type can store them; since codes are **all positive**, an **unsigned** representation is used (no sign bit needed).
- Because internal layouts differ per type, a homogeneous structure uses **one uniform representation** internally — you cannot put a float into a slot designed for an int.

### 2.9 Classification axis 3 — Static vs. Dynamic (storage type)
- **Static data structure:** memory is **fixed at declaration time**. Bounded by a **lower bound L** and **upper bound U** of a fixed block; all data must be stored **sequentially inside that block**. Even if free space exists **elsewhere** in memory, it **cannot be used** by that structure. Example: **array**.
- **Dynamic data structure:** allocates as data arrives.
  - *Diagram described:* computer memory drawn as a long strip with scattered free blocks. The allocator **checks where memory is available**, creates a block there and stores an element; then finds the **next available space** (perhaps 10–15 bytes later), stores the next element there, and **maintains a link from the first block to the second**. The structure is thus a chain of scattered blocks joined by links.
  - Example: **linked list**.
- Contrast in access: in a static (array) structure you access elements **one after another in contiguous memory**; in a dynamic structure you **follow links**.

### 2.10 The Array — formal treatment

**Idea:** an array stores a **group of data together in one place** (a *composite* data structure), in **contiguous memory locations**.

*Memory diagram described:* computer memory is a column of cells, each with an address; assume each cell/word occupies 1 byte, so addresses run 453, 454, 455, … If you store 5, 8, 10 in an array, they occupy three **consecutive** locations.

**Definition:** *An array is a finite, ordered collection of homogeneous data elements.*
- **Finite** → a fixed number of elements can be stored.
- **Ordered** → elements stored one after another.
- **Homogeneous** → all elements of the same type (int array for ints, float array for floats, character array/string for characters).

**Terminology (exam-style vocabulary):**
| Term | Meaning |
|---|---|
| **Size** (also *length*, *dimension*) | Number of elements in the array |
| **Type** | The primitive data type stored (int / float / char / …) |
| **Base** (**M**) | **Starting address** of the array in memory (base address) |
| **Index** | The position at which an element is stored; element written **A[I]** |
| **Range of indices** | From **lower bound L** to **upper bound U** |
| **Word** (**W**) | The amount of memory needed to store **one single element** |

**Index conventions:**
- If the start index is **0**, the third element is at **I = 2**; if the start index is **1**, the third element is at **I = 3**.
- For an array of size **n**:
  - start index 0 → index range **0 to n − 1** (upper bound = size − 1)
  - start index 1 → index range **1 to n** (upper bound = size/length)
- Different programming languages use different lower bounds, hence the need for a **generalized** formula.

**Formulas given (write these down exactly):**

1. **Index of the I-th element relative to the lower bound:**
$$\text{index} = L + I - 1$$

2. **Size of the array from its bounds:**
$$\text{Size} = U - L + 1$$
 (verify: L = 0, U = n − 1 → size = n; L = 1, U = n → size = n)

3. **Address / indexing (mapping) function for a 1-D array — general form:**
$$\textbf{Address}(A[I]) \;=\; M \;+\; (I - L)\times W$$
 where **M** = base address, **L** = lower bound, **W** = word size (bytes per element).

4. **Special case** used in the first illustration (**L = 1** and **W = 1**):
$$\textbf{Address}(A[I]) \;=\; M \;+\; (I - 1)$$

> A one-dimensional array needs **only one subscript** to refer to an element.

**Worked example 1 (L = 1, W = 1):**
- Array A with **base address M = 1000**, **L = 1**, **U = 100** (so indices run 1…100), each element needs **1 word = 1 byte**.
- Find the address of the **4th element**:
 `Address(A[4]) = 1000 + (4 − 1) × 1 = 1003`
- Check by layout: A[1] → 1000, A[2] → 1001, A[3] → 1002, **A[4] → 1003**. ✔

**Worked example 2 (W = 2):**
- **M = 1000**, each element takes **2 bytes** (e.g. storing the value 10).
- A[1] occupies addresses **1000–1001**; therefore the **second element starts at 1002**.
- Using the formula with L = 1: `Address(A[2]) = 1000 + (2 − 1) × 2 = 1002`. ✔

**Clarification raised by a student (why two different formulas?):**
- `M + (I − 1)` is only the **special case** where the lower bound happens to be **1** and the word size is **1 byte**.
- `M + (I − L) × W` is the **generalized** version: if the array's starting index were **5**, you would use **(I − 5)**; if each element needed **2 bytes**, you multiply by **2**.

**Why it's called a "mapping function" / "indexing problem":**
- In real memory, the OS and other running applications occupy space. When memory is allocated for your array, it is taken from **free space**, so the base address **M is essentially an arbitrary value**, not 0. The array is then allocated **contiguously** from M. The formula therefore *maps* a logical index I to a **physical memory address**.

**Generalized mapping diagram (described):** the logical array is drawn with indices running from **L** to **U**; below it, the physical memory is drawn as a contiguous run of cells starting at address **M**, each cell **W** bytes wide, with an arrow from logical index I to the physical address `M + (I − L)·W`.

### 2.11 Class discussion — 1-based vs 0-based indexing
- **0-based:** C, Python, Java.
- **1-based:** **R** — vectors and lists start at **1**. Also **SQL**: string functions like `SUBSTRING` count positions **starting from 1**.
- Take-away: **generalize** — use the given lower bound (0 or 1 or anything else) in the address formula.

### 2.12 Announced upcoming topics
- **Two-dimensional arrays** and their varieties:
  - **Lower triangular array**
  - **Upper triangular array**
  - **Diagonal array**
  - **Alpha–beta (sparse/band) array**
- Then: **linked lists, stacks, queues, trees, graphs, heaps**.

---

## 3. Exam / Assignment / Logistics Notes

- **Course sharing & lecture plan:** Co-taught with **Prof. Surya Prakash**. Sequence: **first 5 lectures — Prof. Somnath Dey → next 5 — Prof. Surya Prakash → next 5 — Prof. Dey → last 5 — Prof. Prakash.** Lectures are divided **by topic**, so the order is usually kept sequential; occasionally the two may swap/parallelize if one is unavailable.
- **Evaluation components announced:**
  - **Mid-term exam**
  - **End-term exam**
  - **Quizzes** (possible)
  - **Viva / interview-style oral** (possible) — conducted **outside lecture hours**
  - **Class participation / interaction** — the instructor **notes the names of students who interact**, and this counts as an evaluation component. (Also: students are requested to **keep cameras on**.)
- **Course materials:** Slides will be uploaded on **Moodle at lms.iiti.ac.in**. The course has been created; **enrolment expected to be completed by the weekend**, after which slides/materials will appear there.
- **Attribution requirement:** slides are derived from **Samanta, *Classic Data Structures*, 2nd ed., PHI Learning** — acknowledge the book if reusing.
- **Highest-value formulas to memorize from this session:**
  - `Address(A[I]) = M + (I − L) × W` (1-D array address/indexing function)
  - `Size = U − L + 1`
  - `index = L + I − 1`
- **Conceptual points likely to be asked:** difference between **data and information**; **ADT vs. data structure**; the three classification axes (linear/non-linear, homogeneous/non-homogeneous, static/dynamic) with examples; the formal **definition of an array** (finite, ordered, homogeneous); **row-major vs column-major** access order.
- **Next class:** Thursday.