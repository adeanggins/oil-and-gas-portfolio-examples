# Electrofacies Classification using Unsupervised Learning

## 1. Problem Statement
In reservoir characterization, identifying lithology (facies) from well logs is a critical step for determining reservoir quality. Traditionally, this is done manually by petrophysicists, which is:
* **Time-consuming** when dealing with hundreds of wells.
* **Subjective**, as different interpreters may define facies boundaries differently.

## 2. Solution Overview
This project automates the identification of electrofacies using **Unsupervised Machine Learning**. By applying **K-Means Clustering**, we can group multi-dimensional well log measurements into distinct clusters that statistically represent different lithologies (e.g., Sandstone, Shale, Limestone) without needing pre-labeled training data.

## 3. Fundamental Knowledge: K-Means Clustering
The core algorithm used here is **K-Means**. It partitions $n$ observations into $k$ clusters in which each observation belongs to the cluster with the nearest mean (centroid).

The algorithm aims to minimize the **Within-Cluster Sum of Squares (WCSS)**, also known as Inertia. Mathematically, the objective function $J$ is:

$$
J = \sum_{i=1}^{k} \sum_{x \in S_i} || x - \mu_i ||^2
$$

Where:
* $k$ is the number of clusters (facies).
* $S_i$ is the set of points in the $i$-th cluster.
* $\mu_i$ is the centroid of the $i$-th cluster.
* $|| x - \mu_i ||^2$ is the squared Euclidean distance between a data point $x$ and the centroid $\mu_i$.

## 4. Dataset
The dataset consists of synthetic well log data from 15 wells representing typical formation responses.
* **GR**: Gamma Ray (API) - Measures natural radioactivity (Shale indicator).
* **RHOB**: Bulk Density (g/cc) - Measures formation density.
* **NPHI**: Neutron Porosity (v/v) - Measures hydrogen index.
* **RT**: Deep Resistivity (ohm.m) - Measures fluid saturation/resistivity.

## 5. Technology Stack
* **Python**: Core programming language.
* **Scikit-Learn**: For the K-Means algorithm and data scaling.
* **Seaborn/Matplotlib**: For statistical visualization and log plotting.
* **Pandas**: For data manipulation.
