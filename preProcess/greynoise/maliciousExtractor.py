import csv
import json

# Define the input CSV file and output JSON file names
input_csv_file = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\output.csv'
output_json_file = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\malicious_ips.json'

# Initialize a list to store the malicious IPs
malicious_ips = []

# Open the CSV file and read its contents
with open(input_csv_file, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Check if the classification is "malicious"
        if row['classification'].strip().lower() == 'malicious':
            # Extract the IP address and add it to the list
            malicious_ips.append(row['ip'].strip())

# Create a dictionary to store the malicious IPs
malicious_ips_dict = {'malicious_ips': malicious_ips}

# Write the malicious IPs to a JSON file
with open(output_json_file, 'w') as json_file:
    json.dump(malicious_ips_dict, json_file, indent=4)

print(f"Malicious IPs have been extracted and saved to {output_json_file}.")
