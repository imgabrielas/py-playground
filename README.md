# Python Mathematical Visualisations

A collection of Python projects exploring mathematics, recursion, fractals, and generative art through code.

---

## About

The projects in this repository transform mathematical formulas and recursive algorithms into visual outputs. They range from parametric curves and chaotic sequences to recursive fractal-like drawings.

---

## Projects

### Oscillating Heart

A heart-shaped curve generated using trigonometric functions, square roots, and mathematical constants.

**Formula**

```text
y = sin(π³x) · √(e²/2 − x²/2) + √|x|
```

**Technologies**

* NumPy
* Matplotlib

---

### Parametric Curve

A smooth parametric curve generated from sine and cosine functions.

**Parametric Equations**

```text
x = √2 · sin³(t)
y = −cos³(t) − cos²(t) + 2cos(t)
```

**Technologies**

* NumPy
* Matplotlib

---

### Hofstadter Chaotic Heart Sequence

A visualisation based on the difference between the Hofstadter Q sequence and Conway sequence.

```text
H(n) = C(n) − Q(n)
```

The resulting scatter plot reveals an unexpected heart-like structure emerging from recursive integer sequences.

**Technologies**

* NumPy
* Matplotlib

---

### Recursive Binary Tree

A recursive tree generated using Turtle Graphics.

Each branch recursively creates smaller branches, producing a fractal-like structure inspired by natural tree growth.

**Technologies**

* Turtle Graphics

---

## Requirements

Install the required libraries:

```bash
pip install numpy matplotlib
```

*Turtle Graphics is included with standard Python installations.*

---

## Author

**imgabrielas**

---

⭐ Feel free to explore the repository and experiment with the code ;))
