# Behavior Rules — WLM‑Agent‑Behavior  
**How WLM structural dimensions generate agent behavior**

This document defines the rules that convert WLM structural primitives  
(nodes, relations, tensions, closures, dimensions) into **agent actions**.

The rules are deterministic, dimension‑aligned, and model‑agnostic.

---

# 1. Policy Rules

The policy engine selects a high‑level strategy.

MVP strategy:

```
strategy: noop
parameters: {}
```

Future strategies:

- goal‑directed  
- tension‑minimizing  
- closure‑anticipatory  
- multi‑agent consensus  
- environment‑stabilizing  

---

# 2. Tension Resolution Rules

Tensions represent **structural pressure** that must be resolved.

### 2.1 Contact tension
```
tension: contact(A, B) → action: disengage(A, B)
```

### 2.2 Instability
```
state: unstable → action: stabilize(node)
```

### 2.3 Causal preconditions
```
missing_precondition(X) → action: satisfy_precondition(X)
```

---

# 3. Closure‑Aware Planning Rules

Closures represent **future structural states**.

### 3.1 Predicted collision
```
future_tension(contact(A, B)) → action: avoid_future_collision(A, B)
```

### 3.2 Predicted interaction
```
future_relation(toward(A, B)) → action: prepare_for_contact(A, B)
```

### 3.3 Predicted instability
```
future_state(unstable) → action: pre_stabilize(node)
```

---

# 4. Dimension‑Aligned Behavior Rules

### 4.1 Spatial dimension
```
relation: toward(A, B) → action: move_to(B)
relation: away_from(A, B) → action: maintain_distance(B)
```

### 4.2 Temporal dimension
```
closure: expires_soon(X) → action: prioritize(X)
```

### 4.3 Physical dimension
```
force > threshold → action: counter_force(node)
```

### 4.4 Causal dimension
```
affordance: graspable → action: pick_up(node)
affordance: pushable → action: push(node)
```

---

# 5. BehaviorPlan Structure

A BehaviorPlan contains:

```
{
  actions: [...],
  policy: {...},
  tensions_resolved: [...],
}
```

Actions are explicit, deterministic, and ordered.

---

# 6. Determinism

All behavior rules must be:

- deterministic  
- reproducible  
- dimension‑aligned  
- tension‑aware  
- closure‑aware  

Same WLMGraph → same BehaviorPlan.

---

# 7. Future Extensions

- multi‑agent behavior fusion  
- real‑time structural policy engine  
- hierarchical behavior trees  
- structural reinforcement learning  
- embodied robotics integration  
