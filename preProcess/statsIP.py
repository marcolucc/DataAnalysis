import re

# Define the file path of the .txt file
file_path = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\cyberhunt\\dati\\ipsingoliOK\\merged.txt'

# Initialize a dictionary to store the count of each IP address
ip_count = {}

# Open the file and read its contents
with open(file_path, 'r') as f:
    content = f.read()

# Find all IP addresses in the content using regular expressions
ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', content)

# Count the number of unique IP addresses and the occurrence of each IP address
unique_ips = set(ip_addresses)
for ip in unique_ips:
    ip_count[ip] = ip_addresses.count(ip)

# Print the results to the console

print('IP address occurrence count:')
for ip, count in ip_count.items():
    print(f'{ip}: {count}')

# Calculate additional statistics
total_occurrences = sum(ip_count.values())
most_common_ip = max(ip_count, key=ip_count.get)

# Print additional statistics to the console
print(f'Total number of IP address occurrences: {total_occurrences}')
print(f'Most common IP address: {most_common_ip}')
print(f'Total number of unique IP addresses: {len(unique_ips)}')