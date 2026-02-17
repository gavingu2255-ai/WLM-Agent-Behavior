# tests/test_end_to_end.py
import pytest
from wlm_agent_behavior import compute_behavior


def test_end_to_end_pipeline_runs():
    wlm_graph = {
        "nodes": [{"id": 1, "class": "Ball"}],
        "relations": [],
        "dimensions": {
            "spatial": {},
            "temporal": {},
            "physical": {},
            "causal": {},
        },
    }

    behavior = compute_behavior(wlm_graph)

    assert isinstance(behavior, dict)
    assert "actions" in behavior
    assert "policy" in behavior
    assert "tensions_resolved" in behavior
