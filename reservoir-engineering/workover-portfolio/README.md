# Well Workover Portfolio Optimization

## Problem Statement
In mature field management, engineers often identify more candidates for stimulation, rig workovers, or pump replacements than the budget allows. The challenge is to select the specific subset of well interventions that results in the **maximum total incremental production** without exceeding a **fixed financial budget**.

This is a classic combinatorial optimization problem that can be solved using **Linear Programming (LP)**.

## The Solution
This repository utilizes Python and the **PuLP** library to mathematically model the selection process.

### Mathematical Formulation
We treat this as a Binary Integer Programming problem:
* **Decision Variable ($x_i$):** A binary variable where $1$ means we select Well $i$, and $0$ means we do not.
* **Objective Function:** Maximize total Production Gain ($P$).
    $$\text{Maximize } Z = \sum_{i=1}^{n} (Gain_i \times x_i)$$
* **Constraint:** Total Cost must be less than or equal to Budget ($B$).
    $$\sum_{i=1}^{n} (Cost_i \times x_i) \leq B$$

## Repository Contents
* `well_candidates.csv`: Contains sample CSV data of well candidates, costs, and estimated gains.
* `Well_Portfolio_Optimization.ipynb`: Jupyter notebook demonstrating the step-by-step optimization process.
* `requirements.txt`: Python dependencies.
