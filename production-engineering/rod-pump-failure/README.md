# Rod Pump Failure Prediction using CNNs 🛢️

## Overview
This repository demonstrates a Deep Learning approach to predictive maintenance in the Oil & Gas industry. Specifically, it focuses on identifying **Sucker Rod Pump** failure modes by analyzing **Dynamometer Cards**.

A Dynamometer Card is a plot of Load (y) vs. Position (x) over one pump stroke. The "shape" of this plot is indicative of downhole conditions. We treat this as a Computer Vision problem, converting the plots into images and using a Convolutional Neural Network (CNN) to classify them.

## Use Case: Dynamometer Card Analysis
We aim to classify three specific conditions:
1.  **Normal Operation:** Full pump fill, healthy pump.
2.  **Fluid Pound:** Incomplete pump fill, causing severe mechanical stress.
3.  **Gas Interference:** Gas entering the pump, reducing efficiency.

## Methodology
1.  **Data Ingestion:** Load raw Position vs. Load time-series data.
2.  **Rasterization:** Convert the time-series coordinates into a 64x64 binary image (Matrix).
3.  **Modeling:** Train a 2D CNN (Conv2D -> MaxPool -> Dense) to learn the geometric features of the cards.
4.  **Inference:** Predict the class of new Dyno Cards.

## File Structure
* `synthetic_dyno_cards.csv`: Generated synthetic dataset.
* `01_Data_Generator.py`: Script to recreate the synthetic dataset.
* `02_Dyno_Card_CNN_Analysis.ipynb`: Step-by-step implementation.
