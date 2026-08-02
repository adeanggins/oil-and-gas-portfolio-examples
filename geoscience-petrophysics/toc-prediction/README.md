# TOC Prediction: Passey ΔlogR vs. Random Forest

## 1. Problem Statement
Total Organic Carbon (TOC) defines source rock quality and shale-play sweet spots, but
lab TOC exists only at core plugs. Estimating TOC continuously from standard logs is a
classic petrophysics problem: the industry workhorse is Passey's ΔlogR overlay, which
assumes a known level of maturity (LOM) and a proper baseline — both frequent error sources.

**Operational Impact:**
* **Sweet spot mapping:** TOC drives landing-zone selection in unconventionals.
* **Resource assessment:** Basin-scale TOC errors compound into resource errors.

## 2. Solution Overview
Passey's ΔlogR method is implemented and honestly tuned, then compared against a
**Random Forest** trained on triple-combo logs with core TOC as labels. Validation is
**leave-one-well-out** so both methods face the same generalization test.

## 3. Fundamental Physics & Features
* **ΔlogR physics:** Organic matter raises resistivity (non-conductive kerogen) and
  sonic (kerogen is slow); their overlay separation scales with TOC and maturity.
* **RF features:** GR (uranium-organic association), DTC, RES, RHOB (kerogen is light),
  NPHI.

**Algorithm:** Passey ΔlogR (physics) vs. Random Forest (data-driven), LOWO validation.
**Libraries:** Scikit-Learn, Pandas, Matplotlib.

## 4. Repository Structure
* `toc_log_core_data.csv`: Synthetic log + core TOC dataset (5 wells).
* `TOC_Prediction.ipynb`: Both methods, comparison, TOC track display.
* `requirements.txt`: List of dependencies.
