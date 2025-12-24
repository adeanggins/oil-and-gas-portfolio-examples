# Hall Plot Diagnostic for Water Injection Surveillance

## 📌 Problem Statement
In waterflooding operations, maintaining injectivity is crucial. Decline in injectivity can result from **pore plugging** (poor water quality, fines migration), while a sudden increase might indicate **formation fracturing** or cap-rock failure. Standard rate-time plots often mask these issues due to fluctuating injection pressures.

## 💡 Solution
The **Hall Plot** (Hall, 1963) is an integral-based method that linearizes the relationship between injection pressure and cumulative injection volume. It is the industry standard for distinguishing between skin damage (plugging) and improved injectivity (stimulation/fracturing).

## 📐 Fundamental Theory

Based on Darcy's Law for steady-state radial flow, Hall derived the following relationship:

$$\int (p_{tf} - p_e) dt = \frac{141.2 \mu B_w \ln(r_e/r_w)}{k h} W_i + C$$

In practice, we simplify this by plotting the **Cumulative Pressure-Time** term against **Cumulative Water Injection**:

* **Y-Axis:** $\sum (p_{tf} \cdot \Delta t)$  (psi-days)
* **X-Axis:** $W_i$ (Cumulative Water Injection, bbl)

*Where:*
* $p_{tf}$: Tubing flowing pressure (injection pressure)
* $p_e$: Reservoir pressure (often neglected if constant relative to $p_{tf}$)
* $\Delta t$: Time step duration
* $W_i$: Cumulative injection

### Interpretation of Slope ($m_H$):

The slope of the Hall Plot is inversely proportional to the injectivity index ($II$).

1.  **Normal Operation:** A **straight line** indicates constant injectivity.
2.  **Plugging (Skin Damage):** The curve deflects **upward** (concave up). The slope increases because more pressure-time is required to inject the same volume of water.
    * *Causes:* Water quality issues, bacterial growth, scale, fines migration.
3.  **Fracturing / Channeling:** The curve deflects **downward** (concave down). The slope decreases because water is entering the formation easier than expected.
    * *Causes:* Injection above parting pressure, acid stimulation, thief zones.

## 🏗️ Architecture
This project is structured as a modular Python package to ensure scalability and reusability.

* `reservoir_diagnostics.py`: Contains the `ReservoirDiagnostics` class. This encapsulates:
    * Data ingestion methods (Production & Injection).
    * **Savitzky-Golay** signal processing logic (hidden from the end-user).
    * Matplotlib visualization engines.
* `run_analysis.ipynb`: The front-end interface for Engineers to run the analysis without touching the core logic.

### Why OOP?
Using Object-Oriented Programming (OOP) allows us to instantiate multiple "Well" objects (e.g., `well_A`, `well_B`) and compare their performance programmatically, rather than rewriting script logic for every dataset.

## 🚀 Usage in Python
The accompanying notebook calculates the cumulative pressure-time integral using the Trapezoidal rule (or simple summation for daily data) and plots it against cumulative injection.
