# Internal Corrosion Rate Prediction: de Waard Model + Random Forest

## 1. Problem Statement
CO2 (sweet) corrosion is the dominant internal degradation mechanism in carbon-steel
flowlines. Inspection pigs measure wall loss only every few years, so operators rely on
corrosion-rate models between runs to prioritize inspection and chemical spend. The
classical de Waard–Milliams correlation captures core physics but misses water
chemistry, flow-regime and inhibition effects.

**Operational Impact:**
* **Integrity:** Under-predicted corrosion becomes a leak; over-predicted wastes
  inspection budget.
* **Chemical optimization:** Inhibitor dosing rides on predicted rates.

## 2. Solution Overview
The **de Waard–Milliams baseline** is implemented from CO2 partial pressure and
temperature, then a **Random Forest** adds water chemistry, velocity and inhibitor
features. Validation against measured (synthetic) UT wall-loss rates shows where the
physics correlation needs help, echoing the hybrid pattern used across this portfolio.

## 3. Fundamental Physics & Features
* **de Waard–Milliams:** log CR = 5.8 − 1710/T + 0.67·log(pCO2) — the industry baseline.
* **Modifiers:** chlorides, bicarbonate (scaling films), velocity (mass transfer/erosion
  of films), inhibitor availability, water cut (oil wetting).

**Algorithm:** Physics baseline + Random Forest, feature importance, criticality ranking.
**Libraries:** Scikit-Learn, Seaborn, Matplotlib.

## 4. Repository Structure
* `corrosion_survey_data.csv`: Synthetic line-segment corrosion dataset.
* `Corrosion_Rate_Prediction.ipynb`: Baseline, ML, comparison, criticality matrix.
* `requirements.txt`: List of dependencies.
