# API Specification — WLM‑Agent‑Behavior  
**Public API surface for converting WLMGraph → BehaviorPlan**

This document defines the official API for WLM‑Agent‑Behavior.  
The API is intentionally minimal, deterministic, and stable.

---

# 1. High‑Level API

The primary entry point is:

```python
compute_behavior(wlm_graph) -> dict
```

### Description
Convert a WLM structural graph into a deterministic behavior plan.

### Signature

```python
def compute_behavior(wlm_graph: dict) -> dict:
    """
    Convert a WLM structural graph into a deterministic BehaviorPlan.
    """
```

### Parameters

| Name | Type | Description |
|------|------|-------------|
| `wlm_graph` | `dict` | WLMGraph-like structure |

### Returns

| Type | Description |
|------|-------------|
| `dict` | BehaviorPlan structure |

---

# 2. Pipeline Stages

```
evaluate_policy     → strategy selection
resolve_tensions    → stability & causal resolution
plan_with_closures  → future-aware planning
emit_behavior_plan  → deterministic output
```

Each stage is modular and testable.

---

# 3. BehaviorPlan Structure

```python
{
  "actions": [],
  "policy": {...},
  "tensions_resolved": []
}
```

Future versions include:

- action parameters  
- multi‑agent coordination  
- temporal sequencing  
- causal precondition satisfaction  

---

# 4. CLI API

The library provides a command‑line interface:

```
wlm-agent-behavior compute-behavior <input>
```

### Usage

```
wlm-agent-behavior compute-behavior graph.json
wlm-agent-behavior compute-behavior '{"nodes": [...]}'
wlm-agent-behavior compute-behavior graph.json --out plan.json
```

---

# 5. Error Handling

- deterministic behavior  
- no silent failures  
- clear error messages  
- no partial plans  

---

# 6. Versioning

Semantic versioning:

- `0.x` — experimental  
- `1.x` — stable behavioral semantics  
- `2.x` — multi‑agent, real‑time behavior  

---

# 7. Summary

The WLM‑Agent‑Behavior API exposes a single stable entry point:

```
compute_behavior(wlm_graph) → BehaviorPlan
```

This enables structured, deterministic, reproducible agent behavior.
