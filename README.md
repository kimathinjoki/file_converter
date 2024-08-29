# JSON to CSV Converter

This script converts JSON Lines files to CSV format. It allows you to specify which keys (columns) to include in the CSV file. If no keys are specified, it includes all keys from the JSON objects.

## Features

- Convert JSON Lines files to CSV format.
- Optionally specify which keys to include as columns in the CSV file.
- Automatically handles duplicate filenames by appending a number to the filename.

## Requirements

- Python 3.x

## Usage

### Convert JSON Lines to CSV

To convert a JSON Lines file to CSV, use the `json_to_csv` function. You can specify the keys to include as columns. If no keys are specified, all keys from the JSON objects will be included.

### Print JSON Keys

To print all unique keys from a JSON Lines file, use the `print_json_keys` function.

## Example

To convert a JSON Lines file to CSV and include specific keys as columns:

```python
json_to_csv('./toBeConverted/file.jsonl', ['key_1', 'key2', 'Key3', 'key4'])
```

To print all unique keys from a JSON Lines file:

```python
print_json_keys('../toBeConverted/example.jsonl')
```
## Directory
```
.
├── jsonCsv.py
├── converted_files
│   └── (CSV files will be saved here)
└── toBeConverted
    └── (Place your JSON Lines files here)
```

## Notes
 - Ensure that the `converted_files` directory exists or will be created by the script.
 - The script handles duplicate filenames by appending a number to the filename to make it unique.

## Author 
This repository is mainatined by:

- [Kimathi Njoki](https://github.com/kimathinjoki)

## License
This project is licensed under the MIT License.
