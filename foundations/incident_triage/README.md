# Incident Triage

This mini-project provides a Python script to triage incident logs, extract transaction details, and summarize failed transactions for further analysis.

## How to Use

1. Place your log file (e.g., `incident_logs.txt`) in this directory.
2. Run `triage_script.py` with Python 3.7 or higher:
   ```
   python triage_script.py
   ```
3. The script will process the log file and output a list of failed transactions with relevant details.

## Features

- Parses log files for transaction and failure information
- Extracts transaction IDs and types from INFO entries
- Associates failure reasons with corresponding transactions
- Handles JSON-formatted error details
- Reports missing files or JSON decode errors

## Example Log Entry

```
INFO: Transaction '12345' 'PAYMENT'
FAILED: '12345': {"error_code": "ERR001", "message": "Insufficient funds"}
```

## Requirements

- Python 3.7 or higher

## Customization

Modify `triage_script.py` to support additional log formats or to extend the incident analysis logic as needed for