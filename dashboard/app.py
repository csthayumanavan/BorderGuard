from __future__ import annotations

import json
from pathlib import Path

import streamlit as st

from scanner.config import load_rules
from scanner.checker import evaluate_flow


ROOT_DIR = Path(__file__).resolve().parents[1]
FLOW_PATH = ROOT_DIR / "sample_data" / "sample_flows.json"


st.set_page_config(page_title="BorderGuard Dashboard", layout="wide")
st.title("BorderGuard Dashboard")
st.caption("Cross-Border Data Residency Violation Auditor")

with open(FLOW_PATH, "r", encoding="utf-8") as file:
    flows = json.load(file)

rules = load_rules(ROOT_DIR / "rules" / "data_residency_rules.yaml")
processed = [evaluate_flow(flow, rules) for flow in flows]

safe_count = sum(1 for item in processed if item["status"] == "SAFE")
alert_count = sum(1 for item in processed if item["status"] == "ALERT")

col1, col2 = st.columns(2)
col1.metric("Safe Transfers", safe_count)
col2.metric("Flagged Violations", alert_count)

for item in processed:
    status = item["status"]
    with st.container():
        st.markdown(f"### {item['source']} -> {item['destination']}  |  {status}")
        st.write(f"Data Type: {item['data_type']}")
        st.write(f"Processor: {item['processor']}")
        st.write(f"Encrypted: {item['encrypted']}")

        if item["issues"]:
            st.warning("Violations:")
            for issue in item["issues"]:
                st.write(f"- {issue}")
        else:
            st.success("No policy violations detected.")

        st.markdown("---")
