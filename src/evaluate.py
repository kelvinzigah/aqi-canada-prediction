
#Since most of our models will require the same evaluation metrics, we'll create the function here which can be reused in train.py
import warnings

import numpy as np

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit

from models import arima_model

def model_evaluation (true_values, predicted_values):
    mse = mean_squared_error(true_values, predicted_values) #Mean Squared Error: Seeing how well the model converged, and shows the overall error delta.
    mae = mean_absolute_error(true_values, predicted_values) #Mean absolute error: Standard averaging or the errors.
    rmse = root_mean_squared_error(true_values, predicted_values) #Root mean squared error: Very strict on large errors.
    mape = mean_absolute_percentage_error(true_values, predicted_values) #Percentage error, problamatic near zero.

    return mse, mae, rmse, mape


#The hyperpatameter tuning functions will be listed and explained here, to make the train.py code easier to read/cleaner.


#Lasso regression model hyperparameter tuning function:
#- Alpha: The regularization strength.
def get_param_grid_lasso():
    param_grid_lasso = {
    'alpha': [0.01, 0.1, 1, 10, 100]
}
    return param_grid_lasso

#Tuning the model for the best hyperparameters using GridSearchCV:
def get_best_lasso_model(lasso_model, param_grid_lasso, X_train, y_train):
    time_series_split = TimeSeriesSplit(n_splits=5) #Using TimeSeriesSplit for the CV, since we are working with time series data.
    grid_search_lasso = GridSearchCV(estimator=lasso_model, param_grid=param_grid_lasso, scoring = 'neg_mean_squared_error', cv=time_series_split) #CV means the amount of cross validation folds that were used. From Lecture 4, this is usually 5 or 10. We will use TimeSeriesSplit for the CV.
    grid_search_lasso.fit(X_train, y_train) #Using the training data only. This is very important; we do not want to use the test data to find the best hyperparameters, as this would lead to data leakage and overfitting.

    return grid_search_lasso #Returning GridSearchCV results.


#Decision Tree regression model hyperparameter tuning function:

#Using GridSearchCV to find the best hyperparameters for the decision tree regression model.
#Source: https://www.geeksforgeeks.org/machine-learning/hyperparameter-tuning-in-linear-regression/
#A breif explaination of the hyperparameters (Source: https://www.geeksforgeeks.org/machine-learning/how-to-tune-a-decision-tree-in-hyperparameter-tuning/):
#- max_depth: Controls the maximum depth on how long the tree can grow. Deeper tree can capture more complex patterns, but can also lead to overfitting. A shallower tree may not capture all the patterns in the data, but is more genralized.
#- min_samples_split: The minimum number of samples required to split a node. 
# -min_samples_leaf: The minimum number of samples required to be at a leaf node.
# -max_features: The number of features to consider when looking for the best split. THis can just be set to: auto which will use all features, sqrt which uses the square root of the number of features, and log2 which uses the logarithm base 2 of the number of features.

def get_param_grid_DT():
    param_grid_DT = { #Giving a range of values for the hyperparameters to be tested in GridSearchCV.
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': [None, 'sqrt', 'log2']
}
    return param_grid_DT

#Tuning the model for the best hyperparameters using GridSearchCV:
#Some important things about this function (Source: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html):
# -The cross validation used is NOT the standard k-folds, but a variation called TimeSeriesSplit, which is used for time series data.
# -With TimeSeriesSplit, the data is split into k folds, but the test set is always after the training set.
def get_best_DT_model(DT_model, param_grid_DT, X_train, y_train):
  
#Source: https://www.geeksforgeeks.org/machine-learning/how-to-tune-a-decision-tree-in-hyperparameter-tuning/
#Source: https://tomerkatzav.medium.com/split-time-series-dataset-826b7dc39cd9
    time_series_split = TimeSeriesSplit(n_splits=5) #Using TimeSeriesSplit for the CV, since we are working with time series data.
    grid_searchDT = GridSearchCV(estimator=DT_model, param_grid=param_grid_DT, scoring = 'neg_mean_squared_error', cv=time_series_split) #CV means the amount of cross validation folds that were used. From Lecture 4, this is usually 5 or 10. We will use TimeSeriesSplit for the CV.
    grid_searchDT.fit(X_train, y_train) #Using the training data only. This is very important; we do not want to use the test data to find the best hyperparameters, as this would lead to data leakage and overfitting.

    return grid_searchDT #Returning GridSearchCV results.


#ARIMA rolling one-step-ahead forecast function:
#ARIMA is a pure time series model, so it does not fit the same X/y pattern as the other models. Instead, it forecasts the AQHI series one step at a time.
#To compare it fairly with the other models, we forecast the test period one day at a time:
# - The series column is the daily AQHI values, where AQHI_NextDay[i] is just AQHI[i+1] (the next day's value).
# - For each test day i, we fit ARIMA on every AQHI value known up to and including day i, then forecast the next day.
# - That forecast is AQHI[i+1], which lines up exactly with the AQHI_NextDay target the other models predict.
#This is called a rolling (or walk-forward) forecast. We refit at every step so the model always uses all the data available up to that day, with no data leakage from the future.
#Sources:
#https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html
#https://machinelearningmastery.com/make-sample-forecasts-arima-python/
def rolling_arima_forecast(series, split_index, order=(2, 0, 0)):
    series = np.asarray(series, dtype=float) #Working with the raw AQHI values as a plain numeric array.
    predictions = [] #This will hold one forecast per test day.

    #We loop over every test day. range(split_index, len(series)) matches the test rows used by train_test_split with shuffle=False.
    for i in range(split_index, len(series)):
        history = series[:i + 1] #All AQHI values known up to and including day i (no future data).

        with warnings.catch_warnings(): #Hiding the harmless "no frequency information" notices statsmodels prints for a plain numeric series.
            warnings.simplefilter("ignore")
            fitted_model = arima_model(history, order=order).fit() #Fitting ARIMA on the history available at day i.
            next_day_forecast = fitted_model.forecast(steps=1)[0] #Forecasting the next day, which corresponds to the AQHI_NextDay target for day i.

        predictions.append(next_day_forecast)

    return np.array(predictions) #Returning all the one-step-ahead forecasts, aligned with y_test.


#Random Forest regression model hyperparameter tuning function (same idea as before):

#A brief explaination of the hyperparameters (Based on the Lecture 8 notes and the features from the source: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
#- n_estimators: The number of trees in the forest.
#- max_depth: Controls the maximum depth of each tree.
#- min_samples_leaf: The minimum number of samples required to be at a leaf node.
#- min_samples_split: The minimum number of samples required to split a node. .
#- max_features: The number of features considered per split.

def get_param_grid_RF():
    param_grid_RF = {
    'n_estimators': [10, 50, 100],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2, 4],
    'max_features': [None, 'sqrt']
   
}
    return param_grid_RF

#Tuning the model for the best hyperparameters using GridSearchCV:
def get_best_RF_model(RF_model, param_grid_RF, X_train, y_train):
    time_series_split = TimeSeriesSplit(n_splits=5) #Using TimeSeriesSplit for the CV, since we are working with time series data.
    grid_searchRF = GridSearchCV(estimator=RF_model, param_grid=param_grid_RF, scoring = 'neg_mean_squared_error', cv=time_series_split) #CV means the amount of cross validation folds that were used. From Lecture 4, this is usually 5 or 10. We will use TimeSeriesSplit for the CV.
    grid_searchRF.fit(X_train, y_train) #Using the training data only. This is very important; we do not want to use the test data to find the best hyperparameters, as this would lead to data leakage and overfitting.

    return grid_searchRF #Returning GridSearchCV results.