# Injector-Producer Connectivity Analysis (CRM)

## 1. Problem Statement
In mature waterfloods, understanding the inter-well connectivity between injectors and producers is critical for optimizing injection rates and maximizing oil recovery. Traditional methods like streamline simulation or tracer tests can be computationally expensive or logistically difficult.

**The Goal:** Quantify the connectivity weights ($f_{ij}$) and time constants ($\tau_j$) for injector-producer pairs using only historical **rate data** (Injection and Production rates).

## 2. Solution: Capacitance Resistance Model (CRM)
The Capacitance Resistance Model (CRM) is a physics-based, data-driven technique that uses signal processing to model the reservoir as a system of tanks (producers) connected to sources (injectors). It accounts for the compressibility of the fluid/rock (capacitance) and the transmissibility (resistance).

We utilize the **CRMP (Producer-based)** representation, which treats each producer as a distinct control volume. The fundamental equation governing the production rate $q_j(t)$ of producer $j$ at time step $t$ is derived from material balance:

$$
q_j(t) = q_j(t-1) e^{-\frac{\Delta t}{\tau_j}} + \sum_{i=1}^{N_{inj}} f_{ij} (1 - e^{-\frac{\Delta t}{\tau_j}}) I_i(t)
$$

Where:
* $q_j(t)$: Liquid production rate of producer $j$ at time $t$.
* $I_i(t)$: Injection rate of injector $i$ at time $t$.
* $\tau_j$: Time constant for producer $j$ (related to compressibility and pore volume).
* $f_{ij}$: Connectivity (gain) between injector $i$ and producer $j$.
* $\Delta t$: Time step interval.

## 3. Methodology
This repository contains a Jupyter Notebook that demonstrates:
1.  **Data Preprocessing:** Aligning injection and production time series.
2.  **Model Definition:** Implementing the CRMP physics equation.
3.  **Optimization:** Using `scipy.optimize.minimize` (L-BFGS-B or SLSQP) to find the optimal parameters ($\tau_j, f_{ij}$) that minimize the squared error between observed and predicted production.
4.  **Constraints:**
    * $0 \le f_{ij} \le 1$
    * $\tau_j > 0$
    * $\sum_j f_{ij} \le 1$ (Material balance constraint, optional but recommended).

## 4. Repository Contents
* `01_Data_Generator.py`: Script used to generate the synthetic dataset based on known physics.
* `02_CRM_Analysis.ipynb`: The main workflow containing code and detailed markdown explanations.
* `03_Advance_Data_Generator.py`: Script used to generate the synthetic dataset based on known physics for the advance exercise.
* `04_Advance_CRM_Analysis.ipynb`: The main workflow containing code and detailed markdown explanations for the advance exercise.
* `production_injection_data.csv`: Synthetic dataset with 10 injectors and 40 producers.
* `production_injection_data_advance.csv`: Synthetic dataset with 10 injectors and 40 producers for the advance exercise.
* `well_locations.csv`: Synthetic dataset with 10 injectors and 40 producers locations for the advance exercise.
