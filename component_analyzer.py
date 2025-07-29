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
        r".* - (?P<log_level>WARNING|ERROR) - Component:\s*(?P<component>[^-\s]+) - Message:.*"
    )
    match = log_pattern.search(log_entry_string)
    if match:
        return match.group('component')
    return None

component_errors_counts = {}
for log in application_errors:
    component = extract_error_component(log)
    if component:
        if component not in component_errors_counts:
            component_errors_counts[component] = 0
        component_errors_counts[component] += 1
print("Component Error Counts:")
for component, count in component_errors_counts.items():
    print(f"{component}: {count}")  
