# PDC Bit Wear Prediction with XGBoost

## 1. Problem Statement
Pulling a bit too early wastes a trip; pulling too late means drilling with a dull bit
(slow ROP) or, worse, leaving cutters in the hole. Dull grade is only known after the
bit is pulled — an ideal target for predictive modeling from while-drilling data.

**Operational Impact:**
* **Trip optimization:** A round trip at depth can cost 12+ hours of rig time.
* **Bit selection:** Wear models feed back into bit design and parameter roadmaps.

## 2. Solution Overview
An **XGBoost regressor** predicts the IADC-style dull grade (0–8 scale) from cumulative
drilling energy metrics: mechanical specific energy (MSE), cumulative revolutions,
footage in abrasive formations, and vibration exposure. **Permutation importance**
identifies the dominant wear drivers.

## 3. Fundamental Physics & Features
* **Cumulative work:** Wear scales with total energy through the cutters (WOB × revs).
* **Abrasive footage:** Quartz-rich sandstone footage wears PDCs disproportionately.
* **MSE:** High mechanical specific energy indicates inefficient, wear-intensive drilling.
* **Vibration exposure:** Impact damage accelerates cutter chipping.

**Algorithm:** XGBoost regression + permutation importance.
**Libraries:** XGBoost, Scikit-Learn, Matplotlib.

## 4. Repository Structure
* `bit_run_history.csv`: Synthetic bit run records with dull grades.
* `Bit_Wear_Prediction.ipynb`: Data generation, model training and interpretation.
* `requirements.txt`: List of dependencies.
