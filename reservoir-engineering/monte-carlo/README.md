# Probabilistic Reserves Estimation using Monte Carlo Simulation

## Problem Statement
In the oil and gas industry, calculating Hydrocarbon In-Place or Recoverable Reserves is never deterministic due to the high uncertainty of subsurface parameters. Traditional "deterministic" methods (using single average values) often fail to capture the range of possible outcomes, leading to poor investment decisions.

This project demonstrates a **Probabilistic Approach** using **Monte Carlo Simulation**. By treating input parameters (Area, Thickness, Porosity, Saturation) as statistical distributions rather than single values, we run 10,000 iterations to generate a probability distribution of the reserves. This allows us to quantify risk via P10, P50, and P90 estimates.

## The Formula
For this exercise, we calculate the bulk Hydrocarbon Volume using the simplified volumetric equation:

$$V = A \times h \times \phi \times S_o$$

Where:
* **$V$**: Hydrocarbon Volume (e.g., Reservoir Barrels or HCPV)
* **$A$**: Area (Drainage area)
* **$h$**: Net Pay Thickness
* **$\phi$**: Effective Porosity
* **$S_o$**: Oil Saturation

## Methodology
1.  **Data Ingestion**: Load historical/offset well data to understand parameter ranges.
2.  **Distribution Modeling**: Assign statistical distributions to each parameter:
    * *Area*: Triangular Distribution (Min, Mode, Max) - representing geological uncertainty.
    * *Thickness*: Normal Distribution - based on well logs.
    * *Porosity*: Normal Distribution (clipped at 0 and 1).
    * *Saturation*: Uniform Distribution - representing a range of uncertainty.
3.  **Monte Carlo Simulation**: Perform 10,000 vectorized iterations using `NumPy`.
4.  **Quantification**: Extract P90 (Proven), P50 (Proven + Probable), and P10 (Proven + Probable + Possible) values.

## Key Technologies
* **Python**: Core programming language.
* **Numpy**: For high-performance vectorized random number generation and calculation.
* **Matplotlib/Seaborn**: For visualizing the probability density functions (PDF) and cumulative distribution functions (CDF).
