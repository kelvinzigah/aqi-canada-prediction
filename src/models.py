from sklearn.linear_model import LinearRegression, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

#The purpose of this file is just to define the machine learning models that will be used for training and prediction. 
#The models will then be called in train.py to train the model on the training dataset and make predictions on the test dataset.

#Sources used:
#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
#https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html
#https://scikit-learn.org/1.5/auto_examples/linear_model/plot_ols.html
#https://www.geeksforgeeks.org/machine-learning/k-nearest-neighbors-knn-regression-with-scikit-learn/
#https://www.geeksforgeeks.org/machine-learning/k-nearest-neighbours/
#https://www.geeksforgeeks.org/machine-learning/knn-vs-decision-tree-in-machine-learning/



#1) Simple Linear Regression model (baseline model)
#Reason: A good simple model to start with, since we are trying to predict a continuous variable (AQHI). We will only compare the current AQHI with future AQHI here.
def linear_regression_model_base():
    return LinearRegression()


#2) Linear Regression model with lag features
#Reason: We want to use a more thorough Linear Regression Model that uses all of the features to pridict the future AQHI.
def linear_regression_model_lag():
    return LinearRegression()


#3) Lasso Regression model (regularization model)
#Reason: Since we are including extra features outside the AQHI formula, we want to use a regularization model to prevent overfitting and improve the generalization of the model.
def lasso_regression_model():
    return Lasso(alpha=0.1) #Setting alpha to 0.1 for regularization strength, this can be tuned based on the dataset and performance.



#3) K-Nearest Neighbors regression model (non-linear model)
#Reason: Does not assume anything about the data distribution. It can capture non-linear patterns between features and AQHI.
#Important note: Scaling is critical here since KNN uses distance between data points.
def knn_regression_model():
    return KNeighborsRegressor(n_neighbors=5) #Setting n_neighbors to 5, this can be tuned based on dataset performance.


#4) Decision Tree regression model (non-linear model)
#Reason: Can be used to provide more information about feature important, and captures the data patterns, not the data points.
def decision_tree_regression_model():
    return DecisionTreeRegressor(max_depth=5, random_state=42) #Setting max_depth to 5 to prevent overfitting, this can be tuned based on the dataset and performance.


#5) Random Forest regression model (ensemble model)
#Reason: By using an emsemble of decision trees, we can improve the performance and reduce the overfitting of the model. It also makes the trees less correlated with each other, which imroves generalization.
def random_forest_regression_model():
    return RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42) #Setting n_estimators to 100 for the number of trees in the forest, and max_depth to 5 to prevent overfitting, these can be tuned based on the dataset and performance.

