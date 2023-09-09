import json
import pandas as pd

# Load the IP addresses from the JSON file
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\IPs\\ips.json', 'r') as json_file:
    ips_data = json.load(json_file)

# Create a list to store the results
results = []

# Load the CSV file
merged_df = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\merged.csv')

# Iterate through each IP address in the JSON file
for ip_address in ips_data:
    # Check if the IP address exists in the merged CSV
    ip_row = merged_df[merged_df['ip'] == ip_address]
    
    if not ip_row.empty:
        # If the IP is found, extract the information
        actor = ip_row.iloc[0]['actor']
        organization = ip_row.iloc[0]['organization']
        classification = ip_row.iloc[0]['classification']
    else:
        # If the IP is not found, set values to 'Unknown'
        actor = 'Unknown'
        organization = 'unknown'
        classification = 'unknown'
    
    # Append the results to the list
    results.append({'ip': ip_address, 'actor': actor, 'organization': organization, 'classification': classification})

# Create a DataFrame from the results list
results_df = pd.DataFrame(results)

# Save the results to a new CSV file
results_df.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\output.csv', index=False)
