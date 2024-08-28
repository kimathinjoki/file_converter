import json
import csv
import os



import json
import csv
import os

# Function to convert JSON to CSV with selected keys
def json_to_csv(json_file, selected_keys):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Generate CSV file name and save in 'converted_files' folder
    base_name = os.path.basename(json_file)
    name_without_ext = os.path.splitext(base_name)[0]
    csv_file = os.path.join('converted_files', f"{name_without_ext}Csv.csv")
    
    # Ensure the 'converted_files' directory exists
    os.makedirs('converted_files', exist_ok=True)
    
    # Check if the file already exists and append a number if necessary
    if os.path.exists(csv_file):
        counter = 2
        while os.path.exists(os.path.join('converted_files', f"{name_without_ext}Csv{counter}.csv")):
            counter += 1
        csv_file = os.path.join('converted_files', f"{name_without_ext}Csv{counter}.csv")
    
    with open(csv_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(selected_keys)
        
        for row in data:
            csv_writer.writerow([row.get(key, '') for key in selected_keys])

# Example usage
json_to_csv('filename.json', ['key1', 'key2', 'key3'])
    
# Function to convert CSV to JSON
def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as file:
        data = csv.DictReader(file)
        file.close()
    with open(json_file, 'w') as file:
        json_file = json.dumps(list(data), indent=4)
        file.write(json_file)
        file.close()
        return json_file
    