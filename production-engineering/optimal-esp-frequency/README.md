# ESP Optimal Frequency Solver

## 📌 Project Overview
This repository showcases a mathematical optimization use case for Electrical Submersible Pumps (ESPs) in the Oil & Gas industry. The goal is to determine the **Optimal Operating Frequency (Hz)** that maximizes oil production rates without violating the critical **Motor Temperature** limit.

We utilize **Numerical Optimization** techniques (specifically Sequential Least Squares Programming - SLSQP) provided by the `scipy.optimize` library to solve this constrained non-linear problem.

## 🧠 Fundamental Knowledge

### 1. The Affinity Laws
ESP performance changes with variable speed drive (VSD) frequency settings. According to the Affinity Laws:
* **Flow Rate ($Q$):** Directly proportional to frequency ($Q \propto f$).
    $$\frac{Q_2}{Q_1} = \frac{f_2}{f_1}$$
* **Head ($H$):** Proportional to the square of frequency ($H \propto f^2$).
* **Power ($P$):** Proportional to the cube of frequency ($P \propto f^3$).

### 2. The Thermal Constraint
As frequency increases, the motor spins faster, drawing more current and generating more heat. The relationship between Frequency and Motor Temperature ($T_m$) is often non-linear and can be approximated (for this exercise) as a quadratic function:
$$T_m \approx a \cdot f^2 + b \cdot f + c$$

### 3. The Optimization Problem
* **Objective Function:** Maximize Flow Rate $Q(f)$.
    * *Note: Since solvers typically minimize functions, we minimize the negative flow: $-Q(f)$.*
* **Constraint:** Motor Temperature must be less than the limit ($T_{limit}$).
    * $T_{limit} - T_m(f) \ge 0$

## 🛠️ Usage
1. Install dependencies: `pip install -r requirements.txt`
2. specific dataset is located in `esp_operational_data.csv`.
3. Run the analysis in `Optimal_Frequency_Solver.ipynb`.
