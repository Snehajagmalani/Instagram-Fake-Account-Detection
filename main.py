 # Import necessary libraries
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('instagram_train.csv')

# Split the data into training and testing sets
X = data.iloc[:, :-1].values # input features
y = data.iloc[:, -1].values # target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a logistic regression object and fit it to the training data
lr = LogisticRegression()
lr.fit(X_train, y_train)
filename = 'lr_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(lr, file)
# Predict the test set results and calculate the accuracy score
y_pred = lr.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy * 100)) 
