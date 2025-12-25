# PVT Correlation Benchmarking: Standing vs. Glaso vs. Vasquez-Beggs

## 1. Problem Statement
In Reservoir Engineering, accurate PVT (Pressure-Volume-Temperature) properties—specifically **Bubble Point Pressure ($P_b$)**, **Solution Gas-Oil Ratio ($R_s$)**, and **Oil Formation Volume Factor ($B_o$)**—are critical for reserves estimation, material balance calculations, and simulation.

However, lab PVT reports are often scarce or limited to specific wells. Engineers rely on empirical correlations to estimate these properties across the field. The challenge is that no single correlation works everywhere; a correlation developed for California crudes (Standing) may fail for North Sea oils (Glaso).

**The Objective:** This project benchmarks three standard industry correlations (Standing, Glaso, Vasquez-Beggs) against actual Lab PVT data to statistically determine which correlation provides the best fit for a specific field.

## 2. Solution Overview
This repository contains a Python-based workflow that:
1.  **Ingests Lab Data:** Loads experimental PVT data (Pressure, Temp, API, Gas Gravity).
2.  **Implements Correlations:** Calculates $P_b$ and $B_o$ using:
    * **Standing (1947):** Based on California crudes.
    * **Glaso (1980):** Based on North Sea oils.
    * **Vasquez-Beggs (1980):** General correlation with huge dataset.
3.  **Statistical Benchmarking:** Compares calculated values vs. lab values using Mean Absolute Percentage Error (MAPE) and Root Mean Squared Error (RMSE).
4.  **Visualization:** Plots Cross-plots (Predicted vs. Actual) and Error Residuals.

## 3. Fundamental Knowledge & Equations

### A. Standing Correlation
Developed for California black oils.
$$
P_b = 18.2 \left[ \left( \frac{R_s}{\gamma_g} \right)^{0.83} \cdot 10^{(0.00091T - 0.0125 \text{API})} - 1.4 \right]
$$
<div align="center">
  <img src="https://latex.codecogs.com/svg.latex?\large&space;P_b=18.2\left[\left(\frac{R_s}{\gamma_g}\right)^{0.83}\cdot10^{(0.00091T-0.0125\text{API})}-1.4\right]" title="Standing's Correlation" />
</div>

### B. Vasquez-Beggs Correlation
Uses different coefficients based on oil gravity (API > 30 or API <= 30).
$$
P_b = \left( \frac{C_1 \cdot R_s}{\gamma_{gs} \cdot e^{(C_3 \cdot \text{API} / (T+460))}} \right)^{\frac{1}{C_2}}
$$
*Where $C_1, C_2, C_3$ are constants derived from regression.*

### C. Glaso Correlation
Developed for North Sea volatile oils. It uses a "paraffinicity" factor.
$$
P_b = 10^{(1.7669 + 1.7447 \log(X) - 0.30218 \log(X)^2)}
$$
Where $X$ is a function of API, temperature, and gas gravity.

## 4. Requirements
* Python 3.8+
* NumPy
* Pandas
* Matplotlib
* SciPy
