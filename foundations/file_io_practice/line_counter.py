def count_active_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        active_lines = [line for line in lines if line.strip() and not line.startswith('#')]
        return len(active_lines)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        active_lines = []
        print('Log analysis cannot proceed without the log file.')
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        active_lines = []


if __name__ == "__main__":
    log_file = r'C:\Users\matth\PythonProjects\DSEPythonEssentials\foundations\file_io_practice\sample_logs.txt'
    try:
        active_lines = count_active_lines(log_file)
        print(f"The file '{log_file}' contains {active_lines} active lines.")
    except FileNotFoundError:
        print(f"Error: The file '{log_file}' was not found.")