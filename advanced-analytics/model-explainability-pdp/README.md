# Opening the Black Box: Permutation Importance & Partial Dependence

## 1. Problem Statement
The fastest way to kill an ML project in a petroleum engineering organization is a
model nobody can interrogate. Engineers rightly demand: which inputs matter, in which
direction, over what range — and does that match the physics? Explainability is not a
nicety; it is the acceptance test.

**Operational Impact:**
* **Model trust & adoption:** Engineers sign off on mechanisms, not AUCs.
* **Debugging:** Wrong-direction dependence usually means leakage or bad data —
  explainability catches it before deployment.

## 2. Solution Overview
A Gradient Boosting model of well productivity is dissected with the standard
global-explainability toolkit: **permutation importance** (with the
correlated-features caveat demonstrated, not just mentioned), **partial dependence +
ICE curves** (average vs heterogeneous effects), and a **2D interaction PDP**. One
deliberately planted data-leak feature shows how explainability exposes it.

## 3. Fundamental Physics & Features
* **Sanity anchors:** Productivity should rise with kh and lateral length, fall with
  depletion — the model's PDPs are checked against these.
* **Leak plant:** A "post-job efficiency" feature only knowable after outcome —
  importance analysis flags it as suspiciously dominant.

**Algorithm:** Permutation importance, PDP/ICE, 2D interaction PDP, leakage detection.
**Libraries:** Scikit-Learn, Matplotlib.

## 4. Repository Structure
* `productivity_dataset.csv`: Synthetic well productivity data (with planted leak).
* `Model_Explainability_PDP.ipynb`: Full explainability workflow.
* `requirements.txt`: List of dependencies.
