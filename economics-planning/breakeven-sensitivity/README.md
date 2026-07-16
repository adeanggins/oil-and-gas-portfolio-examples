# Break-Even Price Analysis: Tornado & Two-Way Sensitivity

## 1. Problem Statement
"What oil price does this well need?" is the first question every development decision
faces. A single break-even number hides its own fragility: break-even moves with
capex, EUR, decline rate, opex and taxes — and management needs to see which lever
dominates before believing the number.

**Operational Impact:**
* **Portfolio ranking:** Wells are ranked and funded on break-even economics.
* **Negotiation focus:** If capex drives break-even, push the AFE; if EUR does, drill
  appraisal.

## 2. Solution Overview
A transparent single-well cash flow engine (hyperbolic decline, royalty/tax, opex)
feeds three classic decision-analysis products: the **break-even solve** (Brent's
method), the **tornado diagram** (one-at-a-time swings), and **two-way sensitivity
heatmaps** (price × EUR, capex × decline) with the break-even frontier overlaid.

## 3. Fundamental Physics & Features
* **Hyperbolic decline:** q(t) = qi/(1+b·Di·t)^(1/b) — production physics of the cash flow.
* **Break-even:** the price where NPV10 = 0, found by root-finding on the full model.
* **Economic limit:** wells die when revenue < opex, endogenous to price.

**Algorithm:** Cash-flow modeling + Brent root-finding + sensitivity analysis.
**Libraries:** Numpy, Scipy, Matplotlib.

## 4. Repository Structure
* `breakeven_inputs.csv`: Base case and swing ranges.
* `Breakeven_Sensitivity.ipynb`: Engine, tornado, two-way heatmaps.
* `requirements.txt`: List of dependencies.
