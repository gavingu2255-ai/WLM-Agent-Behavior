# Example: WLMGraph → BehaviorPlan

This example demonstrates how a WLM structural graph flows through  
the WLM‑Agent‑Behavior pipeline to produce a deterministic BehaviorPlan.

---

## Input (WLMGraph)

```json
{
  "nodes": [
    {"id": 1, "class": "Ball", "state": "moving"},
    {"id": 2, "class": "Cup", "state": "stationary"}
  ],
  "relations": [
    {"type": "toward", "source": 1, "target": 2}
  ],
  "dimensions": {
    "spatial": {},
    "temporal": {},
    "physical": {},
    "causal": {}
  },
  "closures": [
    {"type": "future_relation", "relation": "toward", "source": 1, "target": 2}
  ]
}
```

---

## Code

```python
from wlm_agent_behavior import compute_behavior

with open("wlmgraph.json") as f:
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

As the engine evolves, this example will produce:

- prepare_for_contact(Ball, Cup)  
- reposition(Cup)  
- stabilize_environment()  

This file will evolve as behavior semantics are implemented.
