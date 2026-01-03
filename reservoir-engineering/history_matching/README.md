# History Matching Error Analysis

## Problem Statement
In reservoir simulation, **History Matching** is the process of adjusting model parameters (permeability, porosity, fault transmissibility, etc.) until the simulated production data matches the historical observed data.

A critical step in this workflow is quantifying the "mismatch" or error. Engineers need to identify not just the overall error, but specifically **when** and **where** the model diverges from reality. A global error metric might look acceptable, but hidden local divergences can indicate incorrect physical assumptions in specific time periods (e.g., water breakthrough timing or pressure support mechanisms).

## Solution Overview
This repository provides a Python-based toolset to visualize and quantify the mismatch between Simulated and Observed data.

The solution includes:
1.  **Time-Series Visualization**: Overlaying observed vs. simulated data to spot trends.
2.  **Residual Analysis**: Calculating the difference between simulated and observed values over time.
3.  **Cross-Plots**: Visualizing goodness-of-fit using 1:1 correlation plots.
4.  **Distribution Analysis**: Using histograms to understand the spread of errors.

## Fundamental Knowledge

### 1. Residual Calculation
The residual ($e_t$) at time step $t$ is defined as:

$$e_t = y_{sim, t} - y_{obs, t}$$

Where:
* $y_{sim, t}$ = Simulated value at time $t$
* $y_{obs, t}$ = Observed value at time $t$

### 2. Percentage Error
To normalize the error across different magnitudes of pressure or rate:

$$\%Error_t = \frac{y_{sim, t} - y_{obs, t}}{y_{obs, t}} \times 100$$

### 3. Root Mean Square Error (RMSE)
A standard metric to quantify the overall quality of the history match:

$$RMSE = \sqrt{\frac{1}{n} \sum_{t=1}^{n} (y_{sim, t} - y_{obs, t})^2}$$
