import csv
import pandas as pd

# Open the output CSV file
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\output.csv', 'r', encoding='utf-8') as csv_file:
    grey_virus_out = csv.DictReader(csv_file)

with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\output.csv', 'r', encoding='utf-8') as csv_file:
    requests_out = csv.DictReader(csv_file)

# panda dataframe
grey_virus_out = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\output.csv')
grey_virus_out = grey_virus_out.drop(['actor'], axis=1)
grey_virus_out = grey_virus_out.drop(['organization'], axis=1)
requests_out = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\IPrequest\\Total_IPvsRequests.csv')

#print(grey_virus_out)
#print("*"*50)
#print(requests_out)

#merge the two dataframes
merged_df = pd.merge(grey_virus_out, requests_out, on='ip', how='inner')
#print(merged_df)
#print("A"*50)

#drop rows where classification = Unknown
merged_df = merged_df[~merged_df['classification'].str.contains('Unknown')]
#print(merged_df)

#SVM table
#concat the data from the csv 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_SVM.csv' to the merged_df
predicted_SVM = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_SVM.csv')
#drop Harmless, Malicious columns
predicted_SVM = predicted_SVM.drop(['Harmless'], axis=1)
predicted_SVM = predicted_SVM.drop(['Malicious'], axis=1)
finalsvm = pd.concat([merged_df, predicted_SVM], axis=0)
print(finalsvm)
finalsvm.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\final_SVM.csv', index=False)

#random forest table
#concat the data from the csv 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_rf.csv' to the merged_df
predicted_SVM = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_rf.csv')
#drop Harmless, Malicious columns
predicted_SVM = predicted_SVM.drop(['Harmless'], axis=1)
predicted_SVM = predicted_SVM.drop(['Malicious'], axis=1)
finalrf = pd.concat([merged_df, predicted_SVM], axis=0)
print(finalrf)
finalrf.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\final_rf.csv', index=False)

#naive bayes table
#concat the data from the csv 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_nb.csv' to the merged_df
predicted_SVM = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_naive.csv')
#drop Harmless, Malicious columns
predicted_SVM = predicted_SVM.drop(['Harmless'], axis=1)
predicted_SVM = predicted_SVM.drop(['Malicious'], axis=1)
finalnb = pd.concat([merged_df, predicted_SVM], axis=0)
print(finalnb)
finalnb.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\final_nb.csv', index=False)

#ada boost table
#concat the data from the csv 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_ada.csv' to the merged_df
predicted_SVM = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_ada.csv')
#drop Harmless, Malicious columns
predicted_SVM = predicted_SVM.drop(['Harmless'], axis=1)
predicted_SVM = predicted_SVM.drop(['Malicious'], axis=1)
finalada = pd.concat([merged_df, predicted_SVM], axis=0)
print(finalada)
finalada.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\final_ada.csv', index=False)

#gradient boost table
#concat the data from the csv 'C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_gradient.csv' to the merged_df
predicted_SVM = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_gradient.csv')
#drop Harmless, Malicious columns
predicted_SVM = predicted_SVM.drop(['Harmless'], axis=1)
predicted_SVM = predicted_SVM.drop(['Malicious'], axis=1)
finalgb = pd.concat([merged_df, predicted_SVM], axis=0)
print(finalgb)
finalgb.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\final_gradient.csv', index=False)


#Print table with for each classification entry the number of IPs and the sum of requests
#print("SVM")
#print(finalsvm.groupby('classification').agg({'ip':'count', 'requests':'sum'}))
#print a latex table with 
tab = (finalsvm.groupby('classification').agg({'ip':'count', 'requests':'sum'}).to_latex())
#add the caption \caption{SVM model Classification of IP addresses}
index = tab.index("rr}") + 3
tab = tab[:index] + "\n \caption{SVM model Classification of IP addresses}" + tab[index:]
print(tab)

#print("Random Forest")
#print(finalrf.groupby('classification').agg({'ip':'count', 'requests':'sum'}))
#print a latex table with
tab = (finalrf.groupby('classification').agg({'ip':'count', 'requests':'sum'}).to_latex())
#add the caption \caption{Random Forest model Classification of IP addresses}
index = tab.index("rr}") + 3
tab = tab[:index] + "\n \caption{Random Forest model Classification of IP addresses}" + tab[index:]
print(tab)

#print("Naive Bayes")
#print(finalnb.groupby('classification').agg({'ip':'count', 'requests':'sum'}))
#print a latex table with
tab = (finalnb.groupby('classification').agg({'ip':'count', 'requests':'sum'}).to_latex())
#add the caption \caption{Naive Bayes model Classification of IP addresses}
index = tab.index("rr}") + 3
tab = tab[:index] + "\n \caption{Naive Bayes model Classification of IP addresses}" + tab[index:]
print(tab)

#print("Ada Boost")
#print(finalada.groupby('classification').agg({'ip':'count', 'requests':'sum'}))
#print a latex table with
tab = (finalada.groupby('classification').agg({'ip':'count', 'requests':'sum'}).to_latex())
#add the caption \caption{Ada Boost model Classification of IP addresses}
index = tab.index("rr}") + 3
tab = tab[:index] + "\n \caption{Ada Boost model Classification of IP addresses}" + tab[index:]
print(tab)

#print("Gradient Boost")
#print(finalgb.groupby('classification').agg({'ip':'count', 'requests':'sum'}))
#print a latex table with
tab = (finalgb.groupby('classification').agg({'ip':'count', 'requests':'sum'}).to_latex())
#add the caption \caption{Gradient Boost model Classification of IP addresses}
index = tab.index("rr}") + 3
tab = tab[:index] + "\n \caption{Gradient Boost model Classification of IP addresses}" + tab[index:]
print(tab)
