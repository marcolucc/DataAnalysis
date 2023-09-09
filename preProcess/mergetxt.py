import os

# Define the folder path containing the txt files
folder_path = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\cyberhunt\\dati\\ipsingoliOK\\'

# Define the output file path where you want to write the merged content
output_file_path = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\cyberhunt\\dati\\merged.txt'

# Initialize an empty string to store the merged content
merged_content = ''

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        # Read the content of the file and append it to the merged content
        with open(os.path.join(folder_path, filename), 'r') as f:
            merged_content += f.read()

# Write the merged content to the output file
with open(output_file_path, 'w') as f:
    f.write(merged_content)