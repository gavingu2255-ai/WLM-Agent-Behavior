# Example: Tension Resolution → Behavior

This example demonstrates how structural tensions in a WLMGraph  
are resolved into behavior actions.

---

## Input (WLMGraph with tensions)

```json
{
  "nodes": [
    {"id": 1, "class": "Block"},
    {"id": 2, "class": "Table"}
  ],
  "tensions": [
    {"type": "contact", "a": 1, "b": 2},
    {"type": "instability", "node": 1}
  ],
  "dimensions": {
    "physical": {},
    "spatial": {},
    "temporal": {},
    "causal": {}
  }
}
```

---

## Code

```python
from wlm_agent_behavior import compute_behavior

with open("tension_graph.json") as f:
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

- disengage(Block, Table)  
- stabilize(Block)  

This file will evolve as tension semantics are implemented.
