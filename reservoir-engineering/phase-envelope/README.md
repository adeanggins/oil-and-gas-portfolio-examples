# Phase Envelope Generator & Well Flow Regime Analysis

## 1. Problem Statement
In reservoir management and production optimization, knowing the phase behavior of the reservoir fluid is critical. Engineers must avoid unintentional phase changes (e.g., retrograde condensation in gas pipes or gas breakout in oil pumps) which can damage equipment and reduce flow efficiency.

This project implements a **Phase Envelope Generator** using the **Peng-Robinson Equation of State (EOS)**. It calculates the Bubble Point and Dew Point curves for a multicomponent mixture.

**Use Case:**
We apply this model to a field with 200 active wells. By overlaying the real-time Pressure (P) and Temperature (T) sensor data from these wells onto the generated Phase Envelope, we classify each well's flow regime:
* **Liquid Phase** (Undersaturated Oil)
* **Vapor Phase** (Superheated Gas)
* **Two-Phase** (Gas + Liquid mixture)

## 2. Fundamental Knowledge: Peng-Robinson EOS
The phase envelope is the boundary separating single-phase regions from the two-phase region. We solve for the condition where the fugacity of component $i$ in the liquid phase ($f_i^L$) equals the fugacity in the vapor phase ($f_i^V$).

The Peng-Robinson EOS is defined as:

$$P = \frac{RT}{V_m - b} - \frac{a \alpha}{V_m(V_m + b) + b(V_m - b)}$$

Where:
* $P$ = Pressure
* $T$ = Temperature
* $R$ = Ideal Gas Constant
* $V_m$ = Molar Volume
* $a, b$ = EOS attraction and repulsion parameters (derived from Critical Properties $T_c, P_c$)
* $\alpha$ = Alpha function (dependent on acentric factor $\omega$ and reduced temperature $T_r$)

To find the saturation points (Bubble/Dew lines), we use **Flash Calculations** (Rachford-Rice equation) combined with stability analysis or Newton-Raphson iteration to satisfy equilibrium conditions.

## 3. Fundamental Knowledge: The Rigorous EOS Solver
To plot an accurate Phase Envelope, we cannot rely on simple correlations. We must satisfy the **Iso-Fugacity Condition**:

$$f_i^L = f_i^V$$

Where $f_i$ is the fugacity of component $i$. This requires calculating the **Fugacity Coefficient** ($\phi_i$) using the Peng-Robinson Equation of State:

$$\ln \phi_i = \frac{b_i}{b}(Z-1) - \ln(Z-B) - \frac{A}{2\sqrt{2}B} \left( \frac{2 \sum x_j a_{ji}}{a} - \frac{b_i}{b} \right) \ln \left( \frac{Z + (1+\sqrt{2})B}{Z + (1-\sqrt{2})B} \right)$$

**The Algorithm (Bubble Point Example):**
1. Fix Temperature ($T$).
2. Initialize Pressure ($P$) and K-values ($K_i$) using Wilson's correlation.
3. **Iterative Loop:**
    * Calculate mole fractions ($y_i = z_i K_i$).
    * Solve Cubic EOS for Liquid $Z^L$ and Vapor $Z^V$.
    * Calculate Fugacity Coefficients $\phi_i^L$ and $\phi_i^V$.
    * Update K-values: $K_i^{new} = K_i^{old} (\phi_i^L / \phi_i^V)$.
    * Check Convergence: Is $\sum y_i \approx 1$?
    * Update Pressure: $P_{new} = P_{old} \times \sum y_i$.

## 4. Repository Structure
* `01_Phase_Envelope_Generator.ipynb`: Jupyter Notebook containing the EOS engine, solving algorithms, and visualization.
* `well_sensor_data.csv`: A dataset containing P-T telemetry from 200 wells.

## 5. Requirements
* Python 3.x
* `numpy`
* `pandas`
* `matplotlib`
* `scipy`
