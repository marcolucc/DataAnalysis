import re
import csv
# Path to the TXT file
txt_file_path = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\IPs\\meta11.txt'
txt_file_path1 = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\IPs\\meta12.txt'
txt_file_path2 = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\IPs\\meta21.txt'
txt_file_path3 = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\IPs\\meta22.txt'

file1_path = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\meta11gn_analysis_2023-09-07-1205.csv'
file2_path = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\meta12gn_analysis_2023-09-07-1211.csv'
file3_path = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\meta21gn_analysis_2023-09-07-1214.csv'
file4_path = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\meta22gn_analysis_2023-09-07-1215.csv'

# Function to count IP addresses in a text file
def count_ip_addresses_in_txt(file_path):
    try:
        with open(file_path, 'r') as txt_file:
            content = txt_file.read()
            # Use a regular expression to find IP addresses in the text
            ip_addresses = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', content)
            return len(ip_addresses)
    except FileNotFoundError:
        return 0  # File not found

# Count IP addresses in the TXT file
count = count_ip_addresses_in_txt(txt_file_path)

if count > 0:
    print(f'The TXT file {txt_file_path} contains {count} IP addresses.')
else:
    print('No IP addresses found in the TXT file or there was an issue with the file.')

count = count_ip_addresses_in_txt(txt_file_path1)

if count > 0:
    print(f'The TXT file {txt_file_path1} contains {count} IP addresses.')
else:
    print('No IP addresses found in the TXT file or there was an issue with the file.')

count = count_ip_addresses_in_txt(txt_file_path2)

if count > 0:
    print(f'The TXT file {txt_file_path2} contains {count} IP addresses.')
else:
    print('No IP addresses found in the TXT file or there was an issue with the file.')

count = count_ip_addresses_in_txt(txt_file_path3)

if count > 0:
    print(f'The TXT file {txt_file_path3} contains {count} IP addresses.')
else:
    print('No IP addresses found in the TXT file or there was an issue with the file.')

#Sum all the counts
count = count_ip_addresses_in_txt(txt_file_path) + count_ip_addresses_in_txt(txt_file_path1) + count_ip_addresses_in_txt(txt_file_path2) + count_ip_addresses_in_txt(txt_file_path3)
print(f'The TXT files contain {count} IP addresses.')

print('*'*50)

# Function to count IP addresses in a CSV file
def count_ip_addresses_in_csv(file_path, column_name):
    ip_addresses = []
    with open(file_path, 'r', encoding='utf-8') as csv_file: 
        for line in csv_file:
            # Split the line into columns based on a comma (`,`)
            columns = line.strip().split(',')
            if len(columns) >= 0:
                # Assuming the IP addresses are in a specific column index (adjust as needed)
                ip = columns[column_index]
                # Use a regular expression to find IP addresses in the column
                ip_matches = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', ip)
                ip_addresses.extend(ip_matches)
        return len(ip_addresses)
    

# Count IP addresses in the CSV file
column_index = 0  # Replace with the index of the column containing IP addresses (0-based)
count = count_ip_addresses_in_csv(file1_path, column_index)

if count > 0:
    print(f'The CSV file contains {count} IP addresses in the specified column.')
else:
    print('No IP addresses found in the CSV file or there was an issue with the file.')

count = count_ip_addresses_in_csv(file2_path, column_index)

if count > 0:
    print(f'The CSV file contains {count} IP addresses in the specified column.')
else:
    print('No IP addresses found in the CSV file or there was an issue with the file.')

count = count_ip_addresses_in_csv(file3_path, column_index)

if count > 0:
    print(f'The CSV file contains {count} IP addresses in the specified column.')
else:
    print('No IP addresses found in the CSV file or there was an issue with the file.')

count = count_ip_addresses_in_csv(file4_path, column_index)

if count > 0:
    print(f'The CSV file contains {count} IP addresses in the specified column.')
else:
    print('No IP addresses found in the CSV file or there was an issue with the file.')

#Sum all the counts
count = count_ip_addresses_in_csv(file1_path, column_index) + count_ip_addresses_in_csv(file2_path, column_index) + count_ip_addresses_in_csv(file3_path, column_index) + count_ip_addresses_in_csv(file4_path, column_index)
print(f'The CSV files contain {count} IP addresses in the specified column.')

############################
print('*'*50)
count = count_ip_addresses_in_csv('C:\\Users\\marco\\Downloads\\gn_analysis_2023-09-07-1431.csv', column_index)

if count > 0:
    print(f'The CSV file contains {count} IP addresses in the specified column.')
else:
    print('No IP addresses found in the CSV file or there was an issue with the file.')



count = count_ip_addresses_in_csv('C:\\Users\\marco\\Downloads\\gn_analysis_2023-09-07-1443.csv', column_index)

if count > 0:
    print(f'The CSV file contains {count} IP addresses in the specified column.')
else:
    print('No IP addresses found in the CSV file or there was an issue with the file.')

