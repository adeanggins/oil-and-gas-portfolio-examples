# Voronoi Drainage Area Analysis

## Problem Statement
In reservoir engineering, determining the **drainage area** of a producing well is critical for estimating Original Oil in Place (OOIP) and optimizing well spacing. In mature fields with irregular well patterns, simple geometric assignments (like uniform squares) are inaccurate. Engineers need a robust mathematical method to approximate the territory "owned" by each well based on proximity.

## Solution
This repository demonstrates how to use **Voronoi Tessellation** (also known as Thiessen Polygons) to mathematically partition a reservoir.

A Voronoi diagram divides a plane into regions close to each of a given set of objects. For well placement, it ensures that every point within a specific polygon is closer to the well at its center than to any other well in the field. This serves as an excellent geometric proxy for the drainage area in homogenous reservoirs.

## Fundamental Concepts

### Voronoi Tessellation
Given a set of well locations $P = \{p_1, p_2, ..., p_n\}$, the Voronoi cell $R_k$ associated with well $p_k$ is defined as:

$$R_k = \{x \in X \mid d(x, p_k) \le d(x, p_j) \text{ for all } j \neq k\}$$

Where:
- $d(x, p)$ is the Euclidean distance between point $x$ and well location $p$.
- The resulting boundaries (ridges) are perpendicular bisectors of the lines connecting neighboring wells.

### Implementation Details
- **Library**: `scipy.spatial`
- **Logic**: We generate the tessellation and clip the resulting polygons to the reservoir boundaries (or a defined bounding box) to ensure finite area calculations.
