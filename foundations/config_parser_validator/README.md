# Config File Parser & Validator

This mini-project provides a Python script to parse and validate configuration files in INI format. It ensures that required sections and keys are present and that values are valid for your application.

## How to Use

1. Edit `app_config.ini` with your desired configuration settings.
2. Run `config_analyzer.py` using Python 3.7 or higher:
   ```
   python config_analyzer.py
   ```
3. The script will read and validate the configuration, reporting any missing or invalid entries.

## Features

- Reads INI configuration files using Python's `configparser` module.
- Validates the presence of required sections and keys.
- Reports missing or invalid configuration entries.

## Example `app_config.ini`

```
[DEFAULT]
log_level = INFO
output_dir = ./logs

[database]
host = localhost
port = 5432
user = user
password = pass
```

## Requirements

- Python 3.7 or higher

## Customization

Modify `config_analyzer.py` to add or change validation rules as