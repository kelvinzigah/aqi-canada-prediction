
#Since most of our models will require the same evaluation metrics, we'll create the function here which can be reused in train.py
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

def model_evaluation (true_values, predicted_values):
    mse = mean_squared_error(true_values, predicted_values) #Mean Squared Error: Seeing how well the model converged, and shows the overall error delta.
    mae = mean_absolute_error(true_values, predicted_values) #Mean absolute error: Standard averaging or the errors.
    rmse = root_mean_squared_error(true_values, predicted_values) #Root mean squared error: Very strict on large errors.
    mape = mean_absolute_percentage_error(true_values, predicted_values) #Percentage error, problamatic near zero.

    return mse, mae, rmse, mape


