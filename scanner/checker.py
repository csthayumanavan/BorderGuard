from __future__ import annotations

from typing import Any, Dict, List


def check_country(flow: Dict[str, Any], rules: Dict[str, Any]) -> List[str]:
    destination = (flow.get("destination") or "").strip().lower()
    data_type = (flow.get("data_type") or "").strip().lower()
    blocked_regions = set((rules.get("blocked_regions") or []))
    restricted = rules.get("restricted_data_types", {}).get(data_type, {})

    issues: List[str] = []
    if destination in blocked_regions:
        issues.append(f"Destination {destination} is blocked by policy.")

    if data_type in rules.get("restricted_data_types", {}) and destination != restricted.get("region_restriction"):
        issues.append(
            f"Data type '{data_type}' is restricted to '{restricted.get('region_restriction')}' but is being sent to '{destination}'."
        )

    return issues


def check_processor(flow: Dict[str, Any], rules: Dict[str, Any]) -> List[str]:
    processor = (flow.get("processor") or "").strip().lower()
    processor_rules = rules.get("processor_rules", {})
    issues: List[str] = []

    processor_info = processor_rules.get(processor)
    if processor_info and processor_info.get("approved") is False:
        issues.append(f"Processor '{processor}' is not approved.")

    return issues


def check_encryption(flow: Dict[str, Any], rules: Dict[str, Any]) -> List[str]:
    data_type = (flow.get("data_type") or "").strip().lower()
    encrypted = bool(flow.get("encrypted", False))
    restricted = rules.get("restricted_data_types", {}).get(data_type, {})
    issues: List[str] = []

    if restricted.get("require_encryption") and not encrypted:
        issues.append(f"Data type '{data_type}' requires encryption before transfer.")

    return issues


def evaluate_flow(flow: Dict[str, Any], rules: Dict[str, Any]) -> Dict[str, Any]:
    issues = []
    issues.extend(check_country(flow, rules))
    issues.extend(check_processor(flow, rules))
    issues.extend(check_encryption(flow, rules))

    allowed_country = (flow.get("destination") or "").strip().lower()
    country_policy = rules.get("allowed_countries", {}).get(allowed_country)
    if country_policy:
        allowed_destinations = set(country_policy.get("allowed_destinations", []))
        if allowed_country not in allowed_destinations:
            issues.append(f"Destination '{allowed_country}' is not allowed for policy compliance.")

    return {
        "source": flow.get("source"),
        "destination": flow.get("destination"),
        "data_type": flow.get("data_type"),
        "processor": flow.get("processor"),
        "encrypted": flow.get("encrypted"),
        "status": "ALERT" if issues else "SAFE",
        "issues": issues,
    }
