import pandas as pd

# Define the file paths for your CSV files
file1_path = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\meta11gn_analysis_2023-09-07-1205.csv'
file2_path = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\meta12gn_analysis_2023-09-07-1211.csv'
file3_path = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\meta21gn_analysis_2023-09-07-1214.csv'
file4_path = 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\meta22gn_analysis_2023-09-07-1215.csv'

#Classification 
#Features: Hramless, malicious, suspicious
#discretizzare le features
#Class: 0 mal, 1 sus, 2 harm
#SVM classificatore 
#testset 20% del dataset
#cross validation 


df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)
df3 = pd.read_csv(file3_path)
df4 = pd.read_csv(file4_path)

# Concatenate the dataframes vertically to merge them
#merged_df = pd.concat([df1, df2, df3], ignore_index=True)
merged_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

total_lines = len(merged_df)
print(merged_df)
print(f"Total lines after merging: {total_lines}")
merged_df.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\merged.csv', index=False)
