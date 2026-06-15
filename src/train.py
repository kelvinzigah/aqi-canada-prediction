
#The purpose of this section is to train the machine learning models defined in models.py on the training dataset, and make predictions on the test dataset. 
#The performance of the models will then be evaluated using mean squared error (MSE) as the evaluation metric.

from load_data import load_data
from models import linear_regression_model, lasso_regression_model, knn_regression_model, decision_tree_regression_model, random_forest_regression_model
from sklearn.metrics import mean_squared_error

import numpy as np
import pandas as pd

#-----------------------------------------------------------------------
#SETUP BEFORE TRAINING THE MODELS:
#-----------------------------------------------------------------------

#Importing the training dataset, which has been preprocessed in preprocess_data.py and sent to load_data.py.
data = load_data()
#Giving a small overview of the dataset:
print("Dataset overview:")
print(data.info()) #Print the summary of the dataset, including the number of non-null values and the data types of each column.
print(data.head()) #Print the first 5 rows of the dataset

#Identifiying our input features and target variable:
features = data.drop(columns=[TARGET_VARIABLE]) #Dropping the target variable column to get the input features.
target = data[TARGET_VARIABLE] #Getting the target variable column.

X = data[features] #Input features
y = data[target] #Target variable

print("Input features:")
display(X.head()) #Print the first 5 rows of the input features.
print("Target variable:")
display(y.head()) #Print the first 5 rows of the target variable.


#Source for graph plotting: https://github.com/jagwithyou/linear-regression-example/blob/master/simple_and_multiple_linear_regression.ipynb

#Plotting a graph to see an overview of the relationship between the input features and the target variable (AQHI).
plt.figure(figsize=(10, 6))
plt.scatter(X['O3'], y, label='O3', c='blue') #Scatter plot of O3 concentration vs AQHI index.
plt.xlabel('O3 Concentration')
plt.ylabel('AQHI Index')
plt.title('Relationship between O3 Concentration and AQHI Index')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(X['NO2'], y, label='NO2', c='orange') #Scatter plot of NO2 concentration vs AQHI index.
plt.xlabel('NO2 Concentration')
plt.ylabel('AQHI Index')
plt.title('Relationship between NO2 Concentration and AQHI Index')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(X['PM2.5'], y, label='PM2.5', c='green') #Scatter plot of PM2.5 concentration vs AQHI index.
plt.xlabel('PM2.5 Concentration')
plt.ylabel('AQHI Index')
plt.title('Relationship between PM2.5 Concentration and AQHI Index')
plt.legend()
plt.show()


#-----------------------------------------------------------------------
#TRAINING THE MODELS AND MAKING PREDICTIONS
#-----------------------------------------------------------------------


#Splitting the dataset into training and test sets, using an 80-20 split.
#Because we want to predict future AQHI values, we will use the most recent 20% of the data as the test set, and the rest as the training set.
#So, 2024 data will be in the test set, and the rest of the data will be in the training set.



#Main function to train the models and make predictions on the test dataset.