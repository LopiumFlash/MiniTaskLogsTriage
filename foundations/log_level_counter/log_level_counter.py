# This script processes a list of log entries and counts the occurrences of each log level,
# excluding 'DEBUG' log entries. It prints the counts of each log level found in the logs.
# It also includes a function to extract the log level from a log entry string.

from collections import Counter
import re

simple_logs = [
    "2025-07-29 10:00:01 - INFO - Application started successfully.",
    "2025-07-29 10:00:05 - ERROR - Database connection failed.",
    "2025-07-29 10:00:10 - INFO - User 'Matthew' accessed dashboard.",
    "2025-07-29 10:00:15 - WARNING - API endpoint /v1/data returned slow response.",
    "2025-07-29 10:00:20 - ERROR - File 'config.json' not found.",
    "2025-07-29 10:00:25 - INFO - Report generation complete.",
    "2025-07-29 10:00:30 - CRITICAL - System meltdown imminent. Core services stopped.",
    "2025-07-29 10:00:35 - WARNING - Outgoing email queue is building up.",
    "2025-07-29 10:00:40 - DEBUG - Detailed variable dump for debugging purposes."
]

def extract_log_level(log_entry_string):
    """
    Extracts the log level from a log entry string using regex.
    
    Args:
        log_entry_string (str): The log entry string.
    Returns:
        str: The extracted log level, or None if not found.
    """
    match = re.search(r" - (INFO|WARNING|ERROR|CRITICAL|DEBUG) - ", log_entry_string)
    if match:
        return match.group(1)
    return None

def analyze_logs_pythonic(logs):
    """
    Analyzes the logs and counts occurrences of each log level, excluding 'DEBUG'.
    
    Args:
        logs (list): List of log entry strings.
    Returns:
        dict: A dictionary with log levels as keys and their counts as values.
    """
    extracted_levels = [
        extract_log_level(log)
        for log in logs
        if extract_log_level(log) is not None and extract_log_level(log) != 'DEBUG'
    ]
    log_level_counts = Counter(extracted_levels)
    return log_level_counts

if __name__ == "__main__":
    counts = analyze_logs_pythonic(simple_logs)
    log_level_counts = analyze_logs_pythonic(simple_logs)
    print("Log Level Counts (excluding 'DEBUG'):")
    print(counts)