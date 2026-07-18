# Real-Time Kick Detection using Isolation Forest

## 1. Problem Statement
A kick — an unplanned influx of formation fluid into the wellbore — is the precursor
to a blowout. Early detection windows are measured in minutes: the sooner pit gain and
flow anomalies are recognized, the smaller the influx to circulate out. Fixed
thresholds on pit volume generate either alarm fatigue or late detection.

**Operational Impact:**
* **Safety:** Kick detection time directly drives well control severity.
* **Cost:** Small influx = short shut-in; large influx = long kill operations.

## 2. Solution Overview
An **Isolation Forest** — an unsupervised anomaly detector — is trained on normal
drilling data only (no labeled kicks needed, which matches reality: kicks are rare).
It monitors pit gain rate, flow-out/flow-in delta and standpipe pressure together,
flagging joint anomalies that single-channel thresholds miss.

## 3. Fundamental Physics & Features
* **Pit gain rate:** Influx displaces mud into the pits — the classic kick sign.
* **Flow delta (out - in):** Formation fluid adds return flow before pits respond.
* **Standpipe pressure:** Gas-cut mud lightens the annulus and drops SPP.
* Joint behavior matters: connections and mud transfers also move pit volume, which is
  why multivariate detection beats a single pit-volume alarm.

**Algorithm:** Isolation Forest (unsupervised anomaly detection) on rolling features.
**Libraries:** Scikit-Learn, Pandas, Matplotlib.

## 4. Repository Structure
* `kick_detection_timeseries.csv`: Synthetic 1-Hz drilling channel data with 3 kicks.
* `Kick_Detection.ipynb`: Simulation, feature engineering, detection and evaluation.
* `requirements.txt`: List of dependencies.
