# Streamline-Based Reservoir Connectivity & Drainage Visualization

## Problem Statement
In reservoir engineering, understanding the flow path of fluids from injectors to producers is critical for waterflood optimization. Traditional grid-based simulation results (saturation/pressure maps) often fail to explicitly show:
1. **Injector-Producer Connectivity:** Which injector is supporting which producer?
2. **Drainage Areas:** What volume of the reservoir is actually being drained by a specific well?
3. **Short-circuiting:** Are fluids moving too fast through high-permeability streaks (thief zones)?

## The Solution
This project utilizes **Streamline Simulation Data** to visualize these flow behaviors. By parsing streamline geometry and Time-of-Flight (TOF) data, we can:
* Visualize 3D flow paths using **PyVista**.
* Quantify and plot connectivity matrices using **Plotly**.

## Fundamental Concepts
* **Streamline:** A line that is everywhere tangent to the velocity vector of the fluid at a given instant. It represents the path a fluid particle takes.
* **Time of Flight (TOF):** The time required for a particle to travel from an injector to a specific point along the streamline.
* **Drainage Volume:** The collection of all streamlines arriving at a specific producer.
* **Well Allocation Factor (WAF):** The fraction of total injection from Well A that arrives at Well B.

## Repository Structure
* `Streamline_Analysis.ipynb`: The main workflow for parsing and visualization.
* `streamline_data.csv`: Sample output data containing streamline traces (x, y, z, TOF).
* `requirements.txt`: List of dependencies.

## Usage
1. Install requirements: `pip install -r requirements.txt`
2. Run the Jupyter Notebook: `jupyter notebook Streamline_Analysis.ipynb`
