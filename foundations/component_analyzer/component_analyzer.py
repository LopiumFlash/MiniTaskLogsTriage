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
    # This regex uses named groups (?P<name>...) to make the code more readable.
    # It looks for a line containing 'WARNING' or 'ERROR' and captures the text
    # after 'Component:' into a group named 'component'.
    log_pattern = re.compile(
        r".* - (?P<log_level>WARNING|ERROR) - Component:\s*(?P<component>.*?)\s*Message:.*"
    )
    
    # The .search() method scans the string for a match to the pattern.
    match = log_pattern.search(log_entry_string)
    
    # If a match is found, we extract the 'component' group and return it.
    # This demonstrates the function's return flow.    
    if match:
        return match.group('component')

    # If no match is found, the function returns None as specified.
    return None

def analyze_compenent_errors(file_path):
    """
    Analyzes the logs and counts occurrences of each component in error logs.
    
    Args:
        file_path (str): The path to the logs file.
    Returns:
        dict: A dictionary with component names as keys and their error counts as values.
    """

    # A list to hold all the component names extracted from the log file.
    # This will be used later by the Counter.
    extracted_components = []
    
    # Using a try-except block to handle potential issues with file operations.
    # The 'with open(...)' statement ensures the file is automatically closed.    
    try:
        with open(file_path, 'r') as file:
            # We iterate through each line of the file, which is an efficient way
            # to process large files without loading the entire file into memory.
            for line in file:
                cleaned_line = line.strip() # This removes leading/trailing whitespace.
                
                # Call the helper function to get the component name from the current line.
                component = extract_error_component(line)
                
                # The 'if component:' check filters out lines that don't have a WARNING/ERROR
                # or don't match the regex pattern (since extract_error_component returns None).
                # This is a key part of the function call/return flow.                
                if component:
                    extracted_components.append(component)
            
            # Using collections.Counter to get a dictionary of component counts.
            # This is an example of dictionary manipulation by creating a new one with counts.           
            return collections.Counter(extracted_components)
    except FileNotFoundError:
        # Gracefully handle the error if the specified file doesn't exist.
        print(f"Error: The file {file_path} does not exist.")
        return {} # Return an empty dictionary to avoid further errors.
    except Exception as e:
        # Catch any other unexpected errors during file processing.
        print(f"An error occurred while reading the file: {e}")
        return {} # Return an empty dictionary.

if __name__ == "__main__":
    # This conditional block ensures this code only runs when the script is executed directly.
    # It will not run if the script is imported as a module into another program.
    
    # The 'r' before the string creates a raw string literal, which is good practice for file paths
    # as it prevents backslashes from being interpreted as escape characters.
    counts = analyze_compenent_errors(r'C:\Users\matth\PythonProjects\DSEPythonEssentials\foundations\component_analyzer\sample_logs.txt')
    print("Component Error Counts:")
    print(counts)