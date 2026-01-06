# Water Recirculation Analysis: Tracer Data

## Problem Statement
In secondary oil recovery (waterflooding), water is injected into the reservoir to maintain pressure and sweep oil towards producer wells. Over time, some of this injected water breaks through to the producers. This is known as "water recycling."

Excessive water recycling is inefficient because it cycles water through the reservoir without contacting new oil. Identifying which producers are recycling water—and how much—is critical for optimizing injection rates and conforming control strategies.

## Solution Approach
This project analyzes chemical tracer data to calculate the **Water Recirculation Fraction (WRF)**. By comparing the concentration of a specific tracer found in producer wells against the concentration of the tracer in the injected water, we can quantify the percentage of produced water that is actually recycled injection water.

## Fundamental Calculation
The analysis relies on a mass balance principle. Assuming the reservoir formation water has a tracer concentration of 0 ppm, the Recirculation Fraction ($F_{rec}$) is calculated as:

$$F_{rec} = \frac{C_{prod} - C_{formation}}{C_{inj} - C_{formation}}$$

Assuming $C_{formation} \approx 0$:

$$F_{rec} (\%)= \left( \frac{C_{prod}}{C_{inj}} \right) \times 100$$

Where:
* $C_{prod}$: Tracer concentration measured at the producer well (ppm).
* $C_{inj}$: Tracer concentration measured at the injector well (ppm).

## Repository Contents
* `01_Data_Generator.ipynb`: Script to generate synthetic dataset with 10 injectors and 40 producers.
* `02_Analysis.ipynb`: Jupyter Notebook containing the step-by-step logic and visualization.
* `water_recirculation_data.csv`: Synthetic dataset with 10 injectors and 40 producers.
* `requirements.txt`: List of required Python libraries.
