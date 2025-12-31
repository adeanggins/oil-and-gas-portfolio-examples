# Automated Saturation Height Function (SHF) Fitting

## Problem Statement
In Reservoir Engineering, accurately distributing water saturation ($S_w$) relative to height above free water level (HAFWL) is critical for Original Oil in Place (OOIP) estimation. Core data provides discrete measurements of Capillary Pressure ($P_c$), Porosity ($\phi$), and Permeability ($k$). However, propagating these discrete points across the entire reservoir model requires a continuous mathematical relationship.

Manual fitting of Saturation Height Functions (like the Leverett J-Function) across varying rock types is time-consuming and prone to human bias.

## Solution
This repository demonstrates an automated approach to fitting the **Leverett J-Function** using Python. By utilizing `scipy.optimize`, we automate the parameter extraction for the power-law relationship between the J-index and Water Saturation.

## Fundamental Theory: Leverett J-Function
The Leverett J-Function is a dimensionless technique used to normalize capillary pressure curves based on rock quality (permeability and porosity). It allows curves from different samples to be grouped into a single universal curve for a specific rock type.

The J-Function is defined as:

$$J(S_w) = 0.2166 \cdot \frac{P_c}{\sigma \cos \theta} \cdot \sqrt{\frac{k}{\phi}}$$

Where:
* $P_c$: Capillary Pressure (psi)
* $\sigma$: Interfacial Tension (dynes/cm)
* $\theta$: Contact Angle (degrees)
* $k$: Permeability (md)
* $\phi$: Porosity (fraction)
* $0.2166$: Unit conversion constant (for Field units)

Once $J$ is calculated, we fit a power-law relationship to the scatter data:
$$J = a \cdot (S_w)^{-b}$$

## Contents
* `01_Data_Generation.ipynb`: Script to generate synthetic dataset containing 20,000+ core measurement points including Porosity, Permeability, and Pc-Sw data.
* `02_Shf_Fitting.ipynb`: The main notebook containing the workflow, mathematical definitions, and visualization.
* `capillary_pressure_data.csv`: A synthetic dataset containing 20,000+ core measurement points including Porosity, Permeability, and Pc-Sw data.

## Requirements
* Python 3.8+
* Pandas
* Numpy
* Scipy
* Matplotlib
