# Example: Closure‑Aware Planning → Behavior

This example demonstrates how predicted future states (closures)  
influence behavior planning.

---

## Input (WLMGraph with closures)

```json
{
  "nodes": [
    {"id": 1, "class": "Robot"},
    {"id": 2, "class": "Box"}
  ],
  "closures": [
    {"type": "future_tension", "tension": "contact", "a": 1, "b": 2},
    {"type": "future_state", "node": 2, "state": "unstable"}
  ],
  "dimensions": {
    "spatial": {},
    "temporal": {},
    "physical": {},
    "causal": {}
  }
}
```

---

## Code

```python
from wlm_agent_behavior import compute_behavior

with open("closure_graph.json") as f:
    graph = json.load(f)

behavior = compute_behavior(graph)
print(behavior)
```

---

## Output (MVP)

```
{
  "actions": [],
  "policy": {
    "strategy": "noop",
    "parameters": {}
  },
  "tensions_resolved": []
}
```

Future versions will produce:

- avoid_future_collision(Robot, Box)  
- pre_stabilize(Box)  

This file will evolve as closure semantics are implemented.
