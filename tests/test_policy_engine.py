# tests/test_policy_engine.py
import pytest
from wlm_agent_behavior.policy_engine import evaluate_policy


def test_evaluate_policy_structure():
    graph = {"nodes": []}
    policy = evaluate_policy(graph)

    assert isinstance(policy, dict)
    assert "strategy" in policy
    assert "parameters" in policy
