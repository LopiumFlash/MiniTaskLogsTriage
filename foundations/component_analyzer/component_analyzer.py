import re
from collections import Counter

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

def analyze_compenent_errors(file_path):
    """
    Analyzes the logs and counts occurrences of each component in error logs.
    
    Args:
        file_path (str): The path to the logs file.
    Returns:
        dict: A dictionary with component names as keys and their error counts as values.
    """
    #
    extracted_components = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                cleaned_line = line.strip()
                component = extract_error_component(line)
                if component:
                    extracted_components.append(component)
            return collections.Counter(extracted_components)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return {}
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return {}

if __name__ == "__main__":
    counts = analyze_compenent_errors(r'C:\Users\matth\PythonProjects\DSEPythonEssentials\foundations\component_analyzer\sample_logs.txt')
    print("Component Error Counts:")
    print(counts)