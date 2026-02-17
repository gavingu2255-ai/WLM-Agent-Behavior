# tests/test_tension_resolver.py
import pytest
from wlm_agent_behavior.tension_resolver import resolve_tensions


def test_resolve_tensions_empty():
    graph = {"nodes": []}
    policy = {"strategy": "noop", "parameters": {}}

    tensions = resolve_tensions(graph, policy)

    assert isinstance(tensions, list)
    assert tensions == []
