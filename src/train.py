
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

mse, mae, rmse, mape = model_evaluation(y_test, y_pred_linear) 
print("For the baseline linear regression model with lag features: \n")
print("MSE:", mse)
print("MAE:", mae)
print("RMSE:", rmse)
print("MAPE:", mape)

#3) Lasso Regression model
#Using all features - Lasso will automatically shrink wights of less important ones to zero

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

y_pred_DT = DT_model.predict(X_test)

mse, mae, rmse, mape = model_evaluation(y_test, y_pred_DT) 
print("For the Decision Tree regression model: \n")
print("MSE:", mse)
print("MAE:", mae)
print("RMSE:", rmse)
print("MAPE:", mape)


#5) Random Forest regression model
#Ensemble of decision trees — typically the strongest performer on tabular
#data.

RF_model = random_forest_regression_model()
RF_model.fit(X_train, y_train)

y_pred_RF = RF_model.predict(X_test)

mse, mae, rmse, mape = model_evaluation(y_test, y_pred_RF)
print("For the Random Forest regression model: \n")
print("MSE:", mse)
print("MAE:", mae)
print("RMSE:", rmse)
print("MAPE:", mape)


