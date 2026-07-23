# Facility CAPEX Estimation with Log-Target Machine Learning

## 1. Problem Statement
Early-phase facility cost estimates lean on capacity-factored scaling ("the six-tenths
rule") from analogue projects. These carry ±40% bands, and cost overruns trace back to
features the scaling law ignores: location, sourness, execution complexity, brownfield
tie-ins. Cost datasets are also heavily right-skewed — a modeling trap.

**Operational Impact:**
* **Screening decisions:** ±40% at concept select kills or anoints projects wrongly.
* **Contingency setting:** Estimate error distributions set contingency levels.

## 2. Solution Overview
A **Random Forest trained on log(CAPEX)** — errors in cost estimation are
multiplicative, so the log transform aligns the loss with reality — benchmarked
against the classical capacity-factor method on the same analogue set. Errors are
reported in **percentage space** (the estimator's language), with a bias check after
back-transformation.

## 3. Fundamental Physics & Features
* **Capacity factor:** C2 = C1·(S2/S1)^0.6 — the industry's default prior.
* **Cost drivers:** capacity, sour service (metallurgy), location factor, brownfield
  flag, water depth, execution year (escalation).

**Algorithm:** Log-target Random Forest vs. capacity-factored baseline; smearing
back-transform bias correction.
**Libraries:** Scikit-Learn, Seaborn, Matplotlib.

## 4. Repository Structure
* `facility_cost_history.csv`: Synthetic analogue project database.
* `CAPEX_Cost_Estimation.ipynb`: Baseline, log-RF, error analysis.
* `requirements.txt`: List of dependencies.
