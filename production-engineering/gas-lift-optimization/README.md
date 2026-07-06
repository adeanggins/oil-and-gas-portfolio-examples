# Gas Lift Allocation Optimization across a Well Group

## 1. Problem Statement
A platform has a fixed compressor capacity for lift gas, and every well responds
differently: some gain little from extra gas, others are gas-starved. Equal splitting —
still common in the field — leaves oil in the ground. This is a textbook constrained
allocation problem with diminishing returns.

**Operational Impact:**
* **Immediate oil:** Optimal reallocation typically adds 2–5% production with zero capex.
* **Compressor planning:** The marginal-barrel curve prices incremental compression.

## 2. Solution Overview
Gas lift performance curves (GLPCs) are fit per well from test data, then limited lift
gas is allocated by the **equal-marginal-slope principle** solved with SciPy (SLSQP),
benchmarked against equal split. A sweep over total gas availability produces the
field-level marginal-barrel curve.

## 3. Fundamental Physics & Features
* **GLPC shape:** Oil rate rises with injection gas (lightened column), plateaus, then
  declines (friction dominates) — concave region is where optimization lives.
* **Equal-slope optimum:** At the optimum, all wells operate at the same marginal
  oil-per-gas slope; any transfer between wells then loses oil.

**Algorithm:** Curve fitting + constrained nonlinear optimization (SLSQP).
**Libraries:** Scipy, Pandas, Matplotlib.

## 4. Repository Structure
* `gas_lift_test_data.csv`: Multi-rate gas lift test points per well.
* `Gas_Lift_Optimization.ipynb`: GLPC fitting, allocation optimization, sensitivity.
* `requirements.txt`: List of dependencies.
