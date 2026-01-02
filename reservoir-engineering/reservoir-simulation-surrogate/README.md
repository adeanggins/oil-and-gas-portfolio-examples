# Reservoir Simulation Surrogate Modeling with PyTorch

## 1. Problem Statement
In reservoir engineering, Full-Physics Reservoir Simulations (using tools like Eclipse, CMG, or tNavigator) are the gold standard for predicting field performance. However, they are computationally expensive and time-consuming. A single run can take hours or even days depending on the grid size and complexity.

This creates a bottleneck when performing:
* Uncertainty Quantification (requiring thousands of runs).
* Field Development Optimization.
* Real-time decision making.

## 2. Solution Overview
This project demonstrates the creation of a **Surrogate Model** (also known as a Proxy Model). We train a Deep Neural Network (DNN) to approximate the physics-based simulator. Once trained, this neural network can predict outcomes (e.g., Cumulative Oil Production) in milliseconds, accelerating workflows by orders of magnitude.

## 3. Fundamental Concepts

### The Surrogate Function
Mathematically, if the reservoir simulator is a function $f$ mapping input parameters $x$ to output $y$:
$$y = f(x)$$
We aim to find parameters $\theta$ for a Neural Network $\hat{f}$ such that:
$$\hat{f}(x; \theta) \approx f(x)$$
Minimizing the loss function (Mean Squared Error):
$$L(\theta) = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{f}(x_i; \theta))^2$$

### Workflow
1.  **Design of Experiments (DoE):** (Simulated here) Generate diverse input combinations.
2.  **Data Generation:** Run the full-physics simulator for these inputs to get ground truth labels.
3.  **Model Training:** Train a PyTorch Multi-Layer Perceptron (MLP).
4.  **Validation:** Compare NN predictions against held-out simulator runs.

## 4. Repository Structure
* `01_Data_Generator.ipynb`: Script to generate synthetic dataset representing simulator inputs and outputs.
* `02_Surrogate_Model_Pytorch.ipynb`: The main notebook containing the workflow.
* `reservoir_simulation_data.csv`: Synthetic dataset representing simulator inputs and outputs.
* `requirements.txt`: List of dependencies.

## 5. Usage
1.  Clone the repository.
2.  Install requirements: `pip install -r requirements.txt`
3.  Run the Jupyter Notebook.
