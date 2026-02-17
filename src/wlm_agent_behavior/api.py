"""
High‑level API for WLM‑Agent‑Behavior.

This module exposes a single entry point:

    compute_behavior(wlm_graph) -> BehaviorPlan

MVP behavior:
    - Returns an empty but structurally valid BehaviorPlan.
"""

from .policy_engine import evaluate_policy
from .tension_resolver import resolve_tensions
from .closure_planner import plan_with_closures
from .behavior_emitter import emit_behavior_plan


def compute_behavior(wlm_graph):
    """
    Convert a WLM structural graph into a deterministic behavior plan.

    Parameters
    ----------
    wlm_graph : dict
        WLMGraph-like structure produced by WLM‑World‑Model‑Interpreter
        or other WLM structural sources.

    Returns
    -------
    dict
        A BehaviorPlan-like structure, serialized as a dict.
    """
    policy = evaluate_policy(wlm_graph)
    tensions_resolved = resolve_tensions(wlm_graph, policy)
    plan = plan_with_closures(wlm_graph, policy, tensions_resolved)
    return emit_behavior_plan(plan, policy, tensions_resolved)
