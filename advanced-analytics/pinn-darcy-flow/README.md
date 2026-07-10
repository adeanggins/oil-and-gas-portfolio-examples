# Physics-Informed Neural Network for 1D Pressure Diffusion (PyTorch)

## 1. Problem Statement
Reservoir pressure diffusion is governed by a PDE. Data-driven surrogates ignore the
PDE and need dense training data; numerical solvers need meshes and can't natively
assimilate scattered measurements. **Physics-informed neural networks (PINNs)** put
the PDE residual into the loss function, learning solutions that honor physics with
little or no labeled data.

**Operational Impact:**
* **Data-sparse surrogacy:** PINNs interpolate pressure between sparse gauges lawfully.
* **Inverse problems:** The same machinery estimates diffusivity from pressure data.

## 2. Solution Overview
A PINN solves the 1D diffusivity equation ∂p/∂t = η·∂²p/∂x² (drawdown between a
constant-pressure boundary and a producing face) using **automatic differentiation**
to compute PDE residuals at collocation points. Validation is against the analytical
Fourier-series solution, plus a comparison against a purely data-driven network given
the same sparse observations.

## 3. Fundamental Physics & Features
* **Diffusivity equation:** Linear pressure transient physics — the cleanest testbed.
* **Loss = data + PDE + BC/IC:** Weighted multi-objective; the PDE term is what
  regularizes between observations.

**Algorithm:** PINN (autograd PDE residual) vs data-only NN vs analytical truth.
**Libraries:** PyTorch, Numpy, Matplotlib.

## 4. Repository Structure
* `pinn_observations.csv`: Sparse synthetic gauge observations.
* `PINN_Darcy_Flow.ipynb`: PINN training, validation, comparison.
* `requirements.txt`: List of dependencies.
