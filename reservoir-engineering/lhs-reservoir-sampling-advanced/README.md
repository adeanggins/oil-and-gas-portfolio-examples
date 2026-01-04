# Advanced Reservoir Sensitivity Analysis: LHS with Correlation Control

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Scipy](https://img.shields.io/badge/SciPy-Stats-orange)
![Status](https://img.shields.io/badge/Status-Expert%20Demo-green)

## 📌 Executive Summary
This repository implements an advanced **Design of Experiments (DoE)** workflow for Reservoir Simulation. unlike standard Monte Carlo or basic Latin Hypercube implementations, this tool utilizes the **Iman-Conover Method** to enforce geological correlations (e.g., Porosity vs. Permeability) while preserving the stratification efficiency of Latin Hypercube Sampling.

This approach addresses the "Unphysical Combination" problem in reservoir modeling, ensuring that sensitivity analysis runs are both statistically efficient and geologically realistic.

## 🚧 The Problem: "Garbage In, Garbage Out"
In reservoir simulation, uncertainty parameters are rarely independent.
* **High Porosity** generally implies **High Permeability**.
* **High Water Saturation** is often correlated with **Low Permeability** (Rock Quality).

**Standard Sampling Failures:**
1.  **Monte Carlo (MCS):** Requires thousands of runs to converge; samples often cluster, leaving "gaps" in the uncertainty space.
2.  **Basic Latin Hypercube (LHS):** Efficiently covers the range (Marginals) but treats variables as independent (creates "High Porosity / Low Perm" realizations that are physically impossible).

## 💡 The Solution: LHS + Iman-Conover
This repository combines two powerful statistical concepts:



1.  **Latin Hypercube Sampling (LHS):**
    * Divides the CDF into $N$ intervals of equal probability.
    * Ensures the entire range of uncertainty is sampled with fewer runs ($O(1/N)$ variance reduction compared to MCS).

2.  **Iman-Conover Rank Re-ordering (1982):**
    * A distribution-free method to induce rank correlation.
    * **The Logic:** We generate a "target" correlation structure using Gaussian copulas (Cholesky decomposition). We then simply *re-shuffle* our stratified LHS samples so their rank order matches the target structure.
    * **The Result:** Perfect marginal distributions (LHS) + Realistic dependencies (Correlation).

## 🛠️ Repository Workflow

### 1. Configuration (`parameters.csv` / Config Dict)
We define uncertainty distributions and a **Target Correlation Matrix**:
$$
\rho = \begin{bmatrix} 
1.0 & 0.8 & -0.4 \\
0.8 & 1.0 & -0.6 \\
-0.4 & -0.6 & 1.0 
\end{bmatrix}
$$

### 2. The Engine (`lhs_advanced_workflow.ipynb`)
The core algorithm follows these steps:
1.  **Generate LHS:** Create $N$ samples in the unit hypercube $[0,1]^d$.
2.  **Iman-Conover Transformation:**
    * Map Unit samples to Normal Scores ($Z$).
    * Apply Cholesky Decomposition ($L$) to induce correlation: $Z_{corr} = Z \cdot L^T$.
    * Re-order original LHS samples to match the rank of $Z_{corr}$.
3.  **Inverse Transform Sampling:** Convert $[0,1]$ samples to physical units (mD, ft, %) using `scipy.stats.ppf`.
4.  **QC & Validation:** Calculate the Spearman Rank Correlation of the output to verify it matches the input matrix.

### 3. Simulation & Analytics
* **Mock Simulator:** A physics-based proxy function calculates *Recoverable Reserves* based on the input parameters.
* **Sensitivity Analysis:** A Tornado Plot is generated using standardized linear regression coefficients to identify the "Heavy Hitters" (key drivers) of production.

## 📊 Visualizations included
The notebook generates:
* **Correlation Heatmaps:** Input vs. Output correlation verification.
* **Cross-Plots:** Visual confirmation of Porosity/Permeability trends.
* **Tornado Plots:** Ranking parameters by their impact on the objective function.

## 📜 References
- Iman, R. L., & Conover, W. J. (1982). A distribution-free approach to inducing rank correlation among input variables.
- McKay, M. D., Beckman, R. J., & Conover, W. J. (1979). A comparison of three methods for selecting values of input variables in the analysis of output from a computer code.

## 🚀 Usage

### Prerequisites
Install dependencies via `requirements.txt`:
```bash
pip install -r requirements.txt
