# Drilling Dysfunction Classification: Stick-Slip, Whirl & Bit Bounce

## 1. Problem Statement
Downhole vibration dysfunctions — stick-slip (torsional), whirl (lateral) and bit
bounce (axial) — destroy bits and BHAs and cap ROP. Each dysfunction has a different
cure (change RPM vs. change WOB), so misdiagnosis makes things worse. Surface crews
often cannot tell them apart from raw traces.

**Operational Impact:**
* **Tool failure:** MWD/LWD electronics and PDC cutters fail under sustained vibration.
* **Wrong remediation:** Raising WOB helps whirl but worsens stick-slip.

## 2. Solution Overview
We simulate downhole acceleration/torque signals for four regimes (normal + three
dysfunctions), extract **frequency-domain band energies and statistical features**,
and train a **Support Vector Machine (RBF kernel)** to classify the regime. The
confusion matrix shows which dysfunctions are separable from surface-computable features.

## 3. Fundamental Physics & Features
* **Stick-slip:** Low-frequency (0.1–0.5 Hz) torsional oscillation; RPM swings from 0 to 2× set point.
* **Whirl:** High-frequency lateral vibration at multiples of rotary speed.
* **Bit bounce:** Axial vibration at 3× RPM (tri-cone) or resonance bands.
* Features: band energy ratios, RMS, crest factor, torque variance.

**Algorithm:** SVM (RBF) on FFT band-energy features, with confusion matrix analysis.
**Libraries:** Scikit-Learn, Scipy, Matplotlib.

## 4. Repository Structure
* `vibration_features.csv`: Extracted features per 10-second window.
* `Drilling_Dysfunction_Classification.ipynb`: Signal simulation, feature extraction, SVM.
* `requirements.txt`: List of dependencies.
