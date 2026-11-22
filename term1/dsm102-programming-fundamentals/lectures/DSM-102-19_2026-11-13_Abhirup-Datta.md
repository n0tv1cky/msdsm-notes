---
course: DSM 102
date: 2026-11-13
start: 7:00pm
session: "19"
faculty: Abhirup Datta
---

<!-- nav -->
← [Session 18 (2026-11-02)](DSM-102-18_2026-11-02_Abhirup-Datta.md) · [All lectures](./) · [Session 20 (2026-11-14)](DSM-102-20_2026-11-14_Abhirup-Datta.md) →
<!-- /nav -->

# DSM-102 · Session 19 · Calculus for Data Science: Optimization and Learning

**File:** DSM-102-19_2026-11-13_Abhirup-Datta

> **About these notes:** The transcript has heavy speech-to-text errors. Formulas and code below are reconstructed from context. Where I had to infer a value, symbol, or line of code, it is marked **[inferred]**. Several worked examples come from astronomy, which is the instructor's chosen application domain. The code was shown in a notebook and only described verbally, so every code block is a best-effort reconstruction, not a verbatim copy.

---

## 1. Overview

The previous session covered probability distributions (Poisson, Normal, Beta, etc.) and their summary statistics. Those distributions always took their parameters ($`\lambda, \mu, \sigma`$) as known. In real data science the parameters are unknown and must be learned from data. This session introduces calculus as the tool for that learning.

Every ML model learns by solving one problem: find parameters $`\theta`$ that make a loss/cost function $`L(\theta)`$ as small as possible. The session builds up the needed machinery step by step:

- derivatives (including numerical approximation and error propagation)
- partial derivatives and relative sensitivity
- gradients, including the vanishing-gradient problem and the log trick
- gradient descent and the effect of the learning rate
- cost functions derived from negative log-likelihood
- the chain rule, applied to logistic regression
- Jacobians (change of variables, vector error propagation)
- Hessians (curvature, classifying minima/maxima/saddles, maximum stable learning rate, parameter uncertainty)

Each idea is checked numerically in Python with NumPy, Matplotlib, SciPy and SymPy. Worked examples include the distance modulus, stellar flux, a Gaussian star image, Poisson photon counts, Hubble's law, and star–galaxy classification.

---

## 2. Topics Covered (in order taught)

### 2.0 Setup / Libraries
- Libraries used: `numpy` (`np`), `matplotlib.pyplot` (`plt`), `scipy` (especially `scipy.optimize`), and later `sympy` (`sp`) for symbolic derivatives.
- Core framing: learning means finding

  $`\displaystyle \hat\theta = \arg\min_\theta L(\theta)`$

---

### 2.1 The Derivative

**Definition.** The derivative measures how sensitive the output is to a tiny change in one input; this is the slope.

```math
f'(x) = \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
```

**Geometric meaning.** $`f'(x)`$ is the slope of the tangent line at $`x`$.
- $`f'(x) > 0`$: the function is rising.
- $`f'(x) < 0`$: the function is falling.
- $`f'(x) = 0`$: the function is flat there, which is possibly a minimum (or a maximum).

**Standard derivatives listed on the slide** (partly garbled; the standard forms are given):
- Power rule: $`\dfrac{d}{dx}x^n = n x^{n-1}`$
- Exponential: $`\dfrac{d}{dx}e^{ax} = a\,e^{ax}`$ **[inferred]**
- Logarithm: $`\dfrac{d}{dx}\ln x = \dfrac{1}{x}`$ **[inferred]**

#### Worked example 1: $`f(x) = (x-3)^2 + 1`$

- Analytic derivative: $`f'(x) = 2(x-3)`$.
- **Numerical check at $`x = 5`$:** use the finite difference $`\frac{f(x+h)-f(x)}{h}`$ for increasing/decreasing values of $`h`$. Then compare with the exact value $`f'(5) = 2(5-3) = 4`$ and look at the truncation error.
- **Critical point:** $`f'(x) = 0 \Rightarrow x = 3`$, which is the minimum, with $`f(3) = 1`$. The demo started from $`x = 0`$ and "slid" toward $`x = 3`$ by following the slope.

```python
import numpy as np
import matplotlib.pyplot as plt

f      = lambda x: (x - 3)**2 + 1
fprime = lambda x: 2 * (x - 3)          # analytic derivative

x0 = 5.0
for h in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:   # exact h values [inferred]
    fd = (f(x0 + h) - f(x0)) / h           # forward difference
    print(h, fd, abs(fd - fprime(x0)))     # truncation error
```

For this quadratic, the forward-difference error equals exactly $`h`$, because $`\frac{(x+h-3)^2-(x-3)^2}{h} = 2(x-3)+h`$. So the error shrinks linearly with $`h`$.

> **Tip (standard numerical analysis, not explicitly stated in lecture):** making $`h`$ extremely small (e.g. $`10^{-12}`$) eventually increases the error because of floating-point round-off. Truncation error is reduced by smaller $`h`$; round-off error is increased by it.

#### First-order Taylor expansion and error propagation

```math
f(x + \delta) \approx f(x) + f'(x)\,\delta
```

An input uncertainty $`\sigma_x`$ therefore produces an output uncertainty

```math
\sigma_f \approx |f'(x)|\,\sigma_x
```

#### Worked example 2: Distance modulus (magnitude error becomes distance error)

- Distance modulus: $`\mu = m - M = 5\log_{10}\!\left(\dfrac{d}{10\,\text{pc}}\right)`$.
- Solving for distance:

  $`\displaystyle d = 10^{(\mu + 5)/5}\ \text{pc}`$

- Derivative:

  $`\displaystyle \frac{dd}{d\mu} = \frac{\ln 10}{5}\, d \approx 0.4605\, d`$

- Propagated error:

  $`\displaystyle \sigma_d = \frac{\ln 10}{5}\, d\, \sigma_\mu \quad\Rightarrow\quad \frac{\sigma_d}{d} \approx 0.46\,\sigma_\mu`$

- The code used $`\sigma_\mu = 0.1`$. That gives $`\sigma_d/d \approx 4.6\%`$ (my arithmetic, not read out in lecture).
- **Plot:** $`d`$ versus $`\mu`$, with the tangent line drawn at $`\mu = 10`$. At that point $`d = 10^{3}\,\text{pc} = 1000`$ pc, the slope is $`\approx 460`$ pc per mag, and $`\sigma_d \approx 46`$ pc (my arithmetic).

```python
sigma_mu = 0.1
d     = lambda mu: 10**((mu + 5) / 5)          # parsecs
dd_dmu = lambda mu: np.log(10) / 5 * d(mu)

mu0 = 10.0
sigma_d = dd_dmu(mu0) * sigma_mu
print(d(mu0), dd_dmu(mu0), sigma_d)

mu = np.linspace(5, 15, 200)                   # range [inferred]
plt.plot(mu, d(mu), label="d(mu)")
plt.plot(mu, d(mu0) + dd_dmu(mu0) * (mu - mu0), "--", label="tangent at mu=10")
plt.legend(); plt.show()
```

---

### 2.2 Partial Derivatives

**Definition.** Real models have many inputs and parameters. A partial derivative measures the effect of one of them while all others are held constant, which isolates the effect of one feature or one weight.

```math
\frac{\partial f}{\partial x_i}(x_1,\dots,x_n) = \lim_{h\to 0}\frac{f(\dots, x_i + h, \dots) - f(\dots, x_i, \dots)}{h}
```

#### Worked example 3: Flux from a star

The flux is

```math
F(L, d) = \frac{L}{4\pi d^2}
```

- Holding $`d`$ fixed: $`\dfrac{\partial F}{\partial L} = \dfrac{1}{4\pi d^2}`$.
- Holding $`L`$ fixed: $`\dfrac{\partial F}{\partial d} = -\dfrac{2L}{4\pi d^3} = -\dfrac{2F}{d}`$.

**Relative sensitivity** (elasticity):

```math
\frac{L}{F}\frac{\partial F}{\partial L} = 1, \qquad \frac{d}{F}\frac{\partial F}{\partial d} = -2
```

Interpretation: a 1% change in distance changes the flux twice as much as a 1% change in luminosity.

**Multi-input error propagation** (independent errors):

```math
\sigma_F^2 = \left(\frac{\partial F}{\partial L}\right)^2 \sigma_L^2 + \left(\frac{\partial F}{\partial d}\right)^2 \sigma_d^2
```

Dividing by $`F^2`$ gives the relative form:

```math
\left(\frac{\sigma_F}{F}\right)^2 = \left(\frac{\sigma_L}{L}\right)^2 + 4\left(\frac{\sigma_d}{d}\right)^2
```

**Code.** Initial values were $`L_0 = L_\odot`$ (solar luminosity) and $`d_0 = 10`$ pc. Analytic partials were compared with numerical finite differences, and the relative sensitivities were printed (≈ 1 and ≈ −2).

```python
L_sun = 3.828e26          # W
pc    = 3.086e16          # m
F = lambda L, d: L / (4 * np.pi * d**2)

L0, d0 = L_sun, 10 * pc
F0 = F(L0, d0)

h = 1e-6                  # relative step [inferred]
dF_dL_num = (F(L0*(1+h), d0) - F0) / (L0*h)
dF_dd_num = (F(L0, d0*(1+h)) - F0) / (d0*h)
dF_dL     = 1 / (4*np.pi*d0**2)
dF_dd     = -2 * F0 / d0
print(dF_dL, dF_dL_num, dF_dd, dF_dd_num)

print("rel. sens. L:", L0/F0 * dF_dL)   # -> 1
print("rel. sens. d:", d0/F0 * dF_dd)   # -> -2
```

**Plots:**
- Left panel: 2-D map of $`F`$ over $`(L, d)`$. The blue and green lines are 1-D slices with one variable fixed.
- Middle and right panels: $`F`$ versus $`L`$ (a straight line) and $`F`$ versus $`d`$ (falling as $`1/d^2`$).

**SymPy (symbolic) version:**
```python
import sympy as sp
L, d = sp.symbols('L d', positive=True)
F_sym = L / (4*sp.pi*d**2)
print(sp.diff(F_sym, L))   # 1/(4*pi*d**2)
print(sp.diff(F_sym, d))   # -L/(2*pi*d**3)
```

---

### 2.3 The Gradient

**Definition.** The gradient collects all partial derivatives into one vector:

```math
\nabla f(\mathbf{x}) = \left(\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n}\right)
```

**Meaning.**
- **Direction:** the gradient points in the direction of steepest ascent. On a hill, it is the direction you would face to walk straight up the steepest part.
- **Magnitude:** $`\|\nabla f\|`$ tells you how steep that incline is.

#### Worked example 4: Gaussian star on a CCD

A star's brightness profile on a CCD is approximately a 2-D Gaussian:

```math
I(x,y) = A \exp\!\left(-\frac{(x-x_0)^2 + (y-y_0)^2}{2\sigma^2}\right)
```

Its gradient:

```math
\frac{\partial I}{\partial x} = -\frac{x - x_0}{\sigma^2}\, I, \qquad \frac{\partial I}{\partial y} = -\frac{y - y_0}{\sigma^2}\, I
```

**Problem: vanishing gradient.** Far from the star, $`I \approx 0`$, so $`\nabla I \approx 0`$ as well. An algorithm that follows $`\nabla I`$ gets stuck, because it sees no slope.

**Fix: use the log.**

```math
\nabla \ln I = \frac{\nabla I}{I} = -\frac{1}{\sigma^2}\big(x - x_0,\; y - y_0\big)
```

The factor $`I`$ cancels. The gradient of $`\ln I`$ never vanishes away from the centre and always points straight at the star.

**Code / demo.**
- Parameters: $`A, x_0, y_0, \sigma`$ (values not clearly audible).
- Analytic $`\partial I/\partial x`$ at the test pixel $`(-1, 1)`$ was compared with a finite difference. The transcript says roughly "64 … numerically 64.3, matches". The exact numbers are uncertain **[inferred]**.
- A grid `np.arange(-3, 3, …)` was used for a quiver plot of arrows. The arrows all point toward the star.
- Ascent started at $`(-3, 3)`$:
  - Following $`\nabla I`$: the gradient there is ≈ 0, so the path barely moves.
  - Following $`\nabla \ln I`$: about 40 steps reach the star centre (shown as a green dotted path).
  - The final coordinates in the transcript are garbled ("1, 1.49 … −7").

```python
A, x0, y0, sigma = 1000.0, 0.0, 0.0, 1.0      # values [inferred]
I = lambda x, y: A * np.exp(-((x-x0)**2 + (y-y0)**2) / (2*sigma**2))

def grad_I(x, y):
    return np.array([-(x-x0)/sigma**2, -(y-y0)/sigma**2]) * I(x, y)

def grad_lnI(x, y):
    return np.array([-(x-x0)/sigma**2, -(y-y0)/sigma**2])

# numerical check at pixel (-1, 1)
h = 1e-6
num = (I(-1+h, 1) - I(-1, 1)) / h
print(grad_I(-1, 1)[0], num)

# gradient ASCENT toward the star using ln I
p = np.array([-3.0, 3.0]); eta = 0.1            # eta [inferred]
path = [p.copy()]
for _ in range(40):
    p = p + eta * grad_lnI(*p)
    path.append(p.copy())

# arrows
X, Y = np.meshgrid(np.arange(-3, 3.5, 0.5), np.arange(-3, 3.5, 0.5))
U, V = grad_lnI(X, Y)
plt.quiver(X, Y, U, V); plt.plot(*np.array(path).T, 'g.-'); plt.show()
```

> **Key takeaway (student Q&A).** A student asked for this to be re-explained. When $`I \approx 0`$, $`\nabla I \approx 0`$, so the optimiser stalls even though it has not reached the peak. Dividing by $`I`$ (i.e. using $`\nabla \ln I`$) removes that factor, leaving only the geometric part, which always points to the centre.
>
> This is the same reason ML minimises the *log*-likelihood rather than the likelihood itself.

---

### 2.4 Gradient Descent

**Idea.** The gradient points uphill, so step in the opposite direction (multiply by $`-1`$). Repeat until the slope levels out, i.e. you reach the bottom. This is an alternative to the least-squares fitting covered in the previous class.

**Update rule.**

```math
\theta_{t+1} = \theta_t - \eta\, \nabla L(\theta_t)
```

Here $`\eta`$ is the **learning rate** (step size).

**Why it works.** A first-order Taylor expansion gives

```math
L(\theta_{t+1}) \approx L(\theta_t) - \eta\, \|\nabla L(\theta_t)\|^2
```

The subtracted term is non-negative, so each small step lowers the loss.

---

### 2.5 Cost Functions from Likelihood

- Given data $`x_1, \dots, x_n`$ and a model distribution $`p(x\mid\theta)`$, the log-likelihood is

  $`\displaystyle \ell(\theta) = \sum_{i=1}^{n} \ln p(x_i \mid \theta)`$

- The best parameters maximise $`\ell(\theta)`$. This is the same as minimising the **negative log-likelihood (NLL)**, which becomes the cost function:

  $`\displaystyle L(\theta) = -\sum_{i=1}^{n} \ln p(x_i\mid\theta)`$

- **Gaussian errors** give the mean squared error: $`L \propto \sum_i (y_i - \hat y_i)^2`$.
- **Bernoulli outcomes** give the log loss (cross-entropy): $`L = -\sum_i \left[y_i \ln p_i + (1-y_i)\ln(1-p_i)\right]`$.

#### Worked example 5: Poisson photon counts

Five 1-second exposures recorded photon counts $`k_i`$. The transcript says "356 and so on". The mean is 4, so the counts were plausibly something like $`[3,5,6,\dots]`$ **[exact values inferred]**.

1. Poisson NLL (dropping the constant $`\sum \ln k_i!`$):

   $`\displaystyle L(\lambda) = n\lambda - \left(\sum_i k_i\right)\ln\lambda`$

2. Derivative:

   $`\displaystyle \frac{dL}{d\lambda} = n - \frac{\sum_i k_i}{\lambda}`$

3. Set it to zero:

   $`\displaystyle \hat\lambda = \frac{1}{n}\sum_i k_i = \bar k`$

So the MLE is the sample mean, here **4 photons/s**. A numerical minimisation (`minimize_scalar`) gave the same answer, 4 photons/s.

```python
from scipy.optimize import minimize_scalar
k = np.array([3, 5, 6, 2, 4])           # [inferred] -- any 5 counts with mean 4
nll = lambda lam: len(k)*lam - np.sum(k)*np.log(lam)

lam_calc = k.mean()
res = minimize_scalar(nll, bounds=(0.1, 20), method='bounded')
print(lam_calc, res.x)                  # both ~4
```

**Extension.** The experiment was repeated with more exposures (100 and 400 are mentioned). The NLL curve $`L(\lambda)`$ was plotted; its minimum, where $`dL/d\lambda = 0`$, again sits at $`\lambda \approx 4`$ and matches the data.

#### Worked example 6: Hubble's law by gradient descent

- Model: $`v = H_0\, d`$ for 4 galaxies with distances $`d_i`$ and velocities $`v_i`$.
- Cost (Gaussian errors, so MSE):

  $`\displaystyle L(H_0) = \sum_{i=1}^{4} (v_i - H_0 d_i)^2`$

- Derivative:

  $`\displaystyle \frac{dL}{dH_0} = -2\sum_i d_i\,(v_i - H_0 d_i)`$

- Setting it to zero gives the **closed form**:

  $`\displaystyle \hat H_0 = \frac{\sum_i d_i v_i}{\sum_i d_i^2}`$

  In lecture this gave $`\hat H_0 \approx 70`$ km/s/Mpc.
- Gradient-descent update:

  $`\displaystyle H_{t+1} = H_t - \eta\,\frac{dL}{dH_0}\bigg|_{H_t}`$

- **Learning-rate experiment:**

  | $`\eta`$ | Behaviour |
  |---|---|
  | $`3.5\times10^{-4}`$ (large) | **Diverges** (oscillates and blows up) |
  | Smaller values (red and orange curves) | Converge to $`\hat H_0`$ |

  The error shrinks by a constant factor each step. A smaller $`\eta`$ converges more slowly but safely; the converged value is reached by roughly step 10 for good choices.

**Why the error shrinks by a constant factor** (derivation added for clarity):

```math
H_{t+1} - \hat H_0 = \left(1 - 2\eta\textstyle\sum_i d_i^2\right)(H_t - \hat H_0)
```

So convergence requires $`|1 - 2\eta\sum d_i^2| < 1`$, i.e. $`0 < \eta < 1/\sum_i d_i^2`$. This is exactly the Hessian rule in §2.8: here $`H = 2\sum d_i^2`$ and the condition is $`\eta < 2/H`$.

```python
d = np.array([10., 20., 30., 40.])          # Mpc  [inferred, illustrative]
v = np.array([700., 1400., 2100., 2800.])   # km/s [inferred, illustrative]

L      = lambda H: np.sum((v - H*d)**2)
dL_dH  = lambda H: -2*np.sum(d*(v - H*d))
H_closed = np.sum(d*v) / np.sum(d**2)       # ~70

for eta in [3.5e-4, 3e-4, 2e-4, 1e-4]:      # first one diverges
    H = 0.0
    for t in range(20):
        H = H - eta * dL_dH(H)
    print(eta, H)
```

With these illustrative distances, $`\sum d_i^2 = 3000`$, so the threshold is $`\eta < 3.33\times10^{-4}`$. That is consistent with $`3.5\times10^{-4}`$ diverging in lecture, but the real data were not read out.

---

### 2.6 The Chain Rule

**Definition.** The derivative of a nested function (a function inside another function):

```math
\frac{d}{dx} f(g(x)) = f'(g(x))\cdot g'(x)
```

**In machine learning the chain is longer.** If $`L`$ depends on $`p`$, $`p`$ on $`z`$, and $`z`$ on $`w`$:

```math
\frac{\partial L}{\partial w} = \frac{\partial L}{\partial p}\cdot\frac{\partial p}{\partial z}\cdot\frac{\partial z}{\partial w}
```

This is the basis of backpropagation.

#### Worked example 7: Star vs galaxy classification (logistic regression)

- **Feature:** $`x = m_{\text{PSF}} - m_{\text{model}}`$. Stars have $`x \approx 0`$; galaxies have $`x > 0`$.
- SDSS uses a cut on this difference. The standard SDSS value is about $`0.145`$ mag **[inferred from "Carton … magnitude"]**.
- **Model:**

  $`\displaystyle z = w x + b, \qquad p = \sigma(z) = \frac{1}{1 + e^{-z}}`$

- **Loss** (log loss / Bernoulli NLL):

  $`\displaystyle L = -\sum_i \left[y_i \ln p_i + (1-y_i)\ln(1-p_i)\right]`$

**Applying the chain rule, one data point at a time.** The three factors are:

```math
\frac{\partial L_i}{\partial p_i} = -\frac{y_i}{p_i} + \frac{1-y_i}{1-p_i}, \qquad \frac{\partial p_i}{\partial z_i} = p_i(1-p_i), \qquad \frac{\partial z_i}{\partial w} = x_i
```

Multiplying them, the result simplifies to:

```math
\frac{\partial L}{\partial w} = \sum_i (p_i - y_i)\,x_i, \qquad \frac{\partial L}{\partial b} = \sum_i (p_i - y_i)
```

**Code steps:**
1. Simulate $`x`$ for stars and galaxies.
2. Define `sigmoid` and the log loss.
3. **Gradient check:** compare the chain-rule gradient with a numerical finite difference.
4. Run gradient descent for 3000 steps from initial $`w_0`$, $`b_0`$, with learning rate $`\eta`$.

**Results:**
- Plot of the two histograms: blue for stars, the other colour for galaxies. The learned decision boundary ($`p = 0.5`$, i.e. $`x = -b/w`$) sits between them.
- Log loss versus iteration converges to ≈ 0.1. It is already close to that by ≈ 1000 steps; the full run is 3000 steps.

```python
rng = np.random.default_rng(0)
x_star = rng.normal(0.0, 0.05, 500)          # distributions [inferred]
x_gal  = rng.normal(0.5, 0.2, 500)
x = np.concatenate([x_star, x_gal])
y = np.concatenate([np.zeros(500), np.ones(500)])

sigmoid = lambda z: 1 / (1 + np.exp(-z))
def logloss(w, b):
    p = sigmoid(w*x + b)
    return -np.mean(y*np.log(p) + (1-y)*np.log(1-p))
def grad(w, b):
    p = sigmoid(w*x + b)
    return np.mean((p - y)*x), np.mean(p - y)

# gradient check
w0, b0, h = 1.0, 0.0, 1e-6
print(grad(w0, b0)[0], (logloss(w0+h, b0) - logloss(w0, b0))/h)

w, b, eta = w0, b0, 1.0                      # eta [inferred]
losses = []
for step in range(3000):
    gw, gb = grad(w, b)
    w -= eta*gw;  b -= eta*gb
    losses.append(logloss(w, b))
print(w, b, -b/w)                            # decision boundary
```

The lecture's loss may have been a sum rather than a mean, which only rescales $`\eta`$.

---

### 2.7 The Jacobian

**Motivation.** A gradient is a single vector because the function has one output (the total error). When a function takes multiple inputs and produces multiple outputs, we need the Jacobian.

**Definition.** For $`\mathbf f: \mathbb{R}^n \to \mathbb{R}^m`$, the Jacobian is the $`m\times n`$ matrix of first partial derivatives:

```math
J_{ij} = \frac{\partial f_i}{\partial x_j}
```

**Key facts:**
- The gradient is the Jacobian of a scalar function: a single row.
- $`|\det J|`$ tells how the transformation stretches or shrinks area/volume. It is needed when changing variables in an integral.
- **Error propagation for vector outputs:**

  $`\displaystyle \Sigma_y = J\, \Sigma_x\, J^{T}`$

#### Worked example 8: Polar to Cartesian

The transformation is $`x = r\cos\phi`$, $`y = r\sin\phi`$. Its Jacobian:

```math
J = \begin{pmatrix} \dfrac{\partial x}{\partial r} & \dfrac{\partial x}{\partial \phi} \\[2mm] \dfrac{\partial y}{\partial r} & \dfrac{\partial y}{\partial \phi}\end{pmatrix} = \begin{pmatrix} \cos\phi & -r\sin\phi \\ \sin\phi & r\cos\phi\end{pmatrix}
```

Its determinant:

```math
\det J = r\cos^2\phi + r\sin^2\phi = r
```

So a small patch $`dr\,d\phi`$ maps to area $`dA = r\,dr\,d\phi`$. This is the familiar area element in polar integrals.

**Code.** The Jacobian was computed analytically and numerically with $`h = 10^{-6}`$ (printed rounded to 4 decimals). The check gave $`\det J = r = 2`$ at the chosen point. The value of $`\phi_0`$ is unclear **[inferred]**.

```python
r0, phi0, h = 2.0, np.pi/6, 1e-6            # phi0 [inferred]
xy = lambda r, phi: np.array([r*np.cos(phi), r*np.sin(phi)])

J_an = np.array([[np.cos(phi0), -r0*np.sin(phi0)],
                 [np.sin(phi0),  r0*np.cos(phi0)]])
J_num = np.column_stack([(xy(r0+h, phi0) - xy(r0, phi0))/h,
                         (xy(r0, phi0+h) - xy(r0, phi0))/h])
print(np.round(J_an, 4)); print(np.round(J_num, 4))
print(np.linalg.det(J_an))                  # = r0 = 2
```

---

### 2.8 The Hessian

**Analogy.** If the gradient/Jacobian tells you the slope of the hill, the Hessian tells you its curvature.

**Definition.** The matrix of second derivatives, equivalently the Jacobian of the gradient:

```math
H_{jk} = \frac{\partial^2 L}{\partial \theta_j\, \partial \theta_k}
```

**Classifying a critical point** (where $`\nabla L = 0`$):

| Eigenvalues of $`H`$ | Point type | Shape |
|---|---|---|
| All $`> 0`$ | Local **minimum** | Convex bowl |
| All $`< 0`$ | Local **maximum** | Peak |
| Mixed signs | **Saddle point** | Curves up in one direction, down in another |

In 1-D this reduces to: $`f'' > 0`$ means a minimum, $`f'' < 0`$ means a maximum.

**Saddle point (definition given):** a spot on a surface that is completely flat at its exact centre, but curves upward in one direction and downward in the other.

**Uses of the Hessian:**
1. **Largest stable learning rate:**

   $`\displaystyle \eta < \frac{2}{\lambda_{\max}(H)}`$

   This explains the divergence seen in the Hubble example.
2. **Parameter uncertainty:** a sharp curvature of the NLL means a precise estimate.

   $`\displaystyle \sigma_\theta \approx \frac{1}{\sqrt{H}} \quad\text{(1-D)}, \qquad \mathrm{Cov}(\hat\theta) \approx H^{-1}`$

**Poisson example (continuing §2.5).** The Hessian of the NLL is

```math
H = \frac{d^2L}{d\lambda^2} = \frac{\sum k_i}{\lambda^2}
```

At $`\hat\lambda`$ this equals $`n/\hat\lambda`$, so

```math
\sigma_\lambda = \sqrt{\frac{\hat\lambda}{n}} = \sqrt{\frac{4}{5}} \approx 0.89\ \text{photons/s}
```

This matches the lecture's "0.89 per second" and confirms $`n = 5`$ and $`\hat\lambda = 4`$.

#### Worked example 9: Hessian of the Gaussian star image at its centre

At $`(x_0, y_0)`$:

```math
H_I = -\frac{A}{\sigma^2}\begin{pmatrix}1 & 0\\ 0 & 1\end{pmatrix}
```

Both eigenvalues are negative, so the centre is a **maximum** (the star peak). For $`-\ln I`$ (the quantity you would minimise), $`H = \frac{1}{\sigma^2}\mathbf{1}`$, which is positive: a minimum.

```python
def hessian_num(f, x, y, h=1e-4):
    fxx = (f(x+h,y) - 2*f(x,y) + f(x-h,y)) / h**2
    fyy = (f(x,y+h) - 2*f(x,y) + f(x,y-h)) / h**2
    fxy = (f(x+h,y+h) - f(x+h,y-h) - f(x-h,y+h) + f(x-h,y-h)) / (4*h**2)
    return np.array([[fxx, fxy], [fxy, fyy]])

Hc = hessian_num(I, x0, y0)
print(Hc, np.linalg.eigvalsh(Hc))          # both negative -> maximum
```

**3-D plots shown:**
- the Gaussian peak (maximum)
- a convex bowl (minimum)
- a saddle surface

---

## 3. Functions, Keywords, Operators and Built-ins Used

| Item | What it does |
|---|---|
| `lambda x: ...` | Anonymous one-line function, used to define $`f(x)`$, $`I(x,y)`$, etc. |
| `**` | Exponent operator (`(x-3)**2`). Note that `^` in Python is XOR, not a power. |
| `for ... in range(n):` | Loop used for gradient-descent iterations. |
| `np.array` | Create NumPy arrays (data, gradient vectors, matrices). |
| `np.linspace(a, b, n)` | $`n`$ evenly spaced points from $`a`$ to $`b`$, for plotting curves. |
| `np.arange(a, b, step)` | Evenly spaced values with a fixed step (e.g. the $`-3`$ to $`3`$ pixel grid). |
| `np.meshgrid` | Builds 2-D coordinate grids for surfaces, contours and quiver plots. |
| `np.exp`, `np.log`, `np.log10` | Elementwise $`e^x`$, $`\ln x`$, $`\log_{10} x`$. |
| `np.sqrt`, `np.pi`, `np.cos`, `np.sin` | Square root, $`\pi`$, and trig functions. |
| `np.sum`, `np.mean` | Sum and average over array elements (losses, closed-form estimates). |
| `np.round(a, 4)` | Round to 4 decimals, used for printing Jacobians. |
| `np.linalg.det` | Determinant of a matrix ($`\det J`$). |
| `np.linalg.eigvalsh` / `np.linalg.eig` | Eigenvalues, used to classify a Hessian. `eigvalsh` is for symmetric matrices. |
| `np.random.default_rng` / `rng.normal` / `rng.poisson` | Simulate data **[the exact calls used are inferred]**. |
| `scipy.optimize.minimize_scalar` | Numerically minimise a 1-D function (Poisson NLL check). |
| `sp.symbols` | Declare SymPy symbolic variables. |
| `sp.diff(expr, var)` | Symbolic differentiation ("diff command"). |
| `plt.plot`, `plt.legend`, `plt.show` | Line plots (functions, tangents, loss curves). |
| `plt.quiver(X, Y, U, V)` | Arrow plot of a gradient field (arrows pointing to the star). |
| `plt.contour` / 3-D surface plot | Visualise $`I(x,y)`$, bowls and saddles **[inferred]**. |

---

## 4. Syntax Rules, Common Mistakes and Debugging Tips

- **Always gradient-check.** Compare analytic derivatives with finite differences, $`\frac{f(x+h)-f(x)}{h}`$. The instructor did this for every example: $`f'(5)`$, $`\partial F/\partial L`$, $`\partial I/\partial x`$, the logistic gradient, and the Jacobian.
- **Choosing $`h`$:** too large gives truncation error; too tiny gives floating-point round-off. Values around $`10^{-5}`$ to $`10^{-6}`$ were used. A central difference, $`\frac{f(x+h)-f(x-h)}{2h}`$, is more accurate.
- **Learning rate:**
  - Too large ($`\eta = 3.5\times10^{-4}`$ in the Hubble demo) makes gradient descent diverge or oscillate.
  - Too small converges slowly.
  - The safe bound is $`\eta < 2/\lambda_{\max}(H)`$.
- **Vanishing gradients:** when the function is nearly flat (e.g. $`I \approx 0`$ far from the star), the gradient is ≈ 0 and the optimiser stalls. Work with the log ($`\nabla \ln I`$, log-likelihood) instead.
- **Maximise likelihood = minimise NLL.** Optimisers minimise, so negate the log-likelihood.
- **$`\nabla L = 0`$ is not automatically a minimum.** Check the Hessian eigenvalues: it could be a maximum or a saddle.
- **Log-loss tip** (general good practice, not stated in lecture): clip $`p`$ to $`[\epsilon, 1-\epsilon]`$ before `np.log` to avoid `log(0)`.

---

## 5. Exam / Assignment Notes and Admin

- **No explicit exam or assignment items were flagged in this session.**
- The concepts the session was built around, and that are most likely testable:
  - the derivative definition
  - error propagation, $`\sigma_f \approx |f'|\sigma_x`$
  - the gradient descent update, $`\theta_{t+1} = \theta_t - \eta\nabla L`$
  - MLE by setting $`dL/d\theta = 0`$ (e.g. Poisson $`\hat\lambda = \bar k`$; Hubble $`\hat H_0 = \sum d_i v_i / \sum d_i^2`$)
  - the chain-rule gradient for logistic regression, $`(p-y)x`$
  - the Jacobian and its determinant for the polar transform ($`\det J = r`$)
  - Hessian classification of critical points, and $`\eta < 2/\lambda_{\max}`$
- **Admin:**
  - Slides and notebooks will be uploaded by tomorrow.
  - Students requested:
    1. notebooks from previous lectures (missing so far)
    2. practice questions or a practice sheet on these topics
    3. layman or industry examples (sales, procurement, production) in addition to the astronomy examples, showing how tools like Jacobians and vector calculus apply to real problems
  - The instructor asked for suggestions on example types and said future material may be prepared accordingly.

<!-- nav -->
← [Session 18 (2026-11-02)](DSM-102-18_2026-11-02_Abhirup-Datta.md) · [All lectures](./) · [Session 20 (2026-11-14)](DSM-102-20_2026-11-14_Abhirup-Datta.md) →
<!-- /nav -->
