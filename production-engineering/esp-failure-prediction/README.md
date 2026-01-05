# ESP Failure Prediction: Remaining Useful Life (RUL) with LSTM

## Overview
This repository demonstrates a Deep Learning approach to Predictive Maintenance in the Oil & Gas industry. Specifically, it targets **Electrical Submersible Pumps (ESP)**, predicting the **Remaining Useful Life (RUL)** based on high-frequency sensor data (Amperage, Vibration, and Motor Temperature).

## Problem Statement
ESP failures often result in:
1.  **Deferred Production:** Wells are shut in while waiting for workover rigs.
2.  **High Costs:** Emergency replacements are more expensive than planned interventions.

By analyzing temporal patterns in sensor data, we can detect subtle degradation signatures (e.g., increasing vibration trends or amperage instability) before a catastrophic failure occurs.

## Solution Architecture
We utilize a **Long Short-Term Memory (LSTM)** neural network. 
* **Why LSTM?** Standard regression models treat data points independently. ESP degradation is a temporal process; the state of the pump at time $t$ depends heavily on $t-1, t-2...$. LSTMs are designed to capture these long-term dependencies.
* **Input:** A sliding window (e.g., past 30 hours) of sensor metrics.
* **Output:** Continuous regression value representing hours left until failure.

## Repository Contents
* `01_Data_Generator.py`: A script to generate synthetic run-to-failure data for the exercise.
* `02_ESP_RUL_LSTM.ipynb`: The main Jupyter Notebook containing data exploration, preprocessing, model building, and evaluation.
* `esp_sensor_data.csv`: Synthetic run-to-failure data for the exercise.
* `requirements.txt`: List of dependencies.

## Results
The model outputs a visualization contrasting the **Actual RUL** (linear degradation) vs. **Predicted RUL**. Lower RMSE scores indicate higher prediction accuracy.
