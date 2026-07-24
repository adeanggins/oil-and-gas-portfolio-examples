# EUR Uncertainty with Gradient Boosting Quantile Regression

## 1. Problem Statement
Reserves reporting runs on P10/P50/P90, yet most ML EUR models output a single number
and bolt uncertainty on afterwards. **Quantile regression** learns the conditional
quantiles directly — different features can widen or narrow the distribution — which is
exactly how geology behaves: EUR uncertainty in a faulted area is not the uncertainty
of a layer-cake area.

**Operational Impact:**
* **Reserves categories:** P90 (proved-style thinking) drives lending; P10 drives upside.
* **Well ranking under risk:** Ranking on P90 vs P50 changes drilling order.

## 2. Solution Overview
Three **Gradient Boosting regressors with pinball loss** (α = 0.1, 0.5, 0.9) predict
conditional EUR quantiles from geological and completion features. The notebook
validates **calibration** (do 10% of wells actually fall below P90?), fixes **quantile
crossing**, and shows how the P10/P90 ratio — a reserves-audit staple — varies across
the field.

## 3. Fundamental Physics & Features
* **Pinball loss:** The asymmetric loss whose minimizer is the conditional quantile.
* **Heteroscedastic geology:** Fault density widens the conditional distribution
  without moving its center much — a pure uncertainty feature.

**Algorithm:** GBM quantile regression trio + calibration audit + crossing fix.
**Libraries:** Scikit-Learn, Seaborn, Matplotlib.

## 4. Repository Structure
* `eur_well_dataset.csv`: Synthetic wells with EUR outcomes.
* `Quantile_Regression_EUR.ipynb`: Models, calibration, P10/P90 mapping.
* `requirements.txt`: List of dependencies.
