# EOS-Based Reservoir Compartmentalization Clustering

## Problem Statement
In reservoir engineering, accurately defining reservoir compartments is critical for estimating reserves and planning field development. Traditional methods rely on pressure gradients and geological interpretation. However, subtle differences in fluid composition (Equation of State components) can often reveal flow barriers that pressure data might miss.

The challenge is to analyze hundreds of fluid samples from various wells and group them into distinct hydraulic flow units based solely on their molar composition ($C_1$ through $C_{7+}$).

## Solution Approach
This project utilizes **Unsupervised Machine Learning** to detect compartmentalization. By treating the molar fractions of fluid components as features, we apply **K-Means Clustering** to identify natural groupings in the data.

### Fundamental Knowledge
Fluids in connected reservoir volumes tend to equilibrate over geological time, resulting in a consistent composition (gravity grading aside). Conversely, fluids separated by sealing faults or stratigraphic barriers often evolve differently or have different source charges.

We use **K-Means**, an algorithm that partitions $n$ samples into $k$ clusters by minimizing the within-cluster sum of squares (WCSS), also known as inertia:

$$\sum_{i=0}^{n} \min_{\mu_j \in C} (||x_i - \mu_j||^2)$$

Where:
* $x_i$ is a fluid sample vector (compositions).
* $\mu_j$ is the centroid of cluster $j$.

### Contents
1.  `01_Data_Generator.ipynb`: The notebook containing the script to generate synthetic data.
2.  `02_EOS_Clustering_Analysis.ipynb`: The main notebook containing the logic, visualization, and step-by-step explanation.
3.  `fluid_samples.csv`: Synthetic dataset containing molar fractions ($N_2$ to $C_{7+}$) for 250 samples.

### Libraries Used
* **Pandas**: Data manipulation.
* **Scikit-Learn**: K-Means clustering, PCA (for visualization), and Standardization.
* **Matplotlib/Seaborn**: Visualization.
