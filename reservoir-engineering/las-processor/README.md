# LAS File Bulk Processor & Normalizer

## 📌 Problem Statement
In the oil and gas industry, subsurface data is often stored in **Legacy ASCII Standard (LAS)** files. A major challenge in reservoir characterization is handling large volumes of these files acquired over decades by different service companies. Common issues include:
* **Inconsistent Mnemonics:** Gamma Ray might be labeled as `GR`, `G.R.`, `GAMMA`, or `GR_FINAL`.
* **Noisy Data:** Null values often use non-standard indicators (e.g., `-999.25`, `0`, or `NaN`).
* **Fragmentation:** Data is scattered across hundreds of individual files rather than a structured database.

## 🎯 Solution
This project implements a bulk processing pipeline using **Python**, **Lasio**, and **Welly**. It automates the ingestion of raw well logs, normalizes curve names to a standard naming convention, cleanses null values, and exports a unified dataset ready for Machine Learning or Petrophysical analysis.

## ⚙️ Fundamental Knowledge
### 1. The LAS Standard
The LAS format is structured into sections (Version, Well, Curve, Parameter, Data). The challenge lies in the **Curve Information** section, where naming conventions vary wildly between vendors (Schlumberger, Halliburton, etc.).

### 2. Mnemonic Normalization
We use an alias mapping strategy. Mathematically, this is a set mapping function $f: S \rightarrow T$, where $S$ is the set of all observed curve names (e.g., $\{GR, G.R., GAMMA\}$) and $T$ is the target standard set (e.g., $\{GR\}$).

### 3. Null Value Handling
LAS files often use specific "null" integers (like `-999.25`). The pipeline identifies these based on the header information and converts them to standard `numpy.nan` for accurate statistical analysis (mean, variance, etc.).

## 🛠️ Tech Stack
* **Lasio:** For low-level LAS file reading and writing.
* **Welly:** For high-level project management, data quality checks, and curve aliasing.
* **Pandas:** For data manipulation and aggregation.