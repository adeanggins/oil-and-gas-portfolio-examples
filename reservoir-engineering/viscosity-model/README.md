# Crude Oil Viscosity Prediction: Random Forest Regressor

## 1. Problem Statement
Viscosity is a fundamental fluid property that dictates how oil flows through porous media, pipelines, and surface facilities.
* **The Challenge:** Measuring viscosity in the lab (PVT analysis) is expensive, time-consuming, and requires bottom-hole samples that aren't always available.
* **The Opportunity:** Basic field data like **Temperature**, **Pressure**, and **API Gravity** are abundant.
* **The Goal:** Build a Machine Learning model to accurately predict crude oil viscosity ($\mu$) based on these readily available parameters, replacing the need for expensive sampling in brownfields.

## 2. Solution Overview
This repository utilizes a **Random Forest Regressor** to model the non-linear relationships between field variables and oil viscosity.

**Workflow:**
1.  **Data Ingestion:** Load historical field data (Temperature, Pressure, API).
2.  **Exploratory Data Analysis (EDA):** Visualize correlations (e.g., Temperature vs. Viscosity).
3.  **Model Training:** Train a Random Forest model using `scikit-learn`.
4.  **Evaluation:** Assess performance using $R^2$ Score and Mean Absolute Error (MAE).
5.  **Feature Importance:** Quantify which physical parameter drives viscosity changes the most.

## 3. Fundamental Knowledge
While Machine Learning treats this as a regression problem, the model must respect underlying physical principles:

1.  **Temperature ($T$):** Viscosity decreases exponentially as temperature increases (Arrhenius relationship).
    * *Model Expectation:* Strong negative correlation.
2.  **API Gravity:** Lighter oils (High API) have lower viscosity. Heavier oils (Low API) have higher viscosity.
    * *Model Expectation:* Strong negative correlation.
3.  **Pressure ($P$):** Below the bubble point, pressure increases gas solubility (reducing viscosity). Above the bubble point, compressing liquid slightly increases viscosity.
    * *Model Expectation:* Non-linear, weaker influence compared to $T$ and API.

## 4. Requirements
* Python 3.8+
* Scikit-Learn
* Pandas
* NumPy
* Matplotlib/Seaborn
