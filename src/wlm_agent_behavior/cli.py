"""
Command-line interface for WLM‑Agent‑Behavior.

Usage:
    wlm-agent-behavior compute-behavior wlmgraph.json
    wlm-agent-behavior compute-behavior '{"nodes": [...]}'
    wlm-agent-behavior compute-behavior wlmgraph.json --out behavior.json
"""

import argparse
import json
import sys
from pathlib import Path

from .api import compute_behavior


def load_input(input_arg: str):
    """
    Load input either from a JSON file or from an inline JSON string.
    """
    path = Path(input_arg)
    if path.exists() and path.is_file():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            raise ValueError(f"File '{input_arg}' is not valid JSON.")
    else:
        try:
            return json.loads(input_arg)
        except json.JSONDecodeError:
            raise ValueError("Input must be a JSON file path or valid JSON string.")


def cmd_compute_behavior(args):
    """
    Handle the `compute-behavior` subcommand.
    """
    try:
        wlm_graph = load_input(args.input)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    behavior = compute_behavior(wlm_graph)

    if args.out:
        Path(args.out).write_text(json.dumps(behavior, indent=2), encoding="utf-8")
    else:
        print(json.dumps(behavior, indent=2))


def main():
    parser = argparse.ArgumentParser(
        prog="wlm-agent-behavior",
        description="WLM‑Agent‑Behavior CLI"
    )

    sub = parser.add_subparsers(dest="command")

    # -------------------------
    # compute-behavior
    # -------------------------
    p_compute = sub.add_parser(
        "compute-behavior",
        help="Compute a behavior plan from a WLM structural graph"
    )
    p_compute.add_argument(
        "input",
        help="JSON file path or inline JSON string"
    )
    p_compute.add_argument(
        "--out",
        help="Write output to file"
    )
    p_compute.set_defaults(func=cmd_compute_behavior)

    # -------------------------
    # Parse and dispatch
    # -------------------------
    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)

    args.func(args)
