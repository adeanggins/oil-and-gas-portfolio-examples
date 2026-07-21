# CO2 Storage Capacity Screening: Probabilistic Estimate

## 1. Problem Statement
CCS projects begin with storage capacity screening across candidate saline aquifers.
Deterministic volumetric estimates hide the dominant uncertainty — the storage
efficiency factor spans an order of magnitude — and screening also requires an
injectivity check: capacity you cannot inject into on schedule is stranded.

**Operational Impact:**
* **Site selection:** Ranking errors at screening stage cost years of appraisal.
* **Bankability:** Regulators and investors expect probabilistic (P10/P50/P90) statements.

## 2. Solution Overview
**Monte Carlo volumetrics** (mass capacity = A·h·φ·ρCO2·E) with literature-shaped
distributions per aquifer, plus a simplified **radial injectivity model** to estimate
achievable annual rates. Candidates are ranked on **effective capacity** — the minimum
of volumetric capacity and 30-year injectable volume — with tornado sensitivity.

## 3. Fundamental Physics & Features
* **CO2 density at depth:** Supercritical density from a P-T proxy of depth.
* **Efficiency factor E:** Beta-distributed (1–6%), the dominant screening uncertainty.
* **Injectivity:** Darcy radial flow with pressure constrained below fracture gradient.

**Algorithm:** Monte Carlo + rank correlation sensitivity (tornado).
**Libraries:** Numpy, Seaborn, Pandas, Matplotlib.

## 4. Repository Structure
* `aquifer_candidates.csv`: Screening parameters for 5 candidate stores.
* `CO2_Storage_Capacity.ipynb`: MC capacity, injectivity, ranking, tornado.
* `requirements.txt`: List of dependencies.
