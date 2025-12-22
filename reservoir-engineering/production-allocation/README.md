# Oil Production Back-Allocation & Zone Split Analysis

## Problem Statement
In oil field operations, individual wells produce into a commingled pipeline network leading to a central gathering station (Fiscal Meter). While the Fiscal Meter records the exact volume sold or transferred daily ($Q_{fiscal}$), individual wells are not metered continuously. Instead, they are tested periodically (e.g., once a month) using a Test Separator.

**The Challenge:**
1.  **Discrepancy:** The sum of individual well estimates (Theoretical Production) rarely matches the Fiscal Meter readings due to measurement errors, shrinkage, or theft.
2.  **Granularity:** We need to back-allocate the daily fiscal volume to individual wells and subsequently to specific reservoir zones for reservoir management.

## Solution Overview
This repository demonstrates a **Pro-Rata Allocation Method**. We calculate an **Allocation Factor (PAF)** daily to correct the theoretical well rates so they sum up to match the fiscal meter exactly.

## Fundamental Knowledge & Math

### 1. Theoretical Rate Estimation
Since we only have monthly test data, we estimate daily rates for well $i$ on day $t$ ($q_{est, i, t}$) using **Linear Interpolation** or **Forward Fill** between test dates.

### 2. The Allocation Factor (PAF)
The Production Allocation Factor is the ratio of the actual metered volume to the theoretical total.

$$K_t = \frac{Q_{fiscal, t}}{\sum_{i=1}^{n} q_{est, i, t}}$$

Where:
* $K_t$ = Allocation Factor on day $t$
* $Q_{fiscal, t}$ = Total Commingled Production (measured at station)
* $n$ = Total number of wells (10 in this case)

### 3. Back-Allocated Well Production
We adjust the estimated rate for each well by the factor $K$:

$$q_{alloc, i, t} = q_{est, i, t} \times K_t$$

### 4. Zone Interest Split
Finally, we distribute the allocated well volume to specific zones (A, B, C, D) based on zone interest factors ($Z_{zone}$):

$$V_{zone, t} = \sum_{i=1}^{n} (q_{alloc, i, t} \times Z_{i, zone})$$
