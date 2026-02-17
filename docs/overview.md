# WLM‑Agent‑Behavior — Overview  
**Structure → Behavior → World**

The **WLM‑Agent‑Behavior** library is the behavioral execution layer of the WLM ecosystem.  
It converts WLM structural graphs (WLMGraph) into **deterministic, reproducible, controllable agent behavior**.

This is the third major layer in the WLM stack:

1. **SLP‑World‑Interpreter** — Language → Structure  
2. **WLM‑World‑Model‑Interpreter** — World Model → Structure  
3. **WLM‑Agent‑Behavior** — Structure → Behavior ← *this library*

It provides the missing link between **structured perception** and **structured action**.

---

## Why this exists

WLMGraphs describe:

- entities  
- relations  
- tensions  
- closures  
- spatial/temporal/physical/causal dimensions  

But they do not specify **what an agent should do**.

Agents need:

- stable policies  
- predictable actions  
- tension resolution  
- closure‑aware planning  
- dimension‑aligned behavior  

This library provides that layer.

---

## What this interpreter does

Given a WLMGraph, it produces:

- **actions** (move_to, pick_up, avoid, stabilize, etc.)  
- **policies** (strategy selection, parameters)  
- **tension resolutions** (contact, instability, causal preconditions)  
- **closure‑aware plans** (anticipating future states)  

The output is a deterministic **BehaviorPlan**.

---

## Architecture

The behavior pipeline is clean and modular:

```
WLMGraph
    ↓
Policy Engine (strategy)
    ↓
Tension Resolver (stability)
    ↓
Closure Planner (future-aware)
    ↓
Behavior Emitter (deterministic plan)
```

Each stage is isolated and testable.

---

## Design principles

- **Deterministic** — same structure → same behavior  
- **Interpretable** — explicit actions, policies, resolutions  
- **Modular** — each stage can evolve independently  
- **Dimension‑aligned** — spatial, temporal, physical, causal  
- **Future‑aware** — closures guide planning  
- **Agent‑agnostic** — works with any WLM‑compatible agent  

---

## Status

MVP architecture complete.  
Behavioral semantics under development.

See `docs/roadmap.md` for upcoming milestones.
