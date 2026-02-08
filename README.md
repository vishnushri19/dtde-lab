# DTDE Lab – Dynamic Traffic Decision Engine Simulation

This repository contains a small, reproducible lab that demonstrates the core ideas
from the paper **"Dynamic Traffic Decision Engine (DTDE) for Application Delivery Networks"**.

The lab simulates multiple backends with changing health, latency, and security posture,
then compares:

- A static policy (round robin)
- The DTDE composite-scoring decision engine

Key metrics:

- Mean response time
- P95 latency
- Availability (fraction of successful requests)
- A simple MTTR-like measure from failure streaks

## Status

Work in progress. Initial skeleton:

- `dtde/`: core engine (models, telemetry, decision logic, simulation)
- `experiments/`: scripts to run baseline vs. DTDE experiments
- `configs/`: configuration for weights and policies

## Planned next steps

1. Define data models for backends and requests.
2. Implement telemetry and sliding-window health calculations.
3. Implement composite scoring and DTDE routing policy.
4. Implement baseline round-robin policy.
5. Build a simple simulation loop and metrics.
6. Document sample results in this README.
