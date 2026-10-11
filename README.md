# BorderGuard

BorderGuard is a cross-border data residency violation auditor designed to detect whether data is flowing, storing, or being processed in locations that violate compliance laws and regional regulations.

It helps organizations identify risky data movement before a violation becomes a legal or financial issue.

## Project Title
Cross-Border Data Residency Violation Auditor

## Problem Statement
The rule is simple: laws such as India's DPDPA, RBI payment data rules, GDPR, and other country-specific data restrictions define where certain kinds of data may be stored and processed.

However, in practice:
- cloud backups may silently move data across borders,
- third-party APIs may process sensitive information overseas,
- data may be stored in unapproved regions without visibility,
- compliance teams often find violations too late.

This creates a serious gap between legal requirements and real-world data movement.

### Example
An Indian fintech app turns on a cloud backup. It silently copies customers' payment data to a server in the USA. The law is broken and nobody is aware until a regulator raises an issue.

## Solution
BorderGuard watches where data actually flows, compares it with the law, and raises an alarm before a violation becomes a penalty.

The system performs pre-transfer checks on:
- countries allowed for data storage,
- approved processors,
- allowed data destinations,
- third-party processing restrictions,
- encryption requirements.

If any check fails, the system flags the issue and suggests a fix.

## Why This Matters
Data residency laws are becoming stricter across the globe. Businesses operating internationally must know:
- where their data is stored,
- where it is being processed,
- which vendor or cloud region is involved,
- whether the transfer is compliant.

BorderGuard turns this into a clear, automated compliance workflow.

## Key Features
- Data flow monitoring
- Country-based location detection
- Compliance rule evaluation
- Data residency violation detection
- Alert generation for policy violations
- Visual dashboard for flow analysis
- Risk mapping by region and destination
- Support for rule-driven governance
- Pre-transfer compliance checks

## Workflow
1. Collect data-flow records from applications, APIs, or backup services.
2. Locate the destination country for each data flow.
3. Compare the flow with the allowed policy rules.
4. Validate the type of data involved.
5. Alert the user if a violation is detected.
6. Suggest corrective action before the transfer is finalized.

## Architecture
BorderGuard follows a rule-based compliance architecture:

- Rules Layer: compliance rules defined in YAML/structured config
- Scanner Layer: evaluates data flows against allowed rules
- Dashboard Layer: visualization and monitoring interface
- Sample Data Layer: test inputs for validation and demonstration

## Repository Structure
```text
BorderGuard/
├── README.md
├── rules/
│   └── data_residency_rules.yaml
├── scanner/
│   ├── __init__.py
│   ├── config.py
│   ├── checker.py
│   └── main.py
├── dashboard/
│   ├── app.py
│   ├── templates/
│   └── static/
├── sample_data/
│   ├── sample_flows.json
│   └── sample_rules.yaml
├── docs/
│   └── architecture.md
└── .gitignore
```

## Technology Stack
- Python
- YAML for policy definitions
- Streamlit for dashboard
- JSON for sample dataset input
- Rule-based validation engine
- Optional: Plotly / Map visualization for geographic insights

## Rules Engine
The project uses configurable rules to determine whether a data transfer is allowed.

Example rule categories:
- Allowed countries
- Blocked regions
- Approved processors
- Encryption required
- Third-party transfer restriction
- Storage location compliance

Example sample rule concept:
```yaml
country_rules:
  india:
    allowed_storage: ["india"]
    blocked_regions: ["us", "eu"]
    required_encryption: true
```

## Dashboard
The dashboard provides a user-friendly interface to:
- monitor data transfer locations,
- view flagged violations,
- inspect which rule failed,
- identify the destination country,
- understand the legal risk before data is moved.

## Getting Started

### Prerequisites
- Python 3.9+
- pip
- Virtual environment (recommended)

### Clone the Repository
```bash
git clone https://github.com/csthayumanavan/BorderGuard.git
cd BorderGuard
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
# or
venv\Scripts\activate       # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Scanner
```bash
python scanner/main.py
```

### Run the Dashboard
```bash
streamlit run dashboard/app.py
```

## Sample Flow Example
```json
{
  "source": "india",
  "destination": "usa",
  "data_type": "payment_data",
  "processor": "cloud_backup_vendor",
  "encrypted": false
}
```

This example would trigger a compliance warning because the destination is not allowed for the given data type.

## Expected Outcome
BorderGuard helps organizations reduce legal exposure by catching compliance issues before sensitive data crosses forbidden borders.

It gives teams a clear answer to:
- Where is data going?
- Is that location allowed?
- Who is processing it?
- Is the transfer compliant?
- Should it be blocked or fixed?

## Team
Team MORPHERS
- Thayumanavan
- Mohit R
- Shanmuga Sundaram
- Pranet Reddy

## Hackathon Context
This project is positioned as a practical compliance and governance solution for data-driven organizations, especially in regulated industries such as:
- fintech,
- banking,
- healthcare,
- cloud operations,
- international business systems.

## Future Enhancements
- Add regional compliance database integration
- Real-time API event streaming
- Automated policy suggestions
- Support for more global data residency regulations
- Map-based visualization for violations
- ML-based anomaly detection for suspicious transfer patterns

## Conclusion
BorderGuard is a proactive data compliance tool that brings legal awareness into the actual movement of data. By detecting cross-border violations before they happen, it helps businesses stay compliant, reduce risk, and protect sensitive information.

---

If you want, I can also generate:
1. a more professional README for judges,
2. a simplified student-friendly README,
3. a GitHub-ready README + project logo banner,
4. a complete project starter structure for the repo files.

I can create the files for the repository next as well.


























































































































































































































































































































































































































































































































































