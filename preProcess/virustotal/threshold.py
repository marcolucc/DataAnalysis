import pandas as pd
import json
import matplotlib.pyplot as plt

greynoise_data = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\output.csv')
virustotal_data = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\virustotal\\report.csv')

malicious_greynoise = greynoise_data[greynoise_data['classification'] == 'malicious']

# Merge the data from GreyNoise and VirusTotal on IP address
merged_data = malicious_greynoise.merge(virustotal_data, left_on='ip', right_on='IP', how='inner')

mean_harmless = merged_data['Harmless'].mean()
std_harmless = merged_data['Harmless'].std()

mean_malicious = merged_data['Malicious'].mean()
std_malicious = merged_data['Malicious'].std()

mean_suspicious = merged_data['Suspicious'].mean()
std_suspicious = merged_data['Suspicious'].std()

# threshold values

threshold_harmless = mean_harmless +  std_harmless
threshold_malicious = mean_malicious +  std_malicious
threshold_suspicious = mean_suspicious +  std_suspicious

print("Thresholds:")
print(f"Harmless: {threshold_harmless}")
print(f"Malicious: {threshold_malicious}")
print(f"Suspicious: {threshold_suspicious}")


unknown_greynoise = greynoise_data[greynoise_data['classification'] == 'Unknown']

# Merge the data from GreyNoise and VirusTotal on IP address
merged_data = unknown_greynoise.merge(virustotal_data, left_on='ip', right_on='IP', how='inner')

# Initialize lists to store the classification results
unknown_ips = []
classification_results = []

# Function to classify IP based on thresholds
def classify_ip(row):
    if row['Malicious'] > threshold_malicious:
        print("Malicious IP found {}".format(row['ip']))
        return 'Malicious'
    elif row['Harmless'] > threshold_harmless:
        print("Benign IP found {}".format(row['ip']))
        return 'Benign'
    elif row['Suspicious'] > threshold_suspicious:
        print("Suspicious IP found {}".format(row['ip']))
        return 'Suspicious'
    else:
        return 'unknown'  # If it doesn't meet any threshold

count = 0
# Iterate through the unknown IP addresses
for index, row in merged_data.iterrows():
    count += 1
    ip = row['ip']  # Assuming 'ip' is the column in greynoise_data containing IP addresses
    result = classify_ip(row)
    unknown_ips.append(ip)
    classification_results.append(result)
    #print(f"Classified {count} of {len(merged_data)} IP addresses")

# Create a new DataFrame to store the classification results
unknown_classification = pd.DataFrame({'IP': unknown_ips, 'Classification': classification_results})



# Count the occurrences of each classification
classification_counts = unknown_classification['Classification'].value_counts()

# Create a bar plot (histogram) for the classifications
plt.figure(figsize=(8, 6))
classification_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of IP Classifications')
plt.xlabel('Classification')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()


# Save the results to a CSV file
unknown_classification.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\virustotal\\unknown_classification.csv', index=False)

num_total_ips = len(greynoise_data)
print(f"Number of Total IP Addresses: {num_total_ips}")

num_unknown_ips = len(unknown_classification)
print(f"Number of Unknown IP Addresses Classified: {num_unknown_ips}")

num_malicious_ips = (greynoise_data['classification'] == 'malicious').sum()
print(f"Number of Malicious IP Addresses Classified: {num_malicious_ips}")

num_benign_ips = (greynoise_data['classification'] == 'benign').sum()
print(f"Number of Benign IP Addresses Classified: {num_benign_ips}")

num_unkn_ip = (greynoise_data['classification'] == 'unknown').sum()
print(f"Number of unknown IP Addresses Classified: {num_unkn_ip}")

num_not_classified_ips = (greynoise_data['classification'] == 'Unknown').sum()
print(f"Number of not classified (Unknown) IP Addresses Classified: {num_not_classified_ips}")



