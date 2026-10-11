from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict

import yaml


ROOT_DIR = Path(__file__).resolve().parents[1]
RULES_PATH = ROOT_DIR / "rules" / "data_residency_rules.yaml"


def load_rules(path: str | Path | None = None) -> Dict[str, Any]:
    target = Path(path) if path else RULES_PATH
    with open(target, "r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def get_sample_rules_path() -> Path:
    return ROOT_DIR / "sample_data" / "sample_rules.yaml"
