# ESP Gas Locking Detection using Random Forest Classification

## 1. Problem Statement
Gas locking is a critical failure mode in Electric Submersible Pumps (ESPs) operating in high Gas-Liquid Ratio (GLR) wells. It occurs when free gas accumulates in the pump impeller, breaking the hydraulic seal and preventing fluid production.

**Operational Impact:**
* **Production Loss:** Immediate cessation of fluid flow.
* **Equipment Damage:** Motor overheating due to lack of cooling fluid (underload) and severe mechanical stress from cycling.

## 2. Solution Overview
This repository demonstrates a Machine Learning approach to detect gas locking signatures using **Random Forest Classification**. Instead of relying solely on simple threshold alarms (e.g., Low Amps), this model analyzes the relationship between motor current and intake pressure trends to distinguish between normal operation, gas interference, and full gas lock.

## 3. Fundamental Physics & Features
The model relies on the following physical signatures of gas locking:
* **Motor Current (Amps):** Drops significantly and becomes unstable as the pump compresses gas instead of liquid (less work required).
* **Intake Pressure (PIP):** Often rises or fluctuates as the gas column builds up and liquid is not effectively removed.
* **Vibration:** (Optional but helpful) typically spikes as gas slugs pass through the pump.

**Algorithm:** Random Forest Classifier (Supervised Learning).
**Libraries:** Scikit-Learn, Pandas, Matplotlib.

## 4. Repository Structure
* `esp_gas_locking_data.csv`: Contains the synthetic ESP sensor data.
* `Gas_Locking_Detection.ipynb`: Contains the analysis and model training steps.
* `requirements.txt`: List of dependencies.
