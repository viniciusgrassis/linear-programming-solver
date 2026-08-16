# Linear Programming Solver

This project was developed in **Python** for the **Operations Research** course at the Federal University of São João del-Rei (UFSJ), during the **first semester of 2025**.

The goal of the assignment was to implement the **Simplex method from scratch** for solving Linear Programming Problems (LPPs). Mathematical optimization solvers were not allowed; libraries such as NumPy could only be used for data representation and matrix manipulation.

The implementation supports maximization problems with non-negative decision variables and constraints of the following types:

* `≤`
* `≥`
* `=`

When a trivial initial basis is not available, the solver uses the **Big M method** to introduce artificial variables and obtain a feasible basis before proceeding with the Simplex iterations. It also detects infeasible and unbounded problems and checks whether an optimal solution has an alternative optimum.

## Features

* Simplex algorithm implemented from scratch
* Automatic tableau construction
* Slack, surplus and artificial variables
* Big M method for non-trivial initial bases
* Support for `≤`, `≥` and `=` constraints
* Detection of infeasible problems
* Detection of unbounded solutions
* Detection of multiple optimal solutions
* Alternative optimal solution generation
* Text-file input format
* Modular implementation using NumPy arrays

## How It Works

The program follows a pipeline composed of three main stages:

```text
Input Model
    |
    v
Parse coefficients
    |
    v
Build initial tableau
    |
    +----------------------------+
    |                            |
    | trivial initial basis      | artificial variables required
    v                            v
Simplex                      Big M preprocessing
    |                            |
    |                            v
    |                       Simplex
    |                            |
    +-------------+--------------+
                  |
                  v
          Feasibility check
                  |
                  v
          Optimal solution
                  |
                  v
      Multiple optimum check
```

The input is first converted into NumPy vectors and matrices representing:

* objective-function coefficients (`c`);
* constraint matrix (`A`);
* constraint types (`r`);
* right-hand-side values (`b`).

The program then builds the appropriate Simplex tableau.

If all constraints allow a straightforward initial basis, the Simplex method is executed directly.

If `≥` or `=` constraints require artificial variables, the solver applies the **Big M method** before running the Simplex iterations.

For this implementation, `M` is defined as:

```text
M = 100 × largest absolute value in the initial tableau
```

After convergence, the resulting tableau is checked for feasibility and for the existence of alternative optimal solutions.

## Simplex Implementation

The main Simplex procedure is divided into three fundamental operations.

### Entering Variable

The solver examines the objective row and selects a variable whose reduced cost indicates that the objective function can still be improved.

When no improving variable remains, the current tableau is considered optimal.

### Leaving Variable

The leaving variable is determined using the minimum positive ratio between the right-hand-side value and the corresponding positive coefficient in the entering-variable column.

If no valid leaving row exists, the problem is identified as **unbounded**.

### Pivot Operation

The pivot row is normalized by dividing it by the pivot element.

All other rows are then updated using elementary row operations so that the entering-variable column becomes a unit vector.

This process repeats until an optimal tableau is reached.

## Big M Method

Constraints of type `≥` and `=` may require artificial variables to establish an initial feasible basis.

The solver therefore:

1. creates the standard tableau;
2. adds surplus variables when required;
3. adds artificial variables;
4. assigns a Big M penalty to artificial variables in the objective function;
5. adjusts the objective row according to the initial artificial basis;
6. runs the Simplex method normally.

After convergence, the program checks whether an artificial variable remains in the basis with a positive value.

If that happens, the original Linear Programming Problem is considered **infeasible**.

## Multiple Optimal Solutions

After finding an optimal tableau, the solver examines non-basic variables whose reduced cost is approximately zero.

If one is found, the current solution is not unique.

The program then performs an additional pivot operation to obtain and display another extreme point with the same optimal objective value.

## Input Format

The optimization model is read from a text file named:

```text
modelo.txt
```

The file is divided into four sections separated by blank lines:

```text
c1 c2 ... cn

a11 a12 ... a1n
a21 a22 ... a2n
...
am1 am2 ... amn

r1
r2
...
rm

b1
b2
...
bm
```

Where:

* `c` contains the coefficients of the objective function;
* `A` contains the coefficients of the constraints;
* `r` represents the type of each constraint;
* `b` contains the right-hand-side values.

Constraint types are encoded as:

| Value | Constraint |
| ----- | ---------- |
| `0`   | `≥`        |
| `1`   | `≤`        |
| `2`   | `=`        |

The original assignment defined the problems as maximization problems with non-negative variables and non-negative right-hand-side values.

## Example

Consider the following Linear Programming Problem:

### Objective

```text
Maximize:

Z = 6x1 + 4x2 + 2x3
```

### Subject to

```text
3x1 + 2x2 + x3 ≤ 30
 x1 +  x2 + x3 = 15
       x2      ≤ 8

x1, x2, x3 ≥ 0
```

The corresponding `modelo.txt` file is:

```text
6 4 2

3 2 1
1 1 1
0 1 0

1
2
1

30
15
8
```

Run the solver using:

```bash
python3 main.py
```

The program reports the optimal objective value and the values of the original decision variables.

If an alternative optimum exists, the solver also identifies it and performs another pivot operation to display an additional optimal extreme point.

## Possible Results

Depending on the model, the program may report:

### Optimal solution

```text
---/ Solução ótima encontrada /---
Valor ótimo para Z = ...

---/ Variáveis básicas /---

x1 = ...
x2 = ...
...
```

### Feasible solution after Big M preprocessing

```text
Solução viável encontrada.
```

followed by the optimal solution.

### Infeasible problem

```text
Solução inviável.
```

### Unbounded problem

```text
Solucoes ilimitadas.
```

### Multiple optimal solutions

```text
Múltiplas soluções:
```

followed by another optimal solution obtained through an alternative pivot.

## Project Structure

```text
.
├── main.py
├── modelo.txt
├── README.md
│
├── tratamento_entrada/
│   ├── carregar_entrada.py
│   └── criar_tableau.py
│
├── metodo_principal/
│   ├── simplex.py
│   ├── big_m_create.py
│   ├── big_m_checker.py
│   └── multi_solution_checker.py
│
└── tratamento_saida/
    └── apresentar_solucao.py
```

### `tratamento_entrada`

Responsible for parsing the input model and building the initial tableau.

#### `carregar_entrada.py`

Reads `modelo.txt` and converts its sections into the vectors and matrices `c`, `A`, `r` and `b`.

#### `criar_tableau.py`

Determines the required slack, surplus and artificial variables and builds the initial tableau.

### `metodo_principal`

Contains the optimization logic.

#### `simplex.py`

Implements:

* entering-variable selection;
* leaving-variable selection;
* pivot operations;
* the iterative Simplex procedure.

#### `big_m_create.py`

Builds and adjusts the initial tableau when artificial variables are required.

#### `big_m_checker.py`

Checks whether the final Big M solution is feasible by verifying the values associated with artificial variables.

#### `multi_solution_checker.py`

Checks the final objective row for non-basic variables with zero reduced cost, indicating the existence of another optimal solution.

### `tratamento_saida`

Responsible for presenting the final solution.

#### `apresentar_solucao.py`

Extracts and displays:

* the optimal objective value;
* the values of the original decision variables;
* alternative optimal solutions when applicable.

### `main.py`

Coordinates the complete workflow:

```text
Load model
   ↓
Inspect constraint types
   ↓
Build standard or Big M tableau
   ↓
Run Simplex
   ↓
Check feasibility
   ↓
Display optimal solution
   ↓
Check for alternative optima
```

## Requirements

* Python 3
* NumPy

Install NumPy with:

```bash
pip install numpy
```

Then run:

```bash
python3 main.py
```

The model to be solved must be stored in `modelo.txt`.

## Scope and Limitations

The implementation follows the assumptions established by the original assignment:

* objective functions are maximized;
* decision variables are non-negative;
* right-hand-side values are non-negative;
* input models are provided directly through their coefficients;
* no external mathematical solver is used.

The assignment required the program to handle non-trivial initial bases and identify alternative optimal solutions when they exist.

The project is intended as an educational implementation of the Simplex method and its supporting techniques rather than a replacement for production-grade optimization libraries.

## Academic Context

Developed for the **Operations Research** course of the Computer Science undergraduate program at **UFSJ — Federal University of São João del-Rei**, during the first semester of 2025.

The project focused on translating Linear Programming concepts into a complete computational implementation, including tableau construction, basis management, pivoting, feasibility handling and optimal-solution analysis.
