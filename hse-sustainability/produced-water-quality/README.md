# Produced Water Reuse Classification with Interpretable Trees

## 1. Problem Statement
Produced water is the industry's largest byproduct stream. Each batch must be routed:
reuse for waterflooding/fracking, treat then reuse, or disposal well. Routing criteria
live in water-management guidelines, but daily decisions are made by operators from
lab reports — inconsistently. A black-box model is not acceptable here: routing
decisions must be auditable against the guidelines.

**Operational Impact:**
* **Disposal cost:** Trucked disposal can cost $1–5/bbl; reuse offsets fresh water.
* **Compliance:** Mis-routed water risks formation damage or permit violations.

## 2. Solution Overview
A **depth-limited decision tree** classifies water batches into routing classes and —
the point of the exercise — its **rules are extracted as human-readable text** and
audited against the true (synthetic) routing logic. Accuracy is compared against a
Random Forest to quantify the interpretability premium.

## 3. Fundamental Physics & Features
* **TDS/chlorides:** Compatibility with target formation and friction reducers.
* **Oil & grease, TSS:** Plugging risk in injection; treatment triggers.
* **Barium/sulfate pair:** BaSO4 scale risk on mixing — an interaction rule.
* **H2S, bacteria:** Souring control requirements.

**Algorithm:** CART decision tree + rule extraction; Random Forest accuracy benchmark.
**Libraries:** Scikit-Learn, Matplotlib.

## 4. Repository Structure
* `produced_water_batches.csv`: Synthetic lab results with routing labels.
* `Produced_Water_Quality.ipynb`: Tree, rules, audit, benchmark.
* `requirements.txt`: List of dependencies.
