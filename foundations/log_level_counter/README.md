# Log Level Identifier & Counter

This script processes a list of log entries, extracts the log level from each entry, and counts the number of entries for each log level (INFO, WARNING, ERROR, CRITICAL).

## How to Use

1. Add your log entries to `log_level_counter.py` or modify the script to read from a file.
2. Run the script with Python 3.7 or higher:
   ```
   python log_level_counter.py
   ```
3. The script will output the count for each log level.

## Example Input

```
INFO: System started
WARNING: Low disk space
ERROR: Failed to load module
CRITICAL: System crash
```

## Example Output

```
INFO: 1
WARNING: 1
ERROR: 1
CRITICAL: 1
```

## Requirements

- Python 3.7 or higher

## Customization

Modify `log_level_counter.py` to support additional log formats or log levels as needed for your use