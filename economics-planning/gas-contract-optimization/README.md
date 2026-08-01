# Take-or-Pay Gas Contract Optimization

## 1. Problem Statement
Gas supply portfolios mix take-or-pay pipeline contracts (pay for the ACQ whether you
lift it or not, with make-up rights), spot purchases and storage. Deciding how much to
lift from each source each month — against seasonal demand and prices — is a linear
program that treasury and gas-supply desks often approximate with rules of thumb.

**Operational Impact:**
* **Real money:** Poorly timed TOP liftings vs spot purchases cost millions per year.
* **Make-up bank:** Unused prepaid gas expires if not scheduled deliberately.

## 2. Solution Overview
A 24-month **linear program (PuLP)** dispatches TOP contract gas, spot purchases and a
storage facility against demand, minimizing total cost with take-or-pay minimum-bill
and make-up-bank accounting modeled explicitly. Comparison against a
"contract-first" heuristic and a spot-price sensitivity complete the analysis.

## 3. Fundamental Physics & Features
* **Minimum bill:** Pay max(lifted, TOP%·ACQ); shortfall becomes a make-up bank with
  expiry.
* **Storage:** Injection/withdrawal limits and cycling cost couple months together.
* **Seasonality:** Winter demand and winter spot premium create the arbitrage.

**Algorithm:** Multi-period LP with inventory balances (PuLP/CBC).
**Libraries:** PuLP, Pandas, Matplotlib.

## 4. Repository Structure
* `gas_portfolio_inputs.csv`: Demand, prices and contract terms.
* `Gas_Contract_Optimization.ipynb`: LP, dispatch plot, sensitivity.
* `requirements.txt`: List of dependencies.
