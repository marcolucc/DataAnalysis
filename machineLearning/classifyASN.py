import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import KBinsDiscretizer
##################################àà
#####################àààààààà
##########DEVO PRENDERE I NUOVI MODELLI ASN E FAR CLASSIFICARE A LORO IL TEST DATASET
##SOLO CHE DEVO METTERE NEL TEST DATASET PURE L'ASN SE NON C'è 

# panda dataframe
grey_virus_out = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\greynoiseRes\\output.csv')
grey_virus_out = grey_virus_out.drop(['actor'], axis=1)
grey_virus_out = grey_virus_out.drop(['organization'], axis=1)
requests_out = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\IPrequest\\Total_IPvsRequests.csv')
# Merge the two CSV files inner join on the IP address
merged_df = pd.merge(grey_virus_out, requests_out, on='ip', how='inner')
unknown_tmp = merged_df[merged_df['classification'] == 'Unknown']
print(unknown_tmp)
#save requests column
requests_unknown = unknown_tmp['requests']
#unknown_tmp = unknown_tmp.drop(['requests'], axis=1)




#import SVM model
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\svm_model.pkl', 'rb') as model_file:
    svm_model = pickle.load(model_file)
datatest = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\testDatasetWithIP.csv')

datatest = pd.merge(datatest, unknown_tmp, on='ip', how='inner')
print("*"*100)
#print(datatest)

#save a dataframe with ip and requests to use later
datatestWithip = datatest[['ip', 'requests']]
datatest = datatest.drop(['ip'], axis=1)
datatest = datatest.drop(['classification_x'], axis=1)
datatest = datatest.drop(['classification_y'], axis=1)
datatest = datatest.drop(['Suspicious'], axis=1)
datatest = datatest.drop(['requests'], axis=1)

#x_test = datatest.drop('classification', axis=1)
#x_test = x_test.drop('Suspicious', axis=1)
x_test = datatest
y_pred = svm_model.predict(x_test)
# Get confidence scores for predictions
confidence_scores = svm_model.decision_function(x_test)
#for i in range(len(y_pred)):
#    print(f"Prediction: {y_pred[i]}, Confidence Score: {confidence_scores[i]}")
#add ip and save file
datatest['classification'] = y_pred
datatest['ip'] = datatestWithip['ip']
datatest['requests'] = datatestWithip['requests']
#put ip column in first position
cols = datatest.columns.tolist()
cols = cols[-1:] + cols[:-1]
datatest = datatest[cols]
datatest.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_SVM.csv', index=False)
print("SVM prediction")
print("total number of malicious ip: {}".format(len(datatest.loc[datatest['classification'] == 'malicious'])))
print("total number of benign ip: {}".format(len(datatest.loc[datatest['classification'] == 'benign'])))

#random forest
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\random_model.pkl', 'rb') as model_file:
    rf_model = pickle.load(model_file)
datatest = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\testDatasetWithIP.csv')
datatest = pd.merge(datatest, unknown_tmp, on='ip', how='inner')
datatestWithip = datatest[['ip', 'requests']]
datatest = datatest.drop(['ip'], axis=1)
datatest = datatest.drop(['classification_x'], axis=1)
datatest = datatest.drop(['classification_y'], axis=1)
datatest = datatest.drop(['Suspicious'], axis=1)
datatest = datatest.drop(['requests'], axis=1)
x_test = datatest
y_pred = rf_model.predict(x_test)
#add ip and save file
datatest['classification'] = y_pred
datatest['ip'] = datatestWithip['ip']
datatest['requests'] = datatestWithip['requests']
#put ip column in first position
cols = datatest.columns.tolist()
cols = cols[-1:] + cols[:-1]
datatest = datatest[cols]
datatest.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_rf.csv', index=False)
print("Random Forest prediction")
print("total number of malicious ip: {}".format(len(datatest.loc[datatest['classification'] == 'malicious'])))
print("total number of benign ip: {}".format(len(datatest.loc[datatest['classification'] == 'benign'])))



#naive bayes
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\naive_model.pkl', 'rb') as model_file:
    naive_model = pickle.load(model_file)
datatest = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\testDatasetWithIP.csv')
datatest = pd.merge(datatest, unknown_tmp, on='ip', how='inner')
datatestWithip = datatest[['ip', 'requests']]
datatest = datatest.drop(['ip'], axis=1)
datatest = datatest.drop(['classification_x'], axis=1)
datatest = datatest.drop(['classification_y'], axis=1)
datatest = datatest.drop(['Suspicious'], axis=1)
datatest = datatest.drop(['requests'], axis=1)
x_test = datatest
y_pred = naive_model.predict(x_test)
#add ip and save file
datatest['classification'] = y_pred
datatest['ip'] = datatestWithip['ip']
datatest['requests'] = datatestWithip['requests']
#put ip column in first position
cols = datatest.columns.tolist()
cols = cols[-1:] + cols[:-1]
datatest = datatest[cols]
datatest.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_naive.csv', index=False)
print("Naive Bayes prediction")
print("total number of malicious ip: {}".format(len(datatest.loc[datatest['classification'] == 'malicious'])))
print("total number of benign ip: {}".format(len(datatest.loc[datatest['classification'] == 'benign'])))

#ada boost
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\ada_model.pkl', 'rb') as model_file:
    ada_model = pickle.load(model_file)
datatest = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\testDatasetWithIP.csv')
datatest = pd.merge(datatest, unknown_tmp, on='ip', how='inner')
datatestWithip = datatest[['ip', 'requests']]
datatest = datatest.drop(['ip'], axis=1)
datatest = datatest.drop(['classification_x'], axis=1)
datatest = datatest.drop(['classification_y'], axis=1)
datatest = datatest.drop(['Suspicious'], axis=1)
datatest = datatest.drop(['requests'], axis=1)
x_test = datatest
datatest['classification'] = y_pred
#put ip column in first position
cols = datatest.columns.tolist()
cols = cols[-1:] + cols[:-1]
datatest = datatest[cols]
datatest.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_ada.csv', index=False)
print("Ada Boost prediction")
print("total number of malicious ip: {}".format(len(datatest.loc[datatest['classification'] == 'malicious'])))
print("total number of benign ip: {}".format(len(datatest.loc[datatest['classification'] == 'benign'])))

#gradient boost
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\gradient_model.pkl', 'rb') as model_file:
    gradient_model = pickle.load(model_file)
datatest = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\testDatasetWithIP.csv')
datatest = pd.merge(datatest, unknown_tmp, on='ip', how='inner')
datatestWithip = datatest[['ip', 'requests']]
datatest = datatest.drop(['ip'], axis=1)
datatest = datatest.drop(['classification_x'], axis=1)
datatest = datatest.drop(['classification_y'], axis=1)
datatest = datatest.drop(['Suspicious'], axis=1)
datatest = datatest.drop(['requests'], axis=1)
x_test = datatest
y_pred = gradient_model.predict(x_test)
#add ip and save file
datatest['classification'] = y_pred
datatest['ip'] = datatestWithip['ip']
datatest['requests'] = datatestWithip['requests']
#put ip column in first position
cols = datatest.columns.tolist()
cols = cols[-1:] + cols[:-1]
datatest = datatest[cols]
datatest.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_gradient.csv', index=False)
print("Gradient Boost prediction")
print("total number of malicious ip: {}".format(len(datatest.loc[datatest['classification'] == 'malicious'])))
print("total number of benign ip: {}".format(len(datatest.loc[datatest['classification'] == 'benign'])))



