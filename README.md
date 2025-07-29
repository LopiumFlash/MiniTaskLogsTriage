# MiniTaskLogsTriage

This project is a simple Python script that processes a list of log entries, extracts the log level from each entry, and counts the number of entries for each log level (INFO, WARNING, ERROR, CRITICAL).

## How to Use
1. Place your log entries in the script or load them from a file.
2. Run the script using your Python environment.
3. The script will output the count of each log level found in the entries.

## Requirements
- Python 3.7 or higher

## Project Structure
- `main.py`: Main script for log processing.
- `.github/copilot-instructions.md`: Copilot custom instructions.

## Example
```
INFO: System started
WARNING: Low disk space
ERROR: Failed to load module
CRITICAL: System crash
```

## Output
```
INFO: 1
WARNING: 1
ERROR: 1
CRITICAL: 1
```
