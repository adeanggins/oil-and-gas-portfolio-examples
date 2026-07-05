# Seismic Facies Classification with 2D CNN (PyTorch)

## 1. Problem Statement
Interpreting seismic facies — channel fills, wedges, parallel continuous reflectors,
chaotic zones — over thousands of square kilometers is slow, subjective work. CNNs can
learn the textural signatures interpreters use and apply them consistently at volume scale.

**Operational Impact:**
* **Cycle time:** Facies screening of a survey drops from weeks to hours.
* **Consistency:** The same model applies the same criteria everywhere — no interpreter drift.

## 2. Solution Overview
A compact **2D convolutional neural network** (PyTorch) classifies 32×32 seismic patches
into four facies. Synthetic patches are built with geologically motivated texture models
(dipping wedges, channel cross-sections, chaotic slumps). The notebook covers training
curves, confusion matrix and — importantly — a look at the misclassified patches.

## 3. Fundamental Physics & Features
* **Facies texture:** Reflector continuity, dip, amplitude and frequency content are the
  discriminating textures — exactly what convolution kernels detect.
* **Patch-based inference:** Sliding-window classification maps facies across a section.

**Algorithm:** 2D CNN (3 conv blocks), Adam optimizer, cross-entropy loss.
**Libraries:** PyTorch, Scikit-Learn, Matplotlib.

## 4. Repository Structure
* `seismic_patch_labels.csv`: Patch metadata and labels (arrays generated in-notebook).
* `Seismic_Facies_CNN.ipynb`: Patch synthesis, CNN training, evaluation, section map.
* `requirements.txt`: List of dependencies.
