# Choke Flow Rate Prediction: Gilbert Correlation vs. Machine Learning

## 1. Problem Statement
Wellhead chokes control rate and protect equipment, and choke-based rate estimation is
the fallback whenever test separators are unavailable. Gilbert-type correlations
(q = C·P_wh·d^a / GLR^b) work in critical flow but degrade badly in subcritical
conditions and outside their calibration envelope.

**Operational Impact:**
* **Allocation:** Choke-estimated rates feed daily allocation when tests are sparse.
* **Integrity:** Rate errors mislead erosion (sand) and slugging assessments.

## 2. Solution Overview
Both approaches are calibrated on the same synthetic well test dataset spanning
critical and subcritical flow: a **tuned Gilbert correlation** (log-space least squares)
and a **Gradient Boosting regressor** with the pressure ratio as an extra feature.
The comparison isolates *where* ML helps (subcritical regime) and where the correlation
is already sufficient.

## 3. Fundamental Physics & Features
* **Critical flow:** Downstream pressure ceases to matter above ~0.5 pressure ratio —
  Gilbert's regime.
* **Subcritical flow:** Rate depends on the pressure differential — invisible to Gilbert.
* **Features:** WHP, downstream pressure, choke size, GLR, water cut.

**Algorithm:** Tuned Gilbert correlation vs. Gradient Boosting, regime-wise evaluation.
**Libraries:** Scikit-Learn, Seaborn, Matplotlib.

## 4. Repository Structure
* `choke_test_data.csv`: Synthetic well test dataset across flow regimes.
* `Choke_Rate_Prediction.ipynb`: Correlation tuning, ML, regime analysis.
* `requirements.txt`: List of dependencies.
