# tests/test_closure_planner.py
import pytest
from wlm_agent_behavior.closure_planner import plan_with_closures


def test_plan_with_closures_structure():
    graph = {"nodes": []}
    policy = {"strategy": "noop", "parameters": {}}
    tensions = []

    plan = plan_with_closures(graph, policy, tensions)

    assert isinstance(plan, dict)
    assert "actions" in plan
    assert isinstance(plan["actions"], list)
