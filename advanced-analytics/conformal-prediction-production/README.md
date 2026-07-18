# Conformal Prediction Intervals for Production Forecasts

## 1. Problem Statement
Point forecasts of well performance are routinely wrong, and most "uncertainty"
attached to them is heuristic. Decision-makers need intervals with a guarantee: "the
true value lands inside 90% of the time." **Split conformal prediction** delivers
exactly that — distribution-free, model-agnostic, and a few lines of code — yet it is
barely known in petroleum analytics.

**Operational Impact:**
* **Type curves & acquisitions:** Valuations hinge on honest P10/P90s, not vibes.
* **Any model, wrapped:** Works around whatever forecaster a team already has.

## 2. Solution Overview
A Gradient Boosting model predicts 12-month cumulative production from well/completion
features. **Split conformal** calibrates residual quantiles on a held-out set to build
intervals with guaranteed marginal coverage — verified empirically. **Conformalized
quantile regression (CQR)** then fixes the constant-width limitation, adapting interval
width to each well's difficulty.

## 3. Fundamental Physics & Features
* **Heteroscedasticity:** Bigger completions have bigger absolute uncertainty — CQR's
  motivation.
* **Coverage guarantee:** Finite-sample, distribution-free — the math holds regardless
  of the model being wrong.

**Algorithm:** Split conformal + CQR on Gradient Boosting; coverage & width audits.
**Libraries:** Scikit-Learn, Numpy, Matplotlib.

## 4. Repository Structure
* `well_cum12_data.csv`: Synthetic well-level features and 12-mo cums.
* `Conformal_Prediction_Production.ipynb`: Split conformal, CQR, audits.
* `requirements.txt`: List of dependencies.
