#main.py

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
    Extracts the log level from a log entry string.
    
    Args:
        log_entry_string (str): The log entry string.
        
    Returns:
        str: The extracted log level.
    """
    # Split the log entry by spaces and extract the second last part
    parts = log_entry_string.split(" - ")
    if len(parts) < 3:
        return None  # Not a valid log entry
    return parts[-2].strip()

log_level_counts = {}
for log in simple_logs:
    log_level = extract_log_level(log)
    if log_level:
        if log_level != 'DEBUG':
            if log_level in log_level_counts:
                log_level_counts[log_level] += 1
            else:
                log_level_counts[log_level] = 1
    else:
        print("Invalid log entry format.")

print(log_level_counts)