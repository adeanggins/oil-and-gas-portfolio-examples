# Relative Permeability Upscaling: Capacity-Weighted Method

## 📌 Problem Statement
In Reservoir Simulation, geological models often contain millions of fine-scale cells. Running flow simulations on such high-resolution grids is computationally expensive. To overcome this, engineers "upscale" these properties to a coarser grid.

While absolute permeability ($k$) upscaling is common, **Relative Permeability ($k_r$)** upscaling is more complex because it is saturation-dependent. Simply averaging the curves without considering the flow capacity of each rock type can lead to inaccurate predictions of water breakthrough and oil recovery.

## 🎯 Solution
This repository provides a Python-based solution to upscale fine-scale relative permeability curves into a single effective coarse-scale curve using the **Capacity-Weighted Averaging** method.

This method assumes:
1.  **Parallel Flow:** Layers are arranged parallel to the flow direction.
2.  **Viscous Limit:** Capillary pressure effects are negligible compared to viscous forces (vertical equilibrium is not dominated by gravity/capillarity).
3.  **Communication:** There is no cross-flow between layers (or effectively modeled as such for linear averaging).

## 🧠 Fundamental Knowledge

### 1. Corey's Correlation (Fine Scale)
We generate synthetic fine-scale curves for each layer using the Corey approximation:

$$k_{rw} = k_{rw}^0 \left( \frac{S_w - S_{wi}}{1 - S_{wi} - S_{or}} \right)^{n_w}$$

$$k_{ro} = k_{ro}^0 \left( \frac{1 - S_w - S_{or}}{1 - S_{wi} - S_{or}} \right)^{n_o}$$

### 2. The Upscaling Equation
The effective relative permeability for the coarse block at a specific water saturation ($S_w$) is derived by summing the flow rates of individual layers (Darcy's Law).

For a system of $N$ parallel layers, the effective relative permeability is the arithmetic average weighted by the **Transmissibility** (or flow capacity, $k_i \cdot h_i$) of each layer:

$$K_{r,coarse}(S_w) = \frac{\sum_{i=1}^{N} (k_i \cdot h_i \cdot k_{r,i}(S_w))}{\sum_{i=1}^{N} (k_i \cdot h_i)}$$

Where:
* $k_i$: Absolute permeability of layer $i$
* $h_i$: Thickness of layer $i$
* $k_{r,i}(S_w)$: Relative permeability of layer $i$ at saturation $S_w$

## 📂 Repository Contents
* `fine_scale_layers.csv`: Input data containing petrophysical properties and Corey parameters for distinct rock layers.
* `relperm_upscaling_demo.ipynb`: A step-by-step Jupyter Notebook demonstrating the calculation and visualization.

## 🚀 Usage
1.  Install dependencies: `pip install -r requirements.txt`
2.  Run the notebook: `jupyter notebook relperm_upscaling_demo.ipynb`
