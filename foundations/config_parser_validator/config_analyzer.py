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

def validate_config(config_data, required_settings):
    """
    Validates the configuration data against required settings.
    Args:
        config_data (dict): The configuration data to validate.
        required_settings (list): A list of required settings that must be present in the config data.
    Returns:
        bool: True if all required settings are present, False otherwise.
    """
    for setting in required_settings:
        if setting not in config_data:
            print(f"ERROR: Missing required setting: {setting}")
            return False
        elif 'APIPort' in required_settings:
            try:
                config_data['APIPort'] = int(config_data['APIPort'])
                print('INFO: APIPort is valid.')
            except ValueError:
                print(f"ERROR: APIPort must be an integer, but got {config_data['APIPort']}.")
                return False
        elif 'TimoutSeconds' in required_settings:
            try:
                config_data['TimeoutSeconds'] = int(config_data['TimoutSeconds'])
                print('INFO: TimoutSeconds is valid.')
            except ValueError:
                print(f"ERROR: TimoutSeconds must be an integer, but got {config_data['TimoutSeconds']}.")
                return False
        elif 'Version' in required_settings:
            try:
                config_data['Version'] = float(config_data['Version'])
                print('INFO: Version is valid.')
            except ValueError:
                print(f"ERROR: Version must be a float, but got {config_data['Version']}.")
                return False
        else:
            print('ERROR: No valid settings found.')
            return False
    if 'APIPort' in config_data and 'TimeoutSeconds' and 'Version' in config_data:
        print('INFO: All required settings are present and valid.')
        return True
    
if __name__ == "__main__":
    config_file_path = r'C:\Users\matth\PythonProjects\DSEPythonEssentials\foundations\config_parser_validator\app_config.ini'
    required_app_settings = ['AppName', 'DBHost', 'APIPort', 'MaxConnections']
    print(f"Parsing config file: {config_file_path}")
    app_config = parse_config(config_file_path)
    print("Configuration loaded:")
    print(app_config)

    print("\nValidating configuration:")
    is_valid = validate_config(app_config, required_app_settings)

    if is_valid:
        print("\nConfiguration validation PASSED.")
    else:
        print("\nConfiguration validation FAILED.")

    print("\nFinal (validated) Configuration:")
    print(app_config)