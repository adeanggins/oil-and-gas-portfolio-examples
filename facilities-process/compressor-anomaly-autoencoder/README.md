# Compressor Anomaly Detection with a Dense Autoencoder (PyTorch)

## 1. Problem Statement
Centrifugal compressors are the most critical rotating equipment in gas processing:
an unplanned trip cascades through the whole plant. Failures announce themselves in
multivariate drift — discharge temperature creeping relative to load, efficiency loss,
vibration signature changes — patterns single-tag alarms miss.

**Operational Impact:**
* **Availability:** A compressor trip can shut in an entire field's production.
* **Maintenance:** Early anomaly detection converts breakdowns into planned work.

## 2. Solution Overview
A **dense autoencoder** (PyTorch) is trained on healthy operating data only. The
reconstruction error becomes a health index: normal states reconstruct well, anomalies
don't. The notebook demonstrates detection of two seeded degradations (fouling drift
and a surge precursor) and shows **per-sensor reconstruction error** for diagnosis.

## 3. Fundamental Physics & Features
* **Operating envelope:** Suction/discharge P&T, flow, speed and power are tied by
  compressor physics; the autoencoder learns that manifold.
* **Fouling:** Polytropic efficiency decays — discharge T rises for the same head.
* **Surge precursor:** Flow drops toward the surge line with rising vibration.

**Algorithm:** Dense autoencoder, reconstruction-error monitoring, error attribution.
**Libraries:** PyTorch, Scikit-Learn, Matplotlib.

## 4. Repository Structure
* `compressor_telemetry.csv`: Synthetic hourly telemetry with seeded anomalies.
* `Compressor_Anomaly_Autoencoder.ipynb`: Simulation, training, monitoring, diagnosis.
* `requirements.txt`: List of dependencies.
