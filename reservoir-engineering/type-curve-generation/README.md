# Type Curve Generation & Probability Analysis

## Problem Statement
In field development planning, engineers often need to estimate the production profile of proposed new wells without historical data. Relying on a single "average" well can be misleading due to geological heterogeneity. The objective is to construct a **Type Well Profile** (Type Curve) based on offset analogy wells to predict future performance.

## Solution Overview
This repository demonstrates a data science approach to generating probabilistic Type Curves (P10, P50, P90) from historical production data.

The workflow includes:
1.  **Data Ingestion:** Loading raw monthly production data from 15 analogy wells.
2.  **Normalization:** Aligning all wells to "Time Zero" based on their peak production month to remove start-date bias.
3.  **Statistical Aggregation:** Calculating the P10 (Aggressive), P50 (Typical), and P90 (Conservative) production rates at each timestep.
4.  **Visualization:** Plotting the probabilistic envelopes against individual well performance.

## Fundamental Concepts

### Peak Rate Alignment
To compare wells drilled at different times, we normalize the time axis. $t=0$ is defined as the month where the well reached its maximum flow rate ($q_{peak}$).

### Probabilistic Profiles
Instead of a simple arithmetic mean, we use percentiles to quantify uncertainty:
* **P90 (Conservative):** 90% of the wells produced more than this rate at time $t$.
* **P50 (Median):** The middle value of the dataset at time $t$.
* **P10 (Optimistic):** Only 10% of the wells exceeded this rate at time $t$.

## Getting Started

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the Notebook:**
    Open `TypeCurve_Generation.ipynb` in Jupyter to see the step-by-step analysis.
