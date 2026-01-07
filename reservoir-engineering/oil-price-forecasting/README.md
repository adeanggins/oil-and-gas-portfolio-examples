# Oil Price Time-Series Forecasting: ARIMA vs. LSTM

## 1. Problem Statement
Crude oil prices are a primary driver of global economic activity and a critical input for revenue estimation in the energy sector. However, oil prices are highly non-linear and volatile, influenced by geopolitical events, supply-demand dynamics, and market sentiment. Accurately forecasting short-term prices is essential for:
* **Revenue Estimation:** Budgeting for exploration and production companies.
* **Risk Management:** Hedging strategies for consumers and producers.
* **Inventory Optimization:** Timing purchases and sales.

## 2. Solution Overview
This repository explores two distinct approaches to forecasting Daily West Texas Intermediate (WTI) Crude Oil Prices:

1.  **ARIMA (AutoRegressive Integrated Moving Average):** A classical statistical method that captures linear relationships in time-series data.
2.  **LSTM (Long Short-Term Memory):** A Recurrent Neural Network (RNN) capable of learning long-term dependencies and non-linear patterns.

## 3. Fundamental Concepts

### A. ARIMA Model
ARIMA is defined by three parameters $(p, d, q)$:
* **AR ($p$):** Autoregression. The dependent relationship between an observation and some number of lagged observations.
    $$Y_t = c + \phi_1 Y_{t-1} + \dots + \phi_p Y_{t-p} + \epsilon_t$$
* **I ($d$):** Integrated. The use of differencing (subtracting an observation from an observation at the previous time step) to make the time series stationary.
* **MA ($q$):** Moving Average. The dependency between an observation and a residual error from a moving average model applied to lagged observations.

### B. LSTM (Deep Learning)
LSTM is a special kind of RNN capable of learning long-term dependencies. Unlike standard feedforward networks, LSTMs have feedback connections. They process data sequences via a cell state and three gates:
1.  **Forget Gate:** Decides what information to discard from the cell state.
2.  **Input Gate:** Decides which new values to update in the cell state.
3.  **Output Gate:** Decides what to output based on the cell state and input.

## 4. Repository Structure
* `oil_price_data.csv`: Historical daily oil price data (Sample).
* `Forecasting.ipynb`: Jupyter Notebook containing EDA, Preprocessing, ARIMA, and LSTM implementation.
* `requirements.txt`: List of dependencies.

## 5. Results & Conclusion
* **ARIMA** performs well on data with clear trends and seasonality but struggles with rapid, non-linear shocks.
* **LSTM** generally outperforms ARIMA in capturing complex volatility but requires more data and computational power.
