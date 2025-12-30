# Permeability-Porosity Transforms: Non-Linear Regression

## Problem Statement
In reservoir characterization, **Permeability ($k$)** is a dynamic property that is difficult and expensive to measure directly (requiring core analysis or well testing). Conversely, **Porosity ($\phi$)** is a static property readily derived from wireline logs (Density, Neutron, Sonic) across the entire wellbore.

The challenge is to establish a robust mathematical relationship to predict permeability from porosity in un-cored intervals. Simple linear regressions often fail because permeability and porosity typically exhibit a non-linear relationship governed by pore throat geometry and tortuosity.

## Objective
Develop a non-linear regression model using **Statsmodels** to predict permeability from core porosity data, moving beyond simple power laws to capture complex lithological behaviors.

## Fundamental Knowledge
The relationship between porosity and permeability is often derived from the **Kozeny-Carman** equation, which relates fluid flow to the properties of the porous medium:

$$k \propto \frac{\phi^3}{(1-\phi)^2} \frac{1}{S_v^2}$$

Where:
* $k$ is permeability.
* $\phi$ is porosity.
* $S_v$ is the specific surface area.

In practice, this theoretical relationship often manifests as a semi-logarithmic relationship. This project explores models of the form:

$$\log(k) = \beta_0 + \beta_1 \phi + \beta_2 \phi^2 + \epsilon$$

This approach allows us to model the exponential nature of permeability growth while correcting for deviations using polynomial expansion.

To further enhance the accuracy of permeability predictions, the following steps are proposed for the next iteration of this project:

### 1. Hydraulic Flow Unit (HFU) Classification (Rock Typing)
A global regression model often averages out distinct geological facies. By applying unsupervised learning, we can separate the reservoir into distinct Rock Types.
* **Method:** Use **K-Means Clustering** or **Gaussian Mixture Models (GMM)** on the Porosity and Permeability data to identify clusters (Flow Units).
* **Benefit:** Instead of one global equation, we can derive specific $k-\phi$ transforms for each cluster (e.g., $k = a_1 e^{b_1 \phi}$ for Cluster 1, $k = a_2 e^{b_2 \phi}$ for Cluster 2). This typically increases the $R^2$ significantly.
* **Metric:** Calculate the **Flow Zone Indicator (FZI)** to validate the physical meaning of the clusters.

### 2. Multivariate Regression
If additional wireline log data (Gamma Ray, Resistivity, Density) is available, we can move from simple regression to multivariate analysis.
* **Action:** Incorporate `Gamma_Ray` and `Depth` as features in the `statsmodels` formula:
    `np.log10(Permeability) ~ Porosity + Gamma_Ray + Depth`

### 3. Cross-Validation
* Implement **K-Fold Cross-Validation** to ensure the model generalizes well to unseen data and isn't just overfitting the specific noise in the training set.

## Repository Contents
* **`01_Data_Generation.ipynb`**: Script to generate Synthetic core data containing 20,000 rows of depth-matched porosity and permeability measurements.
* **`02_Perm_Poro_Regression.ipynb`**: A Jupyter Notebook demonstrating data exploration, transformation, and non-linear regression using `statsmodels` and `sklearn`.
* **`porosity_permeability.csv`**: Synthetic core data containing 20,000 rows of depth-matched porosity and permeability measurements.
