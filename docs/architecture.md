# BorderGuard Architecture

BorderGuard is structured as a lightweight compliance engine for detecting cross-border data residency violations.

## 1. Rules Layer
The rules layer stores legal and policy conditions in YAML files. These include:
- allowed countries for data storage,
- approved processors,
- restricted data types,
- encryption requirements,
- blocked destinations.

## 2. Scanner Layer
The scanner reads each data flow and validates it against the configured compliance logic.
It checks:
- destination country,
- processor approval status,
- encryption requirement,
- blocklist and restricted data rules.

## 3. Dashboard Layer
The dashboard visualizes the results and flags problematic transfers. It provides an easy way for teams to inspect:
- violations,
- affected data type,
- destination,
- processor status,
- recommended fixes.

## 4. Sample Data Layer
Sample JSON files are included to simulate real transfer events and validate the rule engine during testing.

## Outcome
BorderGuard helps detect compliance risks before sensitive data leaves an approved jurisdiction.
