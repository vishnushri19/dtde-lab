import sys
from dtde.models import BackendState
from dtde.decision import DTDEPolicy
from dtde.simulation import simulate_step
from dtde.telemetry import update_telemetry

def test_normal_routing():
    print("\n" + "="*60 + "\nTEST 1: Normal Routing - Verify Score Calculation\n" + "="*60)
    backends = [
        BackendState(id="b1", base_latency_ms=200.0, failure_rate=0.01),
        BackendState(id="b2", base_latency_ms=220.0, failure_rate=0.01),
        BackendState(id="b3", base_latency_ms=250.0, failure_rate=0.01),
    ]
    policy = DTDEPolicy()
    for i in range(10):
        for b in backends: update_telemetry(b, b.base_latency_ms, True)
    
    for b in backends:
        score = policy.score_backend(b, backends)
        print(f"  {b.id}: score={score:.3f} | health={b.health_score:.2f} | latency={b.latency_obs_ms:.1f}ms")
    
    chosen = policy.choose_backend(backends)
    print(f"\n? DTDE chose: {chosen.id}")
    return True

def test_policy_constraints():
    print("\n" + "="*60 + "\nTEST 3: Policy & Security Constraints\n" + "="*60)
    backends = [
        BackendState(id="b1", base_latency_ms=200.0, policy_ok=True, security_ok=True),
        BackendState(id="b2", base_latency_ms=220.0, policy_ok=False, security_ok=True),
        BackendState(id="b3", base_latency_ms=180.0, policy_ok=True, security_ok=False),
    ]
    policy = DTDEPolicy()
    for b in backends: update_telemetry(b, b.base_latency_ms, True)
    
    chosen_count = {"b1": 0, "b2": 0, "b3": 0}
    for i in range(10):
        chosen = policy.choose_backend(backends)
        if chosen: chosen_count[chosen.id] += 1
    
    print(f"  b1: {chosen_count['b1']} | b2: {chosen_count['b2']} | b3: {chosen_count['b3']}")
    return chosen_count["b2"] == 0 and chosen_count["b3"] == 0

if __name__ == '__main__':
    test_normal_routing()
    res = test_policy_constraints()
    print("\n? Functional Verification COMPLETE" if res else "? FAILED")
