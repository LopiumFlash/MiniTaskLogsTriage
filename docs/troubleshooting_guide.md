# Troubleshooting Guide

## Common Issues

- **Python not found:**  
  Ensure Python 3.7 or higher is installed and available in your system PATH. You can check your Python version by running `python --version` in your terminal.

- **Module not found:**  
  If you see an error about a missing module, install required dependencies using:
  ```
  pip install -r requirements.txt
  ```
  If a `requirements.txt` file is not provided, manually install the needed modules (e.g., `configparser`, `flake8`).

- **Permission errors:**  
  If you encounter permission issues, try running your terminal or IDE as an administrator.

- **Script not running as expected:**  
  Double-check that you are in the correct directory and using the right Python interpreter. Use absolute or relative paths as needed.

## Getting Help

- Check the `README.md` in each mini-project for specific usage instructions.
- Carefully review error messages for clues about what went wrong.
- Search online for error messages or consult the [Python documentation](https://docs.python.org/3/).
- If using Visual Studio Code, ensure your workspace settings are correct and the Python extension is