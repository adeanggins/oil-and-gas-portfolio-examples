# Flowing Bottom Hole Pressure (FBHP) Calculation

## Project Overview
This repository showcases a Python-based solution for calculating Flowing Bottom Hole Pressure (FBHP) in vertical oil wells. By implementing a multiphase flow correlation (based on Hagedorn-Brown logic), we can estimate downhole pressure using surface wellhead data.

This use case is critical in the oil and gas industry for surveillance and production optimization where permanent downhole gauges (PDG) are either unavailable or faulty.

## Problem Statement
Accurate knowledge of FBHP is essential for:
1.  **Inflow Performance Relationship (IPR)** analysis.
2.  **Productivity Index (PI)** monitoring.
3.  **Artificial Lift** design and optimization.

However, running wireline surveys to measure pressure is expensive and risky. The objective is to calculate FBHP computationally using surface parameters (Pressure, Temperature, Rates) and well geometry.

## Methodology
The solution utilizes a **Pressure Traverse** algorithm. Unlike simple hydrostatic calculations, calculating FBHP in a flowing well requires accounting for:
* **Multiphase Flow:** The fluid is a mixture of Oil, Gas, and Water.
* **Slip Velocity:** Gas travels faster than liquid (Holdup effect).
* **Friction Losses:** Energy lost due to fluid contact with tubing walls.

The pressure gradient equation solved iteratively is:

$$\frac{dP}{dZ} = \rho_{mix} + \text{Friction}_{loss} + \text{Acceleration}_{loss}$$

## Contents
* `01_Data_Generation.csv`: Script to generate synthetic dataset containing 500 well test records.
* `02_FBHP_Calculation.ipynb`: The core analysis step-by-step.
* `well_test_data.csv`: Synthetic dataset containing 500 well test records.

## Requirements
* Python 3.8+
* NumPy
* Pandas
* Matplotlib
