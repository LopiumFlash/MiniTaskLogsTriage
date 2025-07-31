def parse_config(file_path):
    """
    Parses the configuration file and returns the configuration data.
    
    Args:
        file_path (str): The path to the configuration file.
   
    Returns:
        dict: The parsed configuration data.
    """
    config_data = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line and not cleaned_line.startswith('#'):
                    if '=' in cleaned_line:
                        if cleaned_line.count('=') == 1:                        
                            key, value = cleaned_line.split('=', 1)
                            config_data[key.strip()] = value.strip()
                        else:
                            print(f'File contains invalid format. Multiple "=" found in line: {cleaned_line}. Line skipped.')
                            continue
                    else:
                        print("No active lines found.")
                        continue
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        active_lines = []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        active_lines = []
    return config_data