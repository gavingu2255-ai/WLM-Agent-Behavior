"""
tension_resolver.py — Resolve tensions present in WLMGraph.

MVP behavior:
    - Returns an empty list of resolved tensions.
"""


def resolve_tensions(wlm_graph, policy):
    """
    Resolve tensions in the WLM structural graph according to the policy.

    Parameters
    ----------
    wlm_graph : dict
        WLMGraph-like structure.
    policy : dict
        Policy structure produced by `evaluate_policy`.

    Returns
    -------
    list
        List of resolved tensions (MVP: empty).
    """
    # MVP: no tension resolution yet.
    return []
