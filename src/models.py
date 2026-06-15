from skilearn.linear_model import LinearRegression
from skilearn.metrics import mean_squared_error

#Sources used:
#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
#https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html
#https://scikit-learn.org/1.5/auto_examples/linear_model/plot_ols.html



#Linear Regression model (baseline model)
def linear_regression_model():
    #Creating a linear regression model object
    LinReg = linear.model.LinearRegression()
    #Training the model on the training dataset
    LinReg.fit(X_train, y_train) **To be replaced with the actual training dataset variables**


    return LinReg
