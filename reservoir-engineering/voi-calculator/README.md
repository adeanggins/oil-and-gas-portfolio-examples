# Value of Information (VOI) Calculator: Oil & Gas Decision Tree

## Problem Statement
In petroleum exploration and production, decision-makers constantly face high-stakes choices under uncertainty. A common scenario involves deciding whether to drill a prospect immediately based on available data or to spend capital on acquiring new information (e.g., cutting a core, running an advanced wireline log, or shooting seismic) to reduce that uncertainty.

The critical question is: **Is the new information worth the cost?**

## Solution
This repository implements a **Value of Information (VOI)** calculator using **Bayesian Inference** and **Decision Tree Analysis**.

It utilizes `NetworkX` to construct a directed graph representing the decision chronology, calculating the Expected Monetary Value (EMV) at every decision and chance node.

## Methodology

### 1. Bayesian Update
We update the prior probability of success (presence of hydrocarbons) based on the reliability of the new information (The Core/Log).

$$P(Oil | Positive) = \frac{P(Positive | Oil) \cdot P(Oil)}{P(Positive)}$$

Where:
- $P(Positive | Oil)$ is the **Sensitivity** (True Positive Rate).
- $P(Positive | Dry)$ is $(1 - Specificity)$ (False Positive Rate).

### 2. Expected Monetary Value (EMV)
The value of a specific branch is calculated as:

$$EMV = \sum (Probability_i \times Payoff_i) - Cost$$

### 3. Value of Information (VOI)
The economic value of the core/log is the difference between the EMV with the information and the EMV without it, minus the cost of the information itself.

$$VOI = EMV_{with\_info} - EMV_{without\_info}$$

## Usage
1. Install requirements: `pip install -r requirements.txt`
2. Run the analysis: Open `voi_analysis.ipynb`
