import os
import json
import csv
import requests
import time

# Define the base URL and headers for VirusTotal API
base_url = "https://www.virustotal.com/api/v3/ip_addresses/"
headers = {
    "accept": "application/json",
    "x-apikey": ""  # Replace with your VirusTotal API key
}

# Function to get the report for a specific IP address
def get_ip_report(ip):
    url = base_url + ip
    response = requests.get(url, headers=headers)
    return response.json()


# Function to create a CSV report with specific fields
def create_csv_report(ip_list):
    with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\virustotal\\report.csv', 'w', newline='') as csvfile:
        fieldnames = ["IP", "Harmless", "Malicious", "Suspicious", "Timeout", "Undetected"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        count = 0
        ok = 0
        for ip in ip_list:
            sleep_time = 0.1  # Sleep for 0.1 seconds between each request
            count += 1
            ip_report = get_ip_report(ip)
            if 'data' in ip_report:
                ip_data = ip_report['data']
                ip_filename = f"C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\virustotal\\results/{ip}.json"
                with open(ip_filename, 'w') as file:
                    json.dump(ip_data, file, indent=2)
                last_analysis_stats = ip_data.get('attributes', {}).get('last_analysis_stats', {})
                ok += 1
                writer.writerow({
                    "IP": ip,
                    "Harmless": last_analysis_stats.get('harmless', ''),
                    "Malicious": last_analysis_stats.get('malicious', ''),
                    "Suspicious": last_analysis_stats.get('suspicious', ''),
                    "Timeout": last_analysis_stats.get('timeout', ''),
                    "Undetected": last_analysis_stats.get('undetected', '')
                })
                print(f"Report for IP {count} of {len(ip_list)} ({ip}): {ip_filename}")
        print("Report completed. {ok} of {count} IPs found.")

if __name__ == "__main__":
    # Replace this with loading your IP addresses from the JSON file
    #ip_list_from_json = ["8.8.8.8", "8.8.4.4"]  # Example list of IP addresses
    with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\IPs\\ips.json', 'r') as json_file:
        ip_list_from_json = json.load(json_file)
    
    # Create the "results" folder if it doesn't exist
    os.makedirs("results", exist_ok=True)
    
    # Create the CSV report
    create_csv_report(ip_list_from_json)
