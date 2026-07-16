# HSE Incident Narrative Topic Modeling (NMF)

## 1. Problem Statement
Incident and near-miss registers hold thousands of free-text narratives that nobody
reads end-to-end. Category codes capture what the reporter chose from a dropdown —
not the recurring situational patterns (night-shift lifting jobs, hand injuries during
valve work) that actually drive prevention programs.

**Operational Impact:**
* **Prevention targeting:** Themes → focused campaigns beat generic safety messaging.
* **Emerging risk:** Topic trends surface new failure patterns before they escalate.

## 2. Solution Overview
**Non-negative Matrix Factorization (NMF)** on TF-IDF vectors decomposes narratives
into interpretable topics (additive parts, unlike LDA's harder-to-tune priors on short
texts). The notebook covers topic-count selection, labeling from top terms, alignment
with (deliberately noisy) reporter categories, and **topic trends over time**.

## 3. Fundamental Physics & Features
* **TF-IDF:** Downweights boilerplate ("employee was", "no injury") that dominates
  incident text.
* **NMF parts-based decomposition:** Each narrative = non-negative mix of topics —
  matches how incidents combine themes (a *dropped object* during *crane ops* at *night*).

**Algorithm:** TF-IDF + NMF, reconstruction-error selection, topic-time analysis.
**Libraries:** Scikit-Learn, Pandas, Matplotlib.

## 4. Repository Structure
* `incident_narratives.csv`: Synthetic incident register with narratives.
* `Incident_Topic_Modeling.ipynb`: Vectorization, NMF, labeling, trends.
* `requirements.txt`: List of dependencies.
