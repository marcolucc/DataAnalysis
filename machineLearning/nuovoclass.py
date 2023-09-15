import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
import matplotlib.pyplot as plt
from sklearn.tree import export_graphviz
import os
import numpy as np
from graphviz import Source
from IPython.display import display
from PIL import Image
import pydot
from sklearn import tree

data = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\trainDataset.csv')

#I need to get data from moreIP.csv and concat it to the train_Dataset.csv
#but I need to drop column ip and add column classification
bigger_data = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\moreIP.csv')
bigger_data['classification'] = 'malicious'
bigger_data = bigger_data.drop('ip', axis=1)
bigger_data = bigger_data.drop('Timeout', axis=1)
bigger_data = bigger_data.drop('Undetected', axis=1)
#save the unknown rows

data = data[~data['classification'].str.contains('unknown')]
#drop the rows that have classification = Unknown
#save the unknown rows
data_unknown = data[data['classification'].str.contains('Unknown')]
#save to csv
data_unknown.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\unknown_new_class.csv', index=False)
print(data_unknown)

data = data[~data['classification'].str.contains('Unknown')]
bigger_data = bigger_data[data.columns]
data = pd.concat([data, bigger_data], ignore_index=True)

#I need to get data from cinss.csv and concat it to the train_Dataset.csv
#but I need to drop column ip and add column classification
cinss_data = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\cinss.csv')
cinss_data = cinss_data.drop('ip', axis=1)
cinss_data = cinss_data[data.columns]
data = pd.concat([data, cinss_data], ignore_index=True)




#drop rows where Harmless and Malicious are 0
data = data.drop(data[(data['Harmless'] == 0) & (data['Malicious'] == 0)].index)
X = data.drop('classification', axis=1)
X = X.drop('Suspicious', axis=1)
print(X.describe())
#search and print rows where Harmless and Malicious and Suspicious are 0
#print(len(data.loc[(data['Harmless'] == 0) & (data['Malicious'] == 0) & (data['Suspicious'] == 0)]) )



y = data['classification']
#print(X.head(5))

#discretize data
'''
est = KBinsDiscretizer(n_bins=6, encode='ordinal', strategy='quantile')
est.fit(X)
X = est.transform(X)
print(X)
'''


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)


svm_model = SVC()
naive_model = GaussianNB()
random_model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
ada_model = AdaBoostClassifier(n_estimators=100, random_state=0)
gradient_model = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
svm_model.fit(X_train, y_train)
naive_model.fit(X_train, y_train)
random_model.fit(X_train, y_train)
ada_model.fit(X_train, y_train)
gradient_model.fit(X_train, y_train)

y_pred_svm = svm_model.predict(X_test)
y_pred_naive = naive_model.predict(X_test)
y_pred_random = random_model.predict(X_test)
y_pred_ada = ada_model.predict(X_test)
y_pred_gradient = gradient_model.predict(X_test)

print("Accuracy score SVM: ", accuracy_score(y_test, y_pred_svm))
print("Accuracy score Naive: ", accuracy_score(y_test, y_pred_naive))
print("Accuracy score Random Forest: ", accuracy_score(y_test, y_pred_random))
print("Accuracy score AdaBoost: ", accuracy_score(y_test, y_pred_ada))
print("Accuracy score Gradient Boosting: ", accuracy_score(y_test, y_pred_gradient))



#Plot of data distribution SVM
# Create a label encoder object
le = LabelEncoder()
# Fit the label encoder to the 'y_pred' array
le.fit(y_pred_svm)
# Transform the 'y_pred' array to a sequence of numbers
y_pred_encoded = le.transform(y_pred_svm)
# Use the encoded 'y_pred' array in the 'c' argument of the scatter method
plt.scatter(X_test['Harmless'], X_test['Malicious'], c=y_pred_encoded, s=50, cmap='autumn')
# red decision boundary (hyperplane) for SVM
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
plt.xlabel('Harmless')
plt.ylabel('Malicious')
plt.title('SVM classification')
#plt.show()

#Plot of data distribution Naive
# Create a label encoder object
le = LabelEncoder()
# Fit the label encoder to the 'y_pred' array
le.fit(y_pred_naive)
# Transform the 'y_pred' array to a sequence of numbers
y_pred_encoded = le.transform(y_pred_naive)
# Use the encoded 'y_pred' array in the 'c' argument of the scatter method
plt.scatter(X_test['Harmless'], X_test['Malicious'], c=y_pred_encoded, s=50, cmap='autumn')
plt.xlabel('Harmless')
plt.ylabel('Malicious')
plt.title('Naive classification')
#plt.show()

#Plot of data distribution Random Forest
class_names = ['Malicious', 'Benign']
feature_names = ['Harmless', 'Malicious']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=800)
tree.plot_tree(random_model.estimators_[0], feature_names = feature_names, class_names=class_names, filled = True, rounded=True)
fig.savefig('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\rf_individualtree.png')

#Plot of data distribution AdaBoost
class_names = ['Malicious', 'Benign']
feature_names = ['Harmless', 'Malicious']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=800)
tree.plot_tree(ada_model.estimators_[0], feature_names = feature_names, class_names=class_names, filled = True, rounded=True)
fig.savefig('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\ada_individualtree.png')

#Plot of data distribution Gradient Boosting
class_names = ['Malicious', 'Benign']
feature_names = ['Harmless', 'Malicious']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=800)
tree.plot_tree(gradient_model.estimators_[0, 0], feature_names = feature_names, class_names=class_names, filled = True, rounded=True)
fig.savefig('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\gradient_individualtree.png')


# Save the trained SVM model and label encoder for future use
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\svm_model.pkl', 'wb') as model_file:
    pickle.dump(svm_model, model_file)

#Save naive model
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\naive_model.pkl', 'wb') as model_file:
    pickle.dump(naive_model, model_file)

#Save random forest model
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\random_model.pkl', 'wb') as model_file:
    pickle.dump(random_model, model_file)

#Save ada model
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\ada_model.pkl', 'wb') as model_file:
    pickle.dump(ada_model, model_file)

#Save gradient model
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\gradient_model.pkl', 'wb') as model_file:
    pickle.dump(gradient_model, model_file)


