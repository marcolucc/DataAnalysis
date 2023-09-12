import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
import pickle
from sklearn.preprocessing import StandardScaler

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\testDataset.csv')

X = data.drop('classification', axis=1)
y = data['classification']

# Convert string labels to numeric labels
#le = LabelEncoder()
#y = le.fit_transform(y)

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train = X
y_train = y
X_test = X
y_test = y

# Normalize the input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

data1 = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\trainDataset.csv')
data1Withip = pd.read_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\trainDatasetWithip.csv')
#X_test = data1.drop('classification', axis=1)

# Create and train SVM model on the training data
svm_model = SVC(C=10, gamma='scale', kernel='rbf')
svm_model.fit(X_train, y_train)

# Define the parameter grid to search over
#param_grid = {
#    'C': [0.1, 1, 10],
#    'kernel': ['linear', 'rbf', 'poly'],
#    'gamma': ['scale', 'auto']
#}

# Create a GridSearchCV object and fit it to the training data
#grid_search = GridSearchCV(SVC(), param_grid, scoring='accuracy', cv=5)
#grid_search.fit(X_train, y_train)

# Print the best set of hyperparameters and the corresponding accuracy score
#print("Best hyperparameters: ", grid_search.best_params_)
#print("Accuracy score: ", grid_search.best_score_)

# Make predictions on the test data using the best model
#best_model = grid_search.best_estimator_
#y_pred = best_model.predict(X_test)

# Make predictions on the test data
y_pred = svm_model.predict(X_test)

# Convert numeric labels back to string labels
#y_pred = le.inverse_transform(y_pred)
print(y_pred)
# Calculate and print the accuracy on the test set
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on Test Set: {accuracy}")

confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
print(confusion_matrix)

'''
precision = confusion_matrix[1][1] / (confusion_matrix[1][1] + confusion_matrix[0][1])
recall = confusion_matrix[1][1] / (confusion_matrix[1][1] + confusion_matrix[1][0])
f1 = 2 * precision * recall / (precision + recall)
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
'''


# Save the trained SVM model and label encoder for future use
#with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\svm_model.pkl', 'wb') as model_file:
#    pickle.dump(svm_model, model_file)

#with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\label_encoder.pkl', 'wb') as le_file:
#    pickle.dump(le, le_file)

new_data = data1.drop('classification', axis=1)
new_pred = svm_model.predict(new_data)
#new_pred = le.inverse_transform(new_pred)
#print(new_pred)
print(len(new_pred))
data1['classification'] = new_pred
data1['ip'] = data1Withip['ip']
data1.to_csv('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\predicted.csv', index=False)



#Random Forest
# Create and train Random Forest model on the training data
rf_model = RandomForestClassifier(n_estimators=100, max_depth=5)
rf_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = rf_model.predict(X_test)

# Convert numeric labels back to string labels
y_pred = le.inverse_transform(y_pred)

# Calculate and print the accuracy on the test set
accuracy = accuracy_score(y_test, y_pred)
#accuracy score, bestscore
print(f"Accuracy on Test Set: {accuracy}")


