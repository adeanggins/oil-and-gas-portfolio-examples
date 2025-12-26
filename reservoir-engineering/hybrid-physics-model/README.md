# Hybrid Physics-ML Calibration: Calibrating Standing Correlation with Residual Learning

## 1. Problem Statement
Empirical correlations like **Standing (1947)** are general approximations. They provide a robust baseline but often fail to capture the specific nuances of a unique reservoir, leading to systematic errors (bias).
* **Pure Physics Approach:** Using Standing alone often yields high error (e.g., MAPE > 15%).
* **Pure ML Approach:** Training a model from scratch requires massive data and risks "hallucinating" unphysical results outside the training range.

## 2. Solution: The Hybrid "Residual Learning" Approach
Instead of discarding the physics, we use Machine Learning to **fix the error** of the physics equation.

$$
P_{b,\text{Final}} = P_{b,\text{Standing}} + f_{\text{ML}}(\text{Residual})
$$

**Workflow:**
1.  **Physics Baseline:** Calculate Bubble Point Pressure ($P_b$) using the Standing Correlation.
2.  **Residual Calculation:** Determine where the physics failed ($Error = P_{b,\text{Lab}} - P_{b,\text{Standing}}$).
3.  **ML Correction:** Train a Random Forest to predict *only* this error based on inputs (Temp, API, Gas Gravity).
4.  **Hybrid Prediction:** Add the ML correction back to the Standing result.

## 3. Results
This approach typically reduces error significantly while ensuring the model retains physical interpretability.
