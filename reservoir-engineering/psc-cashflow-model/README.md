# Cash Flow Waterfall Model: PSC Economic Limit Calculator

## 📌 Problem Statement
In the Oil & Gas industry, determining the commercial viability of a field requires rigorous economic modeling. Under a **Production Sharing Contract (PSC)**, the flow of revenue is complex: Gross Revenue must cover Operating Expenses (OPEX) and Capital Expenses (CAPEX) through a "Cost Recovery" mechanism before remaining profits are split between the Government and the Contractor.

The challenge is to:
1.  Model the full fiscal regime (Revenue -> Cost Recovery -> Profit Split -> Tax).
2.  Calculate the **Net Cash Flow (NCF)** for the Contractor.
3.  Identify the **Economic Limit**: The exact year when the asset starts losing money (NCF < 0), signaling abandonment or need for intervention.

## 🚀 Solution
This repository provides a Python-based Economic Calculator using `Pandas`. It ingests production and cost profiles and outputs a detailed cash flow statement and a "Waterfall" visualization of value distribution.

### Fundamental Concepts Implemented
* **Gross Revenue:** Total income from Oil & Gas sales.
* **Cost Recovery:** The portion of revenue the contractor claims to reimburse OPEX and CAPEX.
* **Profit Oil/Gas:** Revenue remaining after Cost Recovery.
* **Entitlement:** The specific split of Profit Oil (e.g., 85% Gov / 15% Contractor).
* **Contractor Tax:** Corporate income tax levied on the Contractor's profit share.
* **Economic Limit:** The timestamp where `Contractor Net Cash Flow <= 0`.

## 🛠 Usage
1.  Install requirements: `pip install -r requirements.txt`
2.  Open the notebook: `jupyter notebook PSC_Economic_Model.ipynb`
3.  Adjust parameters in the "Fiscal Terms" section of the notebook to simulate different regimes.
