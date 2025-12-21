# 🛢️ Automated Decline Curve Analysis (DCA)
### **Physics-Informed Production Forecasting**

This repository implements an automated **Decline Curve Analysis (DCA)** engine using Python. It leverages **Scipy** for non-linear optimization.

Unlike standard curve-fitting scripts, this tool applies **physics-based constraints** (e.g., limiting the b-factor) to ensure forecasts are not just mathematically convenient, but geologically realistic.
---

## 🚀 Key Features

* **Automated Curve Fitting:** Uses `scipy.optimize.curve_fit` to minimize residuals between production data and Arps' equations.
* **Physics Constraints:** Applies boundary constraints to optimization parameters to prevent non-physical results (e.g., negative decline rates or infinite reserves).
* **Plot Visualization:** A Visualization on how the code run to do curve fitting, and EUR (Estimated Ultimate Recovery) forecasts.
* **Outlier Detection:** Pre-processing pipeline to filter out "shut-in" periods ($q=0$) and transient sensor noise before fitting.

---

## 📐 Mathematical Methodology

The core engine utilizes **Arps' Hyperbolic Decline Equation**, the industry standard for reservoir forecasting.

$$q(t) = \frac{q_i}{(1 + b D_i t)^{1/b}}$$

Where:
* **$q(t)$**: Production rate at time $t$
* **$q_i$**: Initial production rate (optimized)
* **$D_i$**: Initial nominal decline rate (optimized)
* **$b$**: Hyperbolic decline exponent

### Optimization Strategy
The model minimizes the **Root Mean Square Error (RMSE)** between the actual rate and the theoretical Arps rate. To ensure stability, we use the **Trust Region Reflective (Trf)** algorithm which allows for strict parameter bounds:

1.  **$q_i$**: Must be positive ($>0$).
2.  **$D_i$**: Must be positive and physically realistic ($0 < D_i < 5.0$ / year).
3.  **$b$**: User-constrained (Default: $0.0 \le b \le 1.0$ for boundary-dominated flow).

---

## 🛠️ Tech Stack

* **Core Logic:** `Python 3.10`, `NumPy`, `SciPy`
* **Data Manipulation:** `Pandas`
* **Visualization:** `Seaborn`, `Matplotlib`
