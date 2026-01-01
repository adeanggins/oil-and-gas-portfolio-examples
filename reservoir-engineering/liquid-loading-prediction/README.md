# Real-Time Liquid Loading Prediction (Turner's Method)

## Problem Statement
In mature gas wells, liquids (water or condensate) naturally drop out of the gas stream. If the gas velocity is high enough, it carries these liquids to the surface. However, as reservoir pressure depletes, gas velocity decreases. 

When the gas velocity drops below a **Critical Velocity**, liquids begin to accumulate in the tubing. This phenomenon, known as **Liquid Loading**, creates backpressure against the formation, drastically reducing production and potentially killing the well.

## Solution
This repository demonstrates a Python-based solution to flag wells at risk of liquid loading in real-time. We use the industry-standard **Turner (1969) Critical Velocity Model** to calculate the minimum gas velocity required to lift liquids.

By comparing the **Actual Gas Velocity** against the calculated **Critical Velocity**, we generate a binary flag:
- `Loading Risk: HIGH` (Actual Velocity < Critical Velocity)
- `Loading Risk: LOW` (Actual Velocity > Critical Velocity)

## Fundamental Equations
The core calculation relies on the Turner Equation for critical velocity ($v_c$):

$$v_c = 1.593 \frac{\sigma^{0.25} (\rho_L - \rho_g)^{0.25}}{\rho_g^{0.5}}$$

Where:
- $v_c$: Critical gas velocity (ft/sec)
- $\sigma$: Interfacial tension (dynes/cm) - *Assumed 60 for water, 20 for condensate*
- $\rho_L$: Liquid density (lb/ft³)
- $\rho_g$: Gas density (lb/ft³)

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the Jupyter Notebook: `01_Liquid_Loading_Analysis.ipynb`
