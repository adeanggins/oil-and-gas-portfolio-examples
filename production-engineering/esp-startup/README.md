# ESP Start-up Transient Analysis: Identifying Hard Starts

## 1. Problem Statement
Electrical Submersible Pumps (ESPs) are critical assets in oil production. The "start-up" phase of an ESP is the most stressful period for the motor. Ideally, a start-up should be smooth, with current and frequency ramping up steadily.

However, mechanical binding, debris, or poor power quality can cause **"Hard Starts"**—characterized by current spikes, erratic frequency ramps, or prolonged stabilization times. These hard starts significantly shorten the insulation life of the motor and lead to premature failure.

Detecting these anomalies manually across hundreds of wells is impossible. This project automates the identification of hard starts using unsupervised machine learning.

## 2. Solution Overview
This repository implements a **K-Means Clustering** algorithm to categorize ESP start-up signatures.
* **Input:** High-frequency time-series data (Amps, Frequency, Voltage) during the first 60 seconds of start-up.
* **Feature Engineering:** Extraction of transient features such as *Peak Current*, *Ramp-up Time*, *Overshoot Percentage*, and *Stabilization Variance*.
* **Model:** Scikit-Learn K-Means to group starts into "Normal" and "Hard/Anomalous" clusters.
* **Output:** Classification of every start-up event to flag wells requiring maintenance.

## 3. Fundamental Physics & Math

### Transient Current Overshoot
A key indicator of a hard start is the overshoot percentage ($OS_{\%}$), calculated as:

$$OS_{\%} = \frac{I_{peak} - I_{steady}}{I_{steady}} \times 100$$

Where:
* $I_{peak}$ = Maximum current recorded during start-up.
* $I_{steady}$ = Average current after stabilization.

### Euclidean Distance for Clustering
The K-Means algorithm minimizes the within-cluster sum of squares (inertia). It assigns a start-up event $x$ to a cluster $C_i$ based on the Euclidean distance to the centroid $\mu_i$:

$$d(x, \mu_i) = \sqrt{ \sum_{j=1}^{n} (x_j - \mu_{ij})^2 }$$

Where $j$ represents the features (e.g., peak current, ramp time).

## 4. Repository Structure
* `esp_startup_data.csv`: Contains the synthetic start-up dataset.
* `01_Data_Generator.ipynb`: Script to generate the synthetic start-up dataset.
* `02_ESP_Startup_Transient_Analysis.ipynb`: Jupyter notebook with the step-by-step analysis.
* `requirements.txt`: Python dependencies.
