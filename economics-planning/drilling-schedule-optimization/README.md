# Rig Scheduling Optimization with MILP

## 1. Problem Statement
A development campaign must sequence wells across a limited rig fleet. Wells differ in
value and duration, some have precedence constraints (pads, facilities readiness), and
NPV decays with delay — every month a good well waits costs discounted barrels.
Spreadsheet sequencing leaves substantial value on the table once the problem exceeds
a handful of wells.

**Operational Impact:**
* **NPV:** Sequencing determines when production starts, well by well.
* **Rig contracts:** The marginal value of a third rig is a scheduling question.

## 2. Solution Overview
A **mixed-integer linear program** (PuLP/CBC) assigns wells to rigs and time slots,
maximizing discounted NPV under rig-capacity, precedence and facility-readiness
constraints. Output includes the **Gantt chart**, comparison against a
highest-value-first heuristic, and the **marginal value of an additional rig**.

## 3. Fundamental Physics & Features
* **Discounting:** NPV_i(t) = NPV_i · δ^t — delay cost baked into the objective.
* **Assignment structure:** x[well, rig, start] binary; durations occupy rig-months.
* **Precedence:** Water injectors after their producers; pad order constraints.

**Algorithm:** Time-indexed MILP + heuristic benchmark + fleet-size sensitivity.
**Libraries:** PuLP, Pandas, Matplotlib.

## 4. Repository Structure
* `well_schedule_inputs.csv`: Well list with values, durations, constraints.
* `Drilling_Schedule_Optimization.ipynb`: MILP, Gantt, sensitivities.
* `requirements.txt`: List of dependencies.
