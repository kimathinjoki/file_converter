import os
import json
import csv

# Function to convert JSON to CSV
def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        file.close()
    with open(csv_file, 'w') as file:
        csv_file = csv.writer(file)
        csv_file.writerow(data[0].keys())
        for row in data:
            csv_file.writerow(row.values())
        file.close()
        return csv_file
    
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
    