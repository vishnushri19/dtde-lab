from typing import List, Optional
from dtde.models import BackendState

class DecisionEngine:
    def __init__(self, w_health=0.4, w_latency=0.4, w_security=0.2):
        self.w_health = w_health
        self.w_latency = w_latency
        self.w_security = w_security

    def calculate_score(self, backend: BackendState) -> float:
        """Computes the composite score Si based on your research formula."""
        # Hard stop: If security or policy fails, the backend is disqualified
        if not backend.security_ok or not backend.policy_ok:
            return 0.0

        # Health score (Hi) is 0-1
        # Latency score (Li): We use (1 / latency) normalized. 
        # Adding 1 to avoid division by zero.
        latency_inv = 1.0 / (backend.latency_obs_ms + 1.0)
        
        score = (
            (self.w_health * backend.health_score) +
            (self.w_latency * latency_inv * 100) + # Scaled for visibility
            (self.w_security * backend.security_score)
        )
        return score

    def select_best_backend(self, backends: List[BackendState]) -> Optional[BackendState]:
        """Returns the backend with the highest composite score Si."""
        if not backends:
            return None
        return max(backends, key=self.calculate_score)
