# Methane Emission Estimation with Monte Carlo Reconciliation

## 1. Problem Statement
Methane inventories are built bottom-up (component counts × emission factors), yet
aerial and satellite campaigns routinely measure site totals 1.5–3× higher — the
famous top-down/bottom-up gap, driven by fat-tailed super-emitter distributions that
average emission factors cannot represent.

**Operational Impact:**
* **Regulatory exposure:** Methane fees are levied on reported quantities.
* **Mitigation targeting:** Finding super-emitters beats polishing averages.

## 2. Solution Overview
A facility inventory is estimated **bottom-up with Monte Carlo** (lognormal emission
factors per component class, fat-tailed malfunction components), compared against a
simulated **top-down measurement**, and reconciled with **Bayesian updating** of the
malfunction rate. The heavy-tail mathematics of super-emitters is made explicit.

## 3. Fundamental Physics & Features
* **Fat tails:** Component emissions are approximately lognormal; the top 5% of
  leakers dominate the total.
* **Malfunctioning states:** Stuck dump valves and unlit flares emit orders of
  magnitude above design — a mixture model, not a shifted mean.

**Algorithm:** Monte Carlo aggregation + Bayesian reconciliation of mixture weight.
**Libraries:** Numpy, Seaborn, Pandas, Matplotlib.

## 4. Repository Structure
* `component_inventory.csv`: Facility component counts and emission factor parameters.
* `Methane_Emission_Estimation.ipynb`: MC inventory, gap analysis, reconciliation.
* `requirements.txt`: List of dependencies.
