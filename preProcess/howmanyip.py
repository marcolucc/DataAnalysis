import json

# Path to the JSON file
json_file_path = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\IPs\\ips.json'

# Function to count IP addresses in the JSON file
def count_ip_addresses(file_path):
    try:
        with open(file_path, 'r') as json_file:
            ip_data = json.load(json_file)
            if isinstance(ip_data, list):
                return len(ip_data)
            else:
                return 0  # JSON data is not in the expected format (list)
    except FileNotFoundError:
        return 0  # File not found
    except json.JSONDecodeError:
        return 0  # JSON parsing error

# Count IP addresses in the JSON file
count = count_ip_addresses(json_file_path)

if count > 0:
    print(f'The JSON file contains {count} IP addresses.')
else:
    print('No IP addresses found in the JSON file or there was an issue with the file.')

