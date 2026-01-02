# Time-Series Reservoir Surrogate Modeling with LSTM (PyTorch)

## 1. Problem Statement
In field development planning, predicting the **production profile** (Oil Rate vs. Time) is critical for economic analysis (NPV calculations). Full-physics simulators calculate this step-by-step, which is slow.
We need a model that can instantly generate a 24-month production forecast based on static reservoir properties.

## 2. Solution Overview
This project implements a **Sequence-Generation Surrogate Model** using Deep Learning.
* **Inputs:** Static geological parameters (Porosity, Permeability, Thickness, etc.).
* **Model:** A Long Short-Term Memory (LSTM) Network.
* **Outputs:** Monthly Oil Production Rates for 24 months.

## 3. Fundamental Concepts: Static-to-Dynamic Mapping
Standard LSTMs typically map *Sequence-to-Sequence* (e.g., stock price yesterday -> stock price today).
In this Reservoir Engineering context, we have a **One-to-Many** problem:
* **One** vector of static properties (Geology does not change over time).
* **Many** time steps of production output (Rates change every month).

### Architecture Strategy
To utilize an LSTM, we project the static input features into a latent space and "repeat" them across time steps, allowing the LSTM to learn the temporal decay function (the decline curve) inherent in the physics.

### Physics-Informed Loss Function
Standard Neural Networks blindly minimize the error between prediction and data (MSE). This can lead to unphysical results, such as production rates increasing arbitrarily or exceeding the total volume of oil in place.

To fix this, we implement a custom **Hybrid Loss Function**:
$$L_{total} = L_{MSE} + \lambda_1 L_{Monotonicity} + \lambda_2 L_{Volume}$$

1.  **$L_{MSE}$ (Data Match):** Fits the training data.
2.  **$L_{Monotonicity}$ (Decline Law):** Enforces $q_{t} \ge q_{t+1}$. It penalizes any positive slope in the production profile, ensuring a physical decline curve.
3.  **$L_{Volume}$ (Material Balance):** Ensures the total predicted cumulative production scales consistently with the Reservoir Pore Volume ($Porosity \times Thickness$).

## 4. Repository Structure
* `01_Data_Generator.py`: Script to generate synthetic production profiles.
* `02_Surrogate_LSTM_Pytorch.ipynb`: The notebook containing the LSTM implementation.
* `reservoir_timeseries_data.csv`: The dataset.
* `requirements.txt`: Dependencies.
