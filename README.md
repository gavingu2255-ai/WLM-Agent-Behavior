# WLM‑Agent‑Behavior  
**Convert WLM structural graphs → stable, controllable, reproducible agent behavior**

The **WLM‑Agent‑Behavior** library is the **behavioral execution layer** of the WLM ecosystem.  
It transforms WLM structural graphs (WLMGraph) into **deterministic agent actions, policies, and plans**.

This is the third major layer of WLM:

1. **SLP‑World‑Interpreter** — Language → Structure  
2. **WLM‑World‑Model‑Interpreter** — World Model → Structure  
3. **WLM‑Agent‑Behavior** — Structure → Behavior ← **this repo**

It provides the missing link between **structured perception** and **structured action**:

> **Structure → Reasoning → Behavior → World**

---

## ✨ Features

### **1. WLMGraph → Agent Actions**
- Convert tensions, closures, and dimensions into actionable behavior  
- Resolve physical/causal tensions  
- Generate movement, manipulation, avoidance, stabilization actions  
- Produce deterministic action sequences

### **2. Dimension‑aligned behavior**
Uses WLM’s four core dimensions:

- **Spatial** → navigation, positioning, approach/avoid  
- **Temporal** → timing, sequencing, persistence  
- **Physical** → stability, force, collision handling  
- **Causal** → affordances, preconditions, effects  

Behavior is **dimension‑consistent** and **structurally grounded**.

### **3. Tension‑driven decision making**
- contact tension → avoid / stabilize / disengage  
- instability tension → correct posture / reposition  
- causal tension → satisfy preconditions  
- temporal tension → act before closure expires  

### **4. Closure‑aware planning**
- predicted collisions → avoidance plans  
- predicted interactions → preparation actions  
- predicted future states → anticipatory behavior  

### **5. Deterministic policy engine**
- No randomness  
- No hidden state  
- Same structure → same behavior  
- Fully reproducible  

### **6. Clean API for agents & simulators**
- One function: `compute_behavior(wlm_graph)`  
- Returns a structured behavior plan

---

## 🚀 Quickstart

### **Install**

```bash
pip install wlm-agent-behavior
```

### **Use**

```python
from wlm_agent_behavior import compute_behavior

behavior = compute_behavior(wlm_graph)
print(behavior)
```

### **Output (MVP)**

```
BehaviorPlan {
  actions: [
  ]
}
```

As the engine evolves, this becomes:

```
BehaviorPlan {
  actions: [
    move_to(Cup),
    pick_up(Cup),
    avoid(Table)
  ]
}
```

---

## 🧠 Why this exists

WLM gives you **structure**, but structure alone does not act.

Agents need:

- stable policies  
- predictable behavior  
- reproducible decisions  
- tension resolution  
- closure‑aware planning  
- dimension‑aligned action semantics  

LLMs cannot do this.  
World models cannot do this.  
SLP cannot do this.  
WLMGraph cannot do this alone.

This library provides the missing layer:

> **Structured perception → Structured behavior**

It enables:

- embodied agents  
- robotics stacks  
- multi‑agent systems  
- simulation control  
- planning engines  
- world‑model‑aligned behavior  

---

## 📦 API

### `compute_behavior(wlm_graph: dict) → dict`

Convert a WLM structural graph into a deterministic behavior plan.

```python
def compute_behavior(wlm_graph: dict) -> dict:
    """
    Convert a WLM structural graph into a deterministic behavior plan.
    Returns a BehaviorPlan dictionary.
    """
```

### BehaviorPlan structure (MVP)

```python
{
  "actions": []
}
```

Future versions include:

```python
{
  "actions": [
    {"type": "move_to", "target": "Cup"},
    {"type": "pick_up", "target": "Cup"},
    {"type": "avoid", "target": "Table"}
  ],
  "policy": {...},
  "tensions_resolved": [...],
  "closures_considered": [...]
}
```

---

## 📘 Examples

### WLMGraph → Behavior

**Input**

```
node Ball { state: moving }
node Cup { state: stationary }
relation: toward(Ball, Cup)
closure: future_relation(toward(Ball, Cup))
```

**Output**

```
BehaviorPlan {
  actions: [
    prepare_for_contact(Ball, Cup),
    reposition(Cup),
    stabilize_environment()
  ]
}
```

---

## 🏗 Repository Structure

```
wlm-agent-behavior/
│
├── README.md
├── pyproject.toml
├── setup.cfg
│
├── src/
│   └── wlm_agent_behavior/
│       ├── __init__.py
│       ├── api.py
│       ├── policy_engine.py
│       ├── tension_resolver.py
│       ├── closure_planner.py
│       ├── dimension_evaluator.py
│       ├── behavior_emitter.py
│       └── cli.py
│
├── examples/
│   ├── wlmgraph_to_behavior.md
│   ├── tension_resolution.md
│   └── closure_planning.md
│
├── tests/
│   ├── test_policy_engine.py
│   ├── test_tension_resolver.py
│   ├── test_closure_planner.py
│   └── test_end_to_end.py
│
└── docs/
    ├── overview.md
    ├── behavior-rules.md
    ├── api.md
    └── roadmap.md
```

---

## 🔗 Relationship to WLM

This library is fully aligned with:

- WLM structural dimensions  
- WLMGraph semantics  
- WLM reasoning engine  
- WLM structural simulator  
- WLM agent frameworks  

It consumes WLMGraph and produces **BehaviorPlan**, which can be executed by:

- embodied agents  
- simulators  
- robotics controllers  
- multi‑agent systems  

---

## 📅 Status

MVP architecture ready.  
Behavioral semantics under development.

Next milestones:

- Tension‑driven action selection  
- Closure‑aware planning  
- Multi‑agent behavior fusion  
- Real‑time structural policy engine  

See `docs/roadmap.md` for details.

---

## 📄 License

MIT License (see `LICENSE`).

---

## 🧩 Summary

The **WLM‑Agent‑Behavior** library is the execution layer of the WLM ecosystem.  
It turns structural understanding into **structural action**.

It enables:

- Agents that act with structure  
- Robots that behave predictably  
- Simulators that run structural policies  
- Multi‑agent systems that coordinate through WLM  

A foundational component of the **WLM behavioral stack**.
