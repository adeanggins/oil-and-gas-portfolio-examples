# Hydrate Formation Risk along Flowlines

## 1. Problem Statement
Gas hydrates plug subsea flowlines and wellheads when water, gas, high pressure and low
temperature coincide. Flow assurance engineers screen operating points against hydrate
equilibrium curves; the operational question is whether a given (P, T, inhibitor)
combination is safe — across thousands of hourly operating points.

**Operational Impact:**
* **Blockage remediation:** A hydrate plug in a subsea line can take weeks to melt.
* **MEG/MeOH cost:** Over-inhibition wastes chemicals; under-inhibition risks plugs.

## 2. Solution Overview
A **logistic regression** classifier learns the hydrate risk boundary from historical
operating points, and is compared against the **Katz-style equilibrium curve** it should
rediscover. The linear-in-features model with a log-pressure term makes the learned
boundary directly comparable to the thermodynamic curve, including the **MEG inhibition
shift**.

## 3. Fundamental Physics & Features
* **Equilibrium curve:** Hydrate stability T rises ~logarithmically with pressure.
* **Inhibitor shift:** MEG depresses the hydrate temperature (Hammerschmidt behavior).
* **Subcooling:** Distance below the curve — the physically meaningful risk metric.

**Algorithm:** Logistic regression with physics-comparable features + decision boundary
visualization.
**Libraries:** Scikit-Learn, Pandas, Matplotlib.

## 4. Repository Structure
* `flowline_operating_points.csv`: Synthetic operating history with hydrate events.
* `Hydrate_Risk_Classification.ipynb`: Physics curve, classifier, operating envelope.
* `requirements.txt`: List of dependencies.
