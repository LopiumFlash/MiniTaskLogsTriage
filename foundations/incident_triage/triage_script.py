import json

def triage_logs(log_file_path):
    """
    Triage logs from a specified file to identify and categorize incidents.
    
    Args:
        log_file_path (str): The path to the log file to be triaged.

    Returns:
        list: A list of dictionaries, each representing an incident with its details.
    """
    failed_transactions_master = []
    transaction_info = {}
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line and not cleaned_line.startswith('#'):
                    if 'INFO' in line:
                        if 'Transaction' in line:
                            transaction_id = line.split("'")[1].split("'")[0]
                            transaction_type = line.split("'")[2].split("'")[0]
                            transaction_info = {
                                'transaction_id': transaction_id,
                                'transaction_type': transaction_type
                            }
                    elif 'FAILED' in line:
                        failed_transaction_id = cleaned_line.split("'")[1].split("'")[0]
                        failure_reason_json = cleaned_line.split(": ")[1]
                        failure_reason = json.loads(failure_reason_json)
                        error_code = failure_reason['error_code']
                        if transaction_info['transaction_id'] == failed_transaction_id:
                            failure_reason['transaction_type'] = transaction_info['transaction_type']
                            failed_transactions_master.append(failure_reason)
                        else:
                            continue               
    except FileNotFoundError:
        print(f"Error: The log file {log_file_path} does not exist.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in the log file {log_file_path}.")
        return []
    return failed_transactions_master

triage_logs(r'C:\Users\matth\PythonProjects\DSEPythonEssentials\foundations\incident_triage\incident_logs.txt')