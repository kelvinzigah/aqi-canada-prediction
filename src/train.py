
#The purpose of this section is to train the machine learning models defined in models.py on the training dataset, and make predictions on the test dataset. 
#The performance of the models will then be evaluated using mean squared error (MSE) as the evaluation metric.
from load_data import load_data, split_data, get_X_Y
from models import linear_regression_model, lasso_regression_model, knn_regression_model, decision_tree_regression_model, random_forest_regression_model
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

#-----------------------------------------------------------------------
#SETUP BEFORE TRAINING THE MODELS:
#-----------------------------------------------------------------------

#Importing the training dataset, which has been preprocessed in preprocess_data.py and sent to load_data.py.
df = load_data()
train, test = split_data(df)
X_train, Y_train = get_X_Y(train)
X_test, Y_test = get_X_Y(test)


#-----------------------------------------------------------------------
#TRAINING THE MODELS AND MAKING PREDICTIONS
#-----------------------------------------------------------------------

#Main function to train the models and make predictions on the test dataset.