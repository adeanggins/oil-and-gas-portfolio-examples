# Automated First-Break Picking: STA/LTA + ML Refinement

## 1. Problem Statement
First-break picking — identifying the first seismic energy arrival on each trace — is
required for refraction statics and near-surface velocity models. Surveys contain
millions of traces; manual picking is impossible at scale and pure threshold triggers
fail on noisy traces.

**Operational Impact:**
* **Statics quality:** Bad picks propagate into structural distortions on the stack.
* **Turnaround:** Automated picking removes a major processing bottleneck.

## 2. Solution Overview
A two-stage picker: the classic **STA/LTA (short-term/long-term average) trigger**
proposes candidate onsets, then a **Random Forest** trained on trace attributes around
each candidate refines the pick. Evaluation reports pick error distributions against
ground truth at multiple noise levels.

## 3. Fundamental Physics & Features
* **STA/LTA:** Energy ratio spikes at signal onset; robust but biased late on emergent
  arrivals and fooled by noise bursts.
* **Refinement features:** local energy ratios, sign-change density, envelope slope,
  ratio of pre/post RMS in several windows.

**Algorithm:** STA/LTA trigger + Random Forest regression refinement.
**Libraries:** Numpy, Scikit-Learn, Matplotlib.

## 4. Repository Structure
* `first_break_picks.csv`: Trace-level true vs picked onset times.
* `First_Break_Picking.ipynb`: Simulation, STA/LTA, ML refinement, error analysis.
* `requirements.txt`: List of dependencies.
