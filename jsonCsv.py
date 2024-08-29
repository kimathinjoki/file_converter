import json
import csv
import os

def print_json_keys(json_file):
    keys_set = set()
    
    with open(json_file, 'r') as file:
        for line in file:
            json_obj = json.loads(line)
            keys_set.update(json_obj.keys())
    
    print("Keys that would be columns in the CSV file:")
    for key in keys_set:
        print(key)


def json_to_csv(json_file, selected_keys=None):
    data = []
    with open(json_file, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    
    # use keys from the first JSON object
    if not selected_keys:
        selected_keys = list(data[0].keys())
    
    # Generate CSV file name and save in converted_files folder
    base_name = os.path.basename(json_file)
    name_without_ext = os.path.splitext(base_name)[0]
    csv_file = os.path.join('converted_files', f"{name_without_ext}Csv.csv")
    
    # Ensure the 'converted_files' directory exists
    os.makedirs('converted_files', exist_ok=True)
    
    # Check if the file already exists and append a number
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


# json_to_csv('../toBeConverted/models.jsonl')


# print_json_keys('../toBeConverted/utterances.jsonl')

json_to_csv('../toBeConverted/utterances.jsonl', ['model_name', 'model_provider', 'model_reponse', 'user_prompt', 'if_chosen', 'score', 'conversation_type', 'user_id'])

    