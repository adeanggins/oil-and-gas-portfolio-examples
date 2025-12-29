# Missing Log Prediction (Synthetic Logs) using XGBoost

## 1. Problem Statement
In reservoir characterization, a complete suite of well logs is essential for accurate estimation of porosity, permeability, and water saturation. However, logs such as Sonic (DT) or Density (RHOB) are frequently missing due to:
* **Tool Failure:** Malfunctions during wireline logging operations.
* **Borehole Conditions:** Washouts or rugose holes affecting pad-contact tools (like Density).
* **Cost Limitations:** Legacy wells often have limited logging suites (e.g., only Gamma Ray and Resistivity).

Re-logging these wells is prohibitively expensive. Therefore, generating **synthetic logs** using Machine Learning based on available logs is a high-value cost-saving solution.

## 2. Methodology & Physics
We utilize **Gradient Boosting (XGBoost)** to map the non-linear relationship between available inputs and the missing target.

### The Petrophysical Link
The fundamental hypothesis relies on the physical correlation between rock properties:
* **Gamma Ray (GR):** Indicates lithology (Shale vs. Sand). Shales typically have higher GR and lower velocity (higher DT) than sands.
* **Resistivity (ILD/RT):** Responds to fluid content and pore structure.
* **Depth:** Accounts for the compaction trend (velocity increases/DT decreases as we go deeper).

**Model Function:**
$$DT_{pred} = f(GR, ILD, Depth)$$

## 3. Contents
1.  `01_Data_Generator.ipynb`: The notebook containing the script to generate synthetic data.
2.  `02_Missing_Log_Prediction.ipynb`: The main notebook containing the logic, visualization, and step-by-step explanation.
3.  `well_logs.csv`: Synthetic dataset that contains 25,000 rows.
4.  `README.md`: Project documentation.

## 4. Requirements
* Python 3.8+
* Pandas
* XGBoost
* Scikit-Learn
* Matplotlib/Seaborn

## 5. Usage
Clone the repository and run the Jupyter Notebook to see the step-by-step training and prediction process.
