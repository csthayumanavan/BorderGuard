from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from scanner.config import load_rules
from scanner.checker import evaluate_flow


ROOT_DIR = Path(__file__).resolve().parents[1]
SAMPLE_FLOW_PATH = ROOT_DIR / "sample_data" / "sample_flows.json"


def load_sample_flows(path: str | Path | None = None) -> List[Dict[str, Any]]:
    target = Path(path) if path else SAMPLE_FLOW_PATH
    with open(target, "r", encoding="utf-8") as file:
        return json.load(file)


def scan_flows(flow_file: str | Path | None = None, rules_file: str | Path | None = None) -> List[Dict[str, Any]]:
    flow_data = load_sample_flows(flow_file)
    rules = load_rules(rules_file)
    return [evaluate_flow(flow, rules) for flow in flow_data]


def main() -> None:
    results = scan_flows()
    for result in results:
        print(f"{result['source']} -> {result['destination']} | {result['status']}")
        if result["issues"]:
            for issue in result["issues"]:
                print(f"  - {issue}")


if __name__ == "__main__":
    main()
