# Well Log QC: Outlier Detection with LOF & DBSCAN

## 1. Problem Statement
Petrophysical workflows are only as good as their input logs. Washouts, tool sticking,
cycle skipping and spliced runs contaminate GR/RHOB/NPHI/DTC curves, and manual QC of
hundreds of wells is a bottleneck. The failure modes are *multivariate*: a density
reading can be individually plausible yet impossible given the neutron and caliper.

**Operational Impact:**
* **Downstream bias:** Bad density in a washout maps straight into porosity error.
* **Scale:** Field reviews need thousands of curves QC'd consistently.

## 2. Solution Overview
Two unsupervised detectors are compared for automated log QC: **Local Outlier Factor**
(density-based, local context) and **DBSCAN** (clustering with a noise class). Both are
run in a standardized multi-log feature space with caliper included, and evaluated
against the known corrupted intervals.

## 3. Fundamental Physics & Features
* **Washouts:** Enlarged caliper + underread density + overread neutron — a joint signature.
* **Cycle skips:** DTC jumps to implausible values inconsistent with density.
* **Feature space:** standardized GR, RHOB, NPHI, DTC, CALI + local rolling deviations.

**Algorithm:** Local Outlier Factor vs. DBSCAN, precision/recall on corrupted intervals.
**Libraries:** Scikit-Learn, Seaborn, Matplotlib.

## 4. Repository Structure
* `well_logs_qc.csv`: Synthetic multi-well logs with labeled corrupted zones.
* `Well_Log_Outlier_Detection.ipynb`: Corruption simulation, detectors, comparison.
* `requirements.txt`: List of dependencies.
