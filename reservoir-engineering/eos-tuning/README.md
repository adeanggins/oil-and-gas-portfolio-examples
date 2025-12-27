# Hybrid EOS Tuning & Viscosity Prediction
**A Physics-Informed Machine Learning Workflow**

## 1. Problem Statement
In Reservoir Engineering, an accurate Equation of State (EOS) is critical for simulating fluid behavior. However, default EOS parameters (like Critical Pressure $P_c$, Critical Temperature $T_c$, and Acentric Factor $\omega$) rarely match experimental PVT data perfectly due to fluid impurities and heavy components ($C_{7+}$).

Furthermore, while EOS models are good at predicting density, they often struggle with transport properties like **Viscosity**. Analytical viscosity correlations (e.g., Lohrenz-Bray-Clark) require heavy calibration.

## 2. Solution Overview
This repository demonstrates a two-stage hybrid workflow:
1.  **EOS Parameter Tuning (Genetic Algorithms):** We use the `DEAP` library to automate the regression of EOS parameters ($P_c, T_c, \omega$) to minimize the error between calculated density and experimental density.
2.  **Viscosity Prediction (Random Forest):** Instead of relying on analytical viscosity equations, we use the tuned EOS outputs (Density) combined with $P$ and $T$ to train a Random Forest Regressor for highly accurate viscosity predictions.

## 3. Fundamental Knowledge

### The Peng-Robinson EOS
The pressure $P$ of a fluid is calculated as:

$$P = \frac{RT}{V_m - b} - \frac{a \alpha}{V_m^2 + 2bV_m - b^2}$$

Where:
* $P$ = Pressure
* $T$ = Temperature
* $R$ = Gas Constant
* $V_m$ = Molar Volume
* $a, b$ = EOS attraction and repulsion parameters, which function on $P_c, T_c, \omega$.

### Optimization Objective
We use a Genetic Algorithm to find the vector $x = [P_c, T_c, \omega]$ that minimizes the Root Mean Squared Error (RMSE):

$$\text{Minimize } J(x) = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (\rho_{exp, i} - \rho_{EOS, i}(x))^2}$$

## 4. Libraries Used
* **DEAP:** Evolutionary computation framework for the Genetic Algorithm.
* **Scipy:** Optimization and root-finding (for solving Cubic EOS).
* **Scikit-Learn:** Random Forest Regressor.
* **Pandas/Numpy:** Data manipulation.
