# Sand Production Risk Classification with Imbalanced Learning

## 1. Problem Statement
Sand production erodes chokes and flowlines, fills separators and can kill wells.
Predicting which wells will sand — before pulling rates or installing screens — is a
classification problem with a structural difficulty: sanding events are rare, so naive
models score 95% accuracy by predicting "no sand" always.

**Operational Impact:**
* **Erosion & HSE:** Sand in high-rate gas wells cuts out chokes within days.
* **Capex triage:** Screens/gravel packs cost millions; installing them everywhere wastes it.

## 2. Solution Overview
A **class-weighted Random Forest** predicts sanding risk from rock strength, drawdown,
water cut and completion type. The notebook demonstrates the imbalanced-learning
toolkit: **precision-recall analysis (not ROC), class weights, threshold tuning** to an
operations-driven recall target, and probability calibration.

## 3. Fundamental Physics & Features
* **Rock strength (UCS/TWC):** Weak sandstone fails at lower stress.
* **Drawdown & depletion:** Effective stress at the perforation drives failure.
* **Water breakthrough:** Capillary cohesion loss — the classic sanding trigger.

**Algorithm:** Class-weighted Random Forest + threshold tuning at target recall.
**Libraries:** Scikit-Learn, Seaborn, Matplotlib.

## 4. Repository Structure
* `sanding_well_data.csv`: Synthetic well dataset with sanding outcomes (7% positive).
* `Sand_Production_Prediction.ipynb`: Imbalance handling, PR analysis, decision support.
* `requirements.txt`: List of dependencies.
