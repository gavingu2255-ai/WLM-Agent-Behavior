"""
behavior_emitter.py — Emit a deterministic BehaviorPlan structure.

MVP behavior:
    - Wraps the plan, policy, and tensions into a stable dict.
"""


def emit_behavior_plan(plan, policy, tensions_resolved):
    """
    Emit a deterministic BehaviorPlan structure.

    Parameters
    ----------
    plan : dict
        BehaviorPlan-like structure with "actions".
    policy : dict
        Policy structure.
    tensions_resolved : list
        List of resolved tensions.

    Returns
    -------
    dict
        Final BehaviorPlan structure.
    """
    return {
        "actions": list(plan.get("actions", [])),
        "policy": dict(policy),
        "tensions_resolved": list(tensions_resolved),
    }
