# tests/test_behavior_emitter.py
import pytest
from wlm_agent_behavior.behavior_emitter import emit_behavior_plan


def test_emit_behavior_plan_deterministic():
    plan = {"actions": []}
    policy = {"strategy": "noop", "parameters": {}}
    tensions = []

    out1 = emit_behavior_plan(plan, policy, tensions)
    out2 = emit_behavior_plan(plan, policy, tensions)

    assert out1 == out2
    assert "actions" in out1
    assert "policy" in out1
    assert "tensions_resolved" in out1
