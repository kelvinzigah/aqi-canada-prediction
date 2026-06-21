
#The purpose of this section is to train the machine learning models defined in models.py on the training dataset, and make predictions on the test dataset. 
#The performance of the models will then be evaluated using mean squared error (MSE) as the evaluation metric.

#Source used:
#[Train_1] https://github.com/jagwithyou/linear-regression-example/blob/master/simple_and_multiple_linear_regression.ipynb
#[Train_2] https://stackoverflow.com/questions/13411544/delete-a-column-from-a-pandas-dataframe
#[Train_3] https://www.kaggle.com/code/tomwarrens/timeseriessplit-how-to-use-it
##[Train_4] https://stackoverflow.com/questions/50879915/splitting-data-using-time-based-splitting-in-test-and-train-datasets
#[Train_5] https://stackoverflow.com/questions/62149138/how-to-split-dataset-as-train-and-test-data-into-rows-using-date-pandas-and-pyt
#[Train_6] https://apxml.com/courses/time-series-analysis-forecasting/chapter-6-model-evaluation-selection/train-test-split-time-series



from load_data import load_data
from models import linear_regression_model_base, linear_regression_model_lag, lasso_regression_model, decision_tree_regression_model, random_forest_regression_model, knn_regression_model
from sklearn.model_selection import train_test_split
from features import TARGET_VARIABLE
from evaluate import model_evaluation
from sklearn.model_selection import GridSearchCV


import numpy as np
import pandas as pd

#-----------------------------------------------------------------------
#SETUP BEFORE TRAINING THE MODELS:
#-----------------------------------------------------------------------

data = load_data() #Importing the training dataset, which has been preprocessed in preprocess_data.py and sent to load_data.py.
print("Dataset overview:") #Giving a small overview of the dataset:
print(data.info()) #Print the summary of the dataset, including the number of non-null values and the data types of each column.
print(data.head()) #Print the first 5 rows of the dataset

#Identifiying our input features and target variable:
X = data.drop(["index", "Date", "Season", TARGET_VARIABLE], axis = 1, errors = "ignore") #Getting our input features [Train_1]
y = data[TARGET_VARIABLE] #Getting our target.

print("Input features:")
print(X.head()) #Print the first 5 rows of the input features.
print("Target variable:")
print(y.head()) #Print the first 5 rows of the target variable.

#-----------------------------------------------------------------------
#TRAINING THE MODELS AND MAKING PREDICTIONS
#-----------------------------------------------------------------------

#Because we want to predict future AQHI values, we will use the most recent 20% of the data as the test set, and the rest as the training set.
#The training set is 80% of the data (2020-2023)
#The test set is the remaining 20% (2024)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle = False) #[Train_5]

print("Training sample length:", len(X_train))
print("Test sample length:", len(X_test))

#Add code to show first 5 rows of training and test, to make sure its sorted.


#1) Simple Linear Regression Model
#For our baseline model, only AQHI will be used to compare to future AQHI values. The reason is that we want to have a basic comparison to start with.

base_linear_model = linear_regression_model_base() #Getting the linear regression model defined in models.py.
base_linear_model.fit(X_train[["AQHI"]], y_train) #Training the linear regression model on the training dataset, only using the present AQHI to predict the future AQHI.

y_pred_linear = base_linear_model.predict(X_test[["AQHI"]]) #Making predictions on the test dataset using the trained linear regression model.

mse, mae, rmse, mape = model_evaluation(y_test, y_pred_linear) #Using the evaluation function in evaluate.py to evaluate our models:
print("For the baseline linear regression model: \n")
print("MSE:", mse)
print("MAE:", mae)
print("RMSE:", rmse)
print("MAPE:", mape)

#2) Linear Regression with lag features
#From now on, we will use all intended features to help predict the future AQHI value.

linear_model = linear_regression_model_lag()
linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test) #Making predictions on the test dataset using the trained linear regression model.
y_pred_linear = linear_model.predict(X_test) #Making predictions on the test dataset using the trained linear regression model.

mse, mae, rmse, mape = model_evaluation(y_test, y_pred_linear) 
print("For the linear regression model with lag features: \n")
print("MSE:", mse)
print("MAE:", mae)
print("RMSE:", rmse)
print("MAPE:", mape)

#3) Lasso Regression model
lasso_model = lasso_regression_model()
lasso_model.fit(X_train, y_train)

y_pred_lasso = lasso_model.predict(X_test)

mse, mae, rmse, mape = model_evaluation(y_test, y_pred_lasso)
print("For the Lasso regression model: \n")
print("MSE:", mse)
print("MAE:", mae)
print("RMSE:", rmse)
print("MAPE:", mape)


#4) Decision Tree regression model

DT_model = decision_tree_regression_model()
DT_model.fit(X_train, y_train)

#Using GridSearchCV to find the best hyperparameters for the decision tree regression model.
#Source: https://www.geeksforgeeks.org/machine-learning/hyperparameter-tuning-in-linear-regression/
#A breif explaination of the hyperparameters (Source: https://www.geeksforgeeks.org/machine-learning/how-to-tune-a-decision-tree-in-hyperparameter-tuning/):
#- max_depth: Controls the maximum depth on how long the tree can grow. Deeper tree can capture more complex patterns, but can also lead to overfitting. A shallower tree may not capture all the patterns in the data, but is more genralized.
#- min_samples_split: The minimum number of samples required to split a node. 
# -min_samples_leaf: The minimum number of samples required to be at a leaf node.
# -max_features: The number of features to consider when looking for the best split. THis can just be set to: auto which will use all features, sqrt which uses the square root of the number of features, and log2 which uses the logarithm base 2 of the number of features.
# -min_weight_fraction_leaf: The minimum fraction of input samples required to be at a leaf node. THis can help with class imbalance, but does not really apply for our regression problem.


param_grid = { #Giving a range of values for the hyperparameters to be tested in GridSearchCV.
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt', 'log2'],
    'min_weight_fraction_leaf': [0.0, 0.1, 0.2]
}

#Using GridSearchCV to find the best hyperparameters for the decision tree regression model.
#Source: https://www.geeksforgeeks.org/machine-learning/how-to-tune-a-decision-tree-in-hyperparameter-tuning/
grid_search = GridSearchCV(estimator=DT_model, param_grid=param_grid, cv=5) #CV means the amount of cross validation folds that were used. From Lecture 4, this is usually 5 or 10. 
grid_search.fit(X_train, y_train) #Using the training data only. This is very important; we do not want to use the test data to find the best hyperparameters, as this would lead to data leakage and overfitting.

best_DT_model_hyperparameters = grid_search.best_estimator_ #Getting the best estimator from the grid search.
print("Best hyperparameters for the decision tree regression model:", best_DT_model_hyperparameters)

y_pred_DT = best_DT_model_hyperparameters.predict(X_test) #Setting the prediction target to the best estimator found by GridSearchCV

#y_pred_DT = DT_model.predict(X_test)

mse, mae, rmse, mape = model_evaluation(y_test, y_pred_DT) 
print("For the Decision Tree regression model: \n")
print("MSE:", mse)
print("MAE:", mae)
print("RMSE:", rmse)
print("MAPE:", mape)

#5) Random Forest regression model
RF_model = random_forest_regression_model()
RF_model.fit(X_train, y_train)

y_pred_RF = RF_model.predict(X_test)

mse, mae, rmse, mape = model_evaluation(y_test, y_pred_RF)
print("For the Random Forest regression model: \n")
print("MSE:", mse)
print("MAE:", mae)
print("RMSE:", rmse)
print("MAPE:", mape)

    