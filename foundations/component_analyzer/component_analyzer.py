import re
from collections import Counter

application_errors = [
    "2025-07-29 11:00:01 - ERROR - Component: UserAuth - Message: Failed to authenticate user 'john.doe'.",
    "2025-07-29 11:00:05 - ERROR - Component: DatabaseService - Message: Connection pool exhausted.",
    "2025-07-29 11:00:10 - WARNING - Component: ReportingEngine - Message: Report generation took longer than 5 seconds.",
    "2025-07-29 11:00:15 - ERROR - Component: UserAuth - Message: Invalid token provided for session.",
    "2025-07-29 11:00:20 - ERROR - Component: PaymentGateway - Message: Third-party API timeout.",
    "2025-07-29 11:00:25 - INFO - Component: UserAuth - Message: User 'jane.smith' logged in.", # Not an error
    "2025-07-29 11:00:30 - ERROR - Component: DatabaseService - Message: Query execution failed for 'orders' table.",
    "2025-07-29 11:00:35 - ERROR - Component: PaymentGateway - Message: Payment processing failed due to insufficient funds.",
    "2025-07-29 11:00:40 - DEBUG - Component: MonitoringAgent - Message: Collecting system metrics." # Not an error
]

def extract_error_component(log_entry_string):
    """
    Extracts the component name from an error log entry string using regex,
    but only if the log level is 'WARNING' or 'ERROR'.
    
    Args:
        log_entry_string (str): The error log entry string.
    Returns:
        str: The extracted component name (e.g., "UserAuth"),
             or None if the log level is not WARNING/ERROR,
             or if the component name pattern is not found.
             """
    log_pattern = re.compile(
        r".* - (?P<log_level>WARNING|ERROR) - Component:\s*(?P<component>.*?)\s*Message:.*"
    )
    match = log_pattern.search(log_entry_string)
    if match:
        return match.group('component')
    return None

def analyze_compenent_errors(logs):
    """
    Analyzes the logs and counts occurrences of each component in error logs.
    
    Args:
        logs (list): List of log entry strings.
    Returns:
        dict: A dictionary with component names as keys and their error counts as values.
    """
    extracted_components = [
        extract_error_component(log)
        for log in logs
        if extract_error_component(log) is not None
    ]
    component_counts = Counter(extracted_components)
    return component_counts



if __name__ == "__main__":
    counts = analyze_compenent_errors(application_errors)
    print("Component Error Counts:")
    print(counts)