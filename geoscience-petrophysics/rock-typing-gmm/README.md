# Probabilistic Rock Typing with Gaussian Mixture Models

## 1. Problem Statement
Rock typing — grouping reservoir rock into classes with common flow behavior — underpins
saturation-height modeling, simulation upscaling and perforation strategy. Hard
clustering (K-Means) forces every sample into one type, hiding the transitional rocks
where most classification mistakes (and completion surprises) happen.

**Operational Impact:**
* **Simulation:** Rock types carry rel-perm and capillary pressure assignments.
* **Completion:** Transitional rock misclassified as pay changes perf decisions.

## 2. Solution Overview
A **Gaussian Mixture Model** clusters samples in (porosity, log-permeability, GR) space,
with the number of components selected by **BIC**. Unlike K-Means, the GMM returns
**membership probabilities**, so every sample carries its classification confidence —
and the transitional rocks are explicitly visible.

## 3. Fundamental Physics & Features
* **Poro-perm clusters:** Rock types form elongated, correlated clusters in φ-log(k)
  space (Winland/FZI behavior) — full-covariance Gaussians fit this naturally.
* **GR:** separates clay-supported textures with similar φ but different k.

**Algorithm:** Gaussian Mixture Model, full covariance, BIC model selection.
**Libraries:** Scikit-Learn, Seaborn, Matplotlib.

## 4. Repository Structure
* `core_rocktype_data.csv`: Synthetic core analysis dataset.
* `Rock_Typing_GMM.ipynb`: BIC selection, GMM fit, probability mapping.
* `requirements.txt`: List of dependencies.
