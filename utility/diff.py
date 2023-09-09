# Function to read IP addresses from a file and return a set of IPs
def read_ips_from_file(file_path):
    ips = set()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                ips.add(line)
    return ips

# Function to find IPs that are not present in both sets
def find_ips_not_in_both(file1_ips, file2_ips):
    ips_not_in_both = file1_ips.symmetric_difference(file2_ips)
    return ips_not_in_both

# Main function
if __name__ == "__main__":
    file1_path = "C:\\Users\\marco\\Downloads\\file1.txt"  # Replace with the path to your first file
    file2_path = "C:\\Users\\marco\\Downloads\\file2.txt"  # Replace with the path to your second file

    # Read IP addresses from both files
    file1_ips = read_ips_from_file(file1_path)
    file2_ips = read_ips_from_file(file2_path)

    # Find IPs that are not present in both files
    ips_not_in_both = find_ips_not_in_both(file1_ips, file2_ips)

    # Print the results
    print("IP addresses not present in both files:")
    for ip in ips_not_in_both:
        print(ip)
