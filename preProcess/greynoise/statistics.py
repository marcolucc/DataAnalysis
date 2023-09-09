import csv

# Open the output CSV file
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\output.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Initialize counters and dictionaries
    num_ips = 0
    num_orgs = 0
    num_actors = 0
    classifications = {}
    actor_counts = {}
    org_counts = {}
    classification_counts = {}

    # Loop over each row in the CSV file
    for row in csv_reader:
        num_ips += 1
        if row['organization']:
            num_orgs += 1
            org = row['organization']
            if org in org_counts:
                org_counts[org] += 1
            else:
                org_counts[org] = 1
        if row['actor']:
            num_actors += 1
            actor = row['actor']
            if actor in actor_counts:
                actor_counts[actor] += 1
            else:
                actor_counts[actor] = 1
        classification = row['classification']
        if classification in classifications:
            classifications[classification] += 1
        else:
            classifications[classification] = 1
        if classification in classification_counts:
            classification_counts[classification] += 1
        else:
            classification_counts[classification] = 1

    # Find the most common actor and organization
    most_common_actor = max(actor_counts, key=actor_counts.get)
    most_common_org = max(org_counts, key=org_counts.get)
    most_common_classification = max(classification_counts, key=classification_counts.get)

    # Print out the statistics
    print(f'Number of unique IPs: {num_ips}')
    print(f'Number of unique organizations: {num_orgs}')
    print(f'Number of unique actors: {num_actors}')
    print(f'Most common actor: {most_common_actor}')
    print(f'Most common organization: {most_common_org}')
    print(f'Most common classification: {most_common_classification}')
    print('Classification counts:')
    for classification, count in classifications.items():
        print(f'{classification}: {count}')
    print('Actor counts:')
    for actor, count in actor_counts.items():
        print(f'{actor}: {count}')
    print('Organization counts:')
    for org, count in org_counts.items():
        print(f'{org}: {count}')