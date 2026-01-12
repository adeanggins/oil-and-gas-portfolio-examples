# Pump Efficiency Degradation Analysis (ESP)

## 📌 Problem Statement
Electric Submersible Pumps (ESPs) are critical assets in oil and gas production. Over time, harsh downhole conditions (sand production, scale, gas locking) cause mechanical wear and stage erosion. This degradation is often invisible until a catastrophic failure occurs.

Operators need a way to **quantify mechanical health** daily without intervening in the well. The standard method is comparing the *actual* operating point against the *theoretical* manufacturer's performance curve.

## 💡 Solution Overview
This repository implements a physics-based analytics solution that:
1.  **Digitizes the Manufacturer's Curve:** Uses polynomial regression to model the Head-Capacity (H-Q) relationship.
2.  **Calculates Theoretical Head:** Computes what the pump *should* produce at the current flow rate and frequency.
3.  **Computates Degradation Index:** Compares actual Total Dynamic Head (TDH) vs. Theoretical Head to flag efficiency loss.

## 🔧 Key Concepts
* **Affinity Laws:** Used to normalize variable frequency operation to the 60Hz (or 50Hz) base curve.
* **Total Dynamic Head (TDH):** The actual lifting work done by the pump, calculated from discharge and intake pressures.
* **Degradation Threshold:** A set percentage (e.g., <90% efficiency) that triggers a maintenance alert.

## 📂 Repository Structure
* `pump_operations_data.csv`: Contains synthetic production data.
* `01_Data_Generator.ipynb`: Script to generate synthetic production data.
* `02_Efficiency_Analysis.ipynb`: Jupyter notebook with step-by-step calculation and visualization.

## 🚀 Getting Started
1.  Install requirements: `pip install -r requirements.txt`
2.  Run the notebook: `jupyter notebook 02_Efficiency_Analysis.ipynb`
