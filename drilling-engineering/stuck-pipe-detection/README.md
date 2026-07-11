# Early Stuck Pipe Detection using Gradient Boosting

## 1. Problem Statement
Stuck pipe is one of the most expensive non-productive time (NPT) events in drilling —
a single incident can cost days of fishing, a sidetrack, or a lost BHA. The precursors
(rising drag, tight spots, poor hole cleaning) are visible in surface data well before
the pipe actually sticks, but they are easy to miss on a busy rig floor.

**Operational Impact:**
* **NPT:** Stuck pipe accounts for a large share of global drilling NPT cost.
* **Escalation:** Early response (circulate, ream, adjust mud) is cheap; fishing is not.

## 2. Solution Overview
A **Gradient Boosting Classifier** trained on connection-level snapshots predicts the
probability of a stuck event within the next stand. Because stuck events are rare and
a missed event costs far more than a false alarm, the notebook focuses on the
**precision-recall trade-off and alarm threshold tuning** rather than raw accuracy.

## 3. Fundamental Physics & Features
* **Overpull & drag deviation:** Friction increase from cuttings beds or geometry.
* **Torque trend:** Rising rotating torque signals poor hole cleaning.
* **ECD margin:** Narrow margin to fracture/collapse promotes instability.
* **Stationary time:** Differential sticking risk grows the longer the string is still.

**Algorithm:** Gradient Boosting Classification with threshold optimization.
**Libraries:** Scikit-Learn, Pandas, Matplotlib.

## 4. Repository Structure
* `stuck_pipe_snapshots.csv`: Connection-level synthetic surveillance data.
* `Stuck_Pipe_Detection.ipynb`: Data generation, model, PR analysis and alarm tuning.
* `requirements.txt`: List of dependencies.
