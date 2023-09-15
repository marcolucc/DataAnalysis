import pandas as pd

greynoise_data = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\output.csv')
virustotal_data = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\virustotal\\report.csv')

columns_to_keep_df1 = ['ip', 'classification']  
columns_to_keep_df2 = ['IP', 'Harmless','Malicious','Suspicious']  


merged_df = pd.merge(greynoise_data[columns_to_keep_df1], virustotal_data[columns_to_keep_df2],  left_on='ip', right_on='IP', how='inner')
#print(merged_df)
# Save the merged dataset to a new CSV file if needed
#merged_df.to_csv('merged_dataset.csv', index=False)

merged_df = merged_df.drop(['IP'], axis=1)
#merged_df = merged_df.drop(['ip'], axis=1)
filtered_df = merged_df[~merged_df['classification'].str.contains('Unknown')]
unknown_rows_df = merged_df[merged_df['classification'].str.contains('Unknown')]
print(unknown_rows_df)
print(filtered_df)
filtered_df.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\classificator\\trainDatasetWithIP.csv', index=False)

# Save the rows containing "Unknown" to a different CSV file
print(unknown_rows_df)
unknown_rows_df.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\classificator\\testDatasetWithIP.csv', index=False)

filtered_df = filtered_df.drop(['ip'], axis=1)
unknown_rows_df = unknown_rows_df.drop(['ip'], axis=1)

filtered_df.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\classificator\\trainDataset.csv', index=False)
#print(unknown_rows_df)
unknown_rows_df.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\classificator\\testDataset.csv', index=False)