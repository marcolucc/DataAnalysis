import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import KBinsDiscretizer

#import SVM model
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\svm_model.pkl', 'rb') as model_file:
    svm_model = pickle.load(model_file)
datatest = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\test_Dataset.csv')
x_test = datatest.drop('classification', axis=1)
x_test = x_test.drop('Suspicious', axis=1)
y_pred = svm_model.predict(x_test)
#add ip and save file
datatestWithip = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\test_DatasetWithip.csv')
datatest['ip'] = datatestWithip['ip']
datatest['classification'] = y_pred
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
datatest = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\test_Dataset.csv')
x_test = datatest.drop('classification', axis=1)
x_test = x_test.drop('Suspicious', axis=1)
y_pred = rf_model.predict(x_test)
#add ip and save file
datatestWithip = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\test_DatasetWithip.csv')
datatest['ip'] = datatestWithip['ip']
datatest['classification'] = y_pred
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
datatest = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\test_Dataset.csv')
x_test = datatest.drop('classification', axis=1)
x_test = x_test.drop('Suspicious', axis=1)
y_pred = naive_model.predict(x_test)
#add ip and save file
datatestWithip = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\test_DatasetWithip.csv')
datatest['ip'] = datatestWithip['ip']
datatest['classification'] = y_pred
#put ip column in first position
cols = datatest.columns.tolist()
cols = cols[-1:] + cols[:-1]
datatest = datatest[cols]
datatest.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted_naive.csv', index=False)
print("Naive Bayes prediction")
print("total number of malicious ip: {}".format(len(datatest.loc[datatest['classification'] == 'malicious'])))
print("total number of benign ip: {}".format(len(datatest.loc[datatest['classification'] == 'benign'])))


