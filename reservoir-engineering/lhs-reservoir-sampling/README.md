# Latin Hypercube Sampling (LHS) Generator for Reservoir Simulation

## Problem Statement
Reservoir simulation models typically involve high-dimensional uncertainty. Parameters such as **Porosity**, **Permeability**, **Water Saturation**, and **Gross Rock Volume** are rarely known with certainty; instead, they are represented by probability distributions.

Running a reservoir simulation is computationally expensive. Traditional **Monte Carlo Simulation (MCS)** requires thousands of runs to achieve convergence because it samples purely randomly, often clustering in one area and neglecting the tails of the distribution. Engineers need a method to generate a representative "Design of Experiments" (DoE) table that covers the entire uncertainty space efficiently with a minimum number of simulation runs.

## Solution
This project utilizes **Latin Hypercube Sampling (LHS)**. LHS is a stratified sampling technique that ensures the full range of each parameter is sampled.

1.  **Stratification:** It divides the probability distribution of each variable into $N$ intervals of equal probability.
2.  **Sampling:** It selects exactly one sample from each interval.
3.  **Shuffling:** It randomly permutes the samples to remove correlations between variables.

This approach often achieves the same accuracy as Monte Carlo with significantly fewer samples (e.g., 50 LHS runs might be equivalent to 1,000 MCS runs).

## Fundamental Knowledge: The Mathematics
### The Unit Hypercube
LHS initially generates samples in a "Unit Hypercube" ($[0, 1]^d$), where $d$ is the number of parameters.
For a sample size $N$, the range $[0, 1]$ is divided into $N$ bins.

### Inverse Transform Sampling
To convert these unit samples ($u$) into physical values ($x$) (e.g., Permeability in mD), we use the **Inverse Cumulative Distribution Function (CDF)**, also known as the Percent Point Function ($ppf$).

$$x = CDF^{-1}(u)$$

* If $u = 0.5$ (median) and the distribution is Normal($\mu=0.2, \sigma=0.05$), $x$ will be $0.2$.
* If the distribution is LogNormal, the transformation adjusts the spacing to respect the "long tail" of high permeability values.

## Usage
1.  Define your uncertainty variables in `parameters.csv`.
2.  Run `lhs_generator.ipynb`.
3.  The script outputs `design_table.csv` ready for your simulator (e.g., Eclipse, tNavigator, CMG).
