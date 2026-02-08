# experiments/run_experiment_baseline_vs_dtde.py
from dtde.models import BackendState

def main():
    # For now, just create a few backends and print them.
    backends = [
        BackendState(id="b1", base_latency_ms=200.0, failure_rate=0.01),
        BackendState(id="b2", base_latency_ms=220.0, failure_rate=0.01),
        BackendState(id="b3", base_latency_ms=250.0, failure_rate=0.01),
    ]
    for b in backends:
        print(b)

if __name__ == "__main__":
    main()
