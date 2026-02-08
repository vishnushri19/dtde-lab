import numpy as np
from typing import List
from dtde.models import BackendState, RequestResult

class TelemetryMonitor:
    def __init__(self, window_size: int = 50):
        self.window_size = window_size

    def update_backend(self, backend: BackendState, result: RequestResult):
        """Updates the backend sliding windows with a new request result."""
        # 1. Update Latency History
        backend.latency_history.append(result.latency_ms)
        if len(backend.latency_history) > self.window_size:
            backend.latency_history.pop(0)
        
        # 2. Update Success History
        backend.success_history.append(result.success)
        if len(backend.success_history) > self.window_size:
            backend.success_history.pop(0)

        # 3. Calculate Derived Metrics
        if backend.latency_history:
            # We use P95 latency to be sensitive to "tail" issues
            backend.latency_obs_ms = float(np.percentile(backend.latency_history, 95))
        
        if backend.success_history:
            # Health score is the ratio of successful requests in the window
            success_count = sum(1 for x in backend.success_history if x)
            backend.health_score = success_count / len(backend.success_history)
