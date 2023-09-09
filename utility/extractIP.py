import json

# Define the input JSON file path
input_file_path = r'C:\Users\marco\Documents\GitHub\thesis-images\scripts\cyberhunt\dati\origin\htt.json'

# Define the output file path where you want to write the extracted values
output_file_path = r'C:\Users\marco\Documents\GitHub\thesis-images\scripts\cyberhunt\dati\output2.txt'

# Initialize an empty list to store the extracted values
extracted_values = []

# Read the JSON file
with open(input_file_path, 'r') as json_file:
    data = json.load(json_file)
    
    # Loop through each JSON object in the file
    for item in data:
        # Extract the value of 'id.orig_h' from each object
        orig_h_value = item.get('id.orig_h', 'Unknown')
        
        # Append the extracted value to the list
        extracted_values.append(orig_h_value)

# Print the extracted values to the console
for value in extracted_values:
    print(value)

# Write the extracted values to the output file
with open(output_file_path, 'w') as output_file:
    for value in extracted_values:
        output_file.write(value + '\n')

print(f"Extracted values have been written to {output_file_path}")
