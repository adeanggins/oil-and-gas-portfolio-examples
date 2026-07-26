# Separator Liquid Carryover Prediction

## 1. Problem Statement
Liquid carryover from production separators floods downstream compression, ruins gas
quality and triggers plant trips. Carryover events look sporadic to operators, but
they cluster around identifiable conditions: inlet momentum surges, foaming crude,
level-control excursions and demister overload.

**Operational Impact:**
* **Compressor damage:** Liquid slugs into compression are a catastrophic event.
* **Chemical spend:** Anti-foam is often dosed blind at fixed rates.

## 2. Solution Overview
A **Gradient Boosting classifier** predicts carryover events from separator operating
data, with **partial dependence plots** revealing the operating envelope — inlet
momentum and level thresholds — that engineering can act on. Time-based splitting
avoids leaking future operating regimes into training.

## 3. Fundamental Physics & Features
* **Inlet momentum (ρv²):** The Souders-Brown/API 12J sizing criterion — carryover
  rises sharply past design momentum.
* **Liquid level:** High level shrinks gas residence time and demister margin.
* **Foaming tendency:** Crude-specific; interacts with residence time.

**Algorithm:** Gradient Boosting classification + PDP-based envelope extraction.
**Libraries:** Scikit-Learn, Seaborn, Matplotlib.

## 4. Repository Structure
* `separator_operating_data.csv`: Synthetic hourly separator data with events.
* `Separator_Carryover_Classification.ipynb`: Model, PDPs, envelope, alarm design.
* `requirements.txt`: List of dependencies.
