# Chan Plot Diagnostic Tool for Water Breakthrough Analysis

## 📌 Problem Statement
In water-drive reservoirs, distinguishing between **water coning** and **water channeling** (high-permeability layers) is critical for selecting the correct remediation strategy (e.g., chemical shut-off vs. reduced production rates). Traditional decline curve analysis often fails to differentiate these mechanisms early.

## 💡 Solution
This repository contains a Python-based diagnostic tool based on the **Chan Plot** methodology (Chan, 1995). By analyzing the Water-Oil Ratio (WOR) and its derivative against Cumulative Oil Production ($N_p$) on a log-log scale, we can identify the flow regime based on the slope of the curve.

## 📐 Fundamental Theory

 The Chan diagnostic relies on the power-law relationship between WOR and cumulative production:

$$WOR = A \cdot N_p^b$$

Where:
* $WOR$: Water-Oil Ratio (stb/stb)
* $N_p$: Cumulative Oil Production (stb)
* $b$: The derivative slope (Diagnostic Indicator)

By taking the logarithm:
$$\log(WOR) = \log(A) + b \cdot \log(N_p)$$

### Interpretation of Slope ($b$):
We calculate the derivative of the WOR with respect to Cumulative Production. The slope behavior on a log-log plot indicates the mechanism:

1.  **Water Channeling:** Characterized by a rapid increase in WOR. The WOR and its derivative curves often exhibit a **constant positive slope** (approximately straight lines) on the log-log plot.
2.  **Water Coning:** Initially follows a similar trend to channeling but typically exhibits a **gradually changing slope** (often a negative derivative slope at late times) as the cone stabilizes or gravity drainage assists.

## 📂 Repository Structure
* `chan_plot_analysis.ipynb`: The Jupyter Notebook containing the calculation and visualization logic.
* `production_data.csv`: Sample dataset containing Cumulative Production and WOR history.
* `README.md`: Project documentation.

## 🚀 Usage
1.  Clone the repo.
2.  Ensure you have `pandas`, `matplotlib`, and `numpy` installed.
3.  Run the Jupyter Notebook to visualize the diagnostic plot.
