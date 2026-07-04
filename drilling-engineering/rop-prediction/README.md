# Rate of Penetration (ROP) Prediction with Random Forest

## 1. Problem Statement
Rate of Penetration (ROP) is the single largest lever on drilling cost: a well that
drills 20% faster saves days of rig spread rate. ROP depends on a tangled mix of
controllable parameters (WOB, RPM, flow rate) and uncontrollable ones (formation
strength, depth, bit condition), so simple lookup tables and single-variable rules
leave performance on the table.

**Operational Impact:**
* **Cost:** Rig spread rates of $150k+/day make every extra hour of rotating time expensive.
* **Planning:** Reliable ROP models improve AFE time estimates and offset-well benchmarking.

## 2. Solution Overview
This project trains a **Random Forest Regressor** on physics-inspired synthetic drilling
data (Bourgoyne–Young style response surface) and benchmarks it against multiple linear
regression. A key detail is the use of **well-grouped train/test splitting** (GroupShuffleSplit)
so the model is evaluated on unseen wells — the honest test for drilling analytics.

## 3. Fundamental Physics & Features
* **WOB & RPM:** Primary energy inputs; ROP responds sub-linearly and interacts with formation strength.
* **UCS (rock strength):** Stronger rock drills slower; effect is non-linear.
* **Overbalance (ECD - pore pressure):** Chip hold-down effect suppresses ROP.
* **Bit wear fraction:** Dull bits lose aggressiveness; interacts with WOB.

**Algorithm:** Random Forest Regression with permutation feature importance.
**Libraries:** Scikit-Learn, Pandas, Seaborn, Matplotlib.

## 4. Repository Structure
* `rop_drilling_data.csv`: Synthetic drilling parameter dataset (8 wells, 3 formations).
* `ROP_Prediction.ipynb`: Data generation, EDA, model training and sensitivity analysis.
* `requirements.txt`: List of dependencies.
