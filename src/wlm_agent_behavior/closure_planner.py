"""
closure_planner.py — Plan behavior with respect to closures (future states).

MVP behavior:
    - Returns an empty BehaviorPlan skeleton.
"""


def plan_with_closures(wlm_graph, policy, tensions_resolved):
    """
    Plan behavior based on WLMGraph, policy, and resolved tensions.

    Parameters
    ----------
    wlm_graph : dict
        WLMGraph-like structure.
    policy : dict
        Policy structure.
    tensions_resolved : list
        List of resolved tensions.

    Returns
    -------
    dict
        BehaviorPlan-like structure (MVP: empty actions list).
    """
    # MVP: no real planning yet.
    return {
        "actions": [],
    }
