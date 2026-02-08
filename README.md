# Dynamic Traffic Decision Engine (DTDE) Lab

This repository implements a **Dynamic Traffic Decision Engine** designed to optimize multi-cloud/multi-region traffic routing through a composite scoring algorithm.

## ?? The Core Algorithm
The engine calculates a health score ($S_i$) for each backend using the following weighted logic:

$$S_i = (w_h \cdot H_i) + (w_l \cdot \frac{1}{L_i}) + (w_s \cdot S_i)$$

Where:
* **$H_i$**: Health score (success rate over a sliding window).
* **$L_i$**: Observed latency (P95).
* **$S_i$**: Security/Policy status.

## ?? Simulation Results
During the baseline experiment, the engine demonstrated high resilience during a simulated regional failure (Brownout):

| Phase | Winning Region | Status | Score |
| :--- | :--- | :--- | :--- |
| **Healthy** | Region-A | PASS | 1.01 |
| **Failure Start** | Region-A | **FAIL** | 0.60 |
| **Recovery** | **Region-B** | PASS | 0.82 |

**Final Performance:** * **Total Success Rate:** 97%
* **Traffic Shift:** Automatically redirected 60% of traffic to healthy secondaries within 2 request cycles of failure detection.

## ??? Project Structure
* `dtde/models.py`: Data structures for backend telemetry.
* `dtde/telemetry.py`: Sliding window implementation using NumPy.
* `dtde/decision.py`: The scoring engine and selection logic.
* `experiments/`: Simulation scripts to test failure scenarios.

## ?? Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Run simulation: `python -m experiments.run_experiment_baseline_vs_dtde`
