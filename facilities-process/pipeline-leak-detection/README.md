# Pipeline Leak Detection with Mass Balance + CUSUM

## 1. Problem Statement
Small pipeline leaks hide inside metering noise: a 0.5% leak is invisible against 1%
meter uncertainty on any single reading. Detecting it requires accumulating evidence
over time — the classic sequential changepoint problem. Regulators increasingly demand
quantified leak detection capability (sensitivity vs response time).

**Operational Impact:**
* **HSE & environment:** Detection delay directly scales spill volume.
* **Compliance:** API 1130 requires documented leak detection performance.

## 2. Solution Overview
A **volume-balance** residual (line-pack-corrected inflow minus outflow) is monitored
with **CUSUM (cumulative sum) changepoint detection**. The notebook derives the
detection-delay vs false-alarm trade-off as a function of leak size, producing the
**sensitivity curve** regulators and control rooms actually use.

## 3. Fundamental Physics & Features
* **Mass balance:** In − Out − ΔLinepack = 0 for a tight line; a leak shifts the mean
  of the residual.
* **Line pack:** Pressure/temperature-driven inventory changes must be corrected or
  they swamp small leaks.
* **CUSUM:** Optimal-ish sequential test for a mean shift; tunable drift/threshold.

**Algorithm:** Volume balance + two-sided CUSUM, Monte Carlo performance curves.
**Libraries:** Numpy, Pandas, Matplotlib.

## 4. Repository Structure
* `pipeline_flow_data.csv`: Synthetic 1-min metering data with seeded leaks.
* `Pipeline_Leak_Detection.ipynb`: Balance, CUSUM, sensitivity analysis.
* `requirements.txt`: List of dependencies.
