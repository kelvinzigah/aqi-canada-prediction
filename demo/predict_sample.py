#A quick demo to show the use of the model on new data. THe dataset used is 2019 data from the Montreal Trudeau Airport.
#We'll only use the best model from the training/test results: Random Forest.


import sys
from pathlib import Path
import joblib

# Put the project's src/ folder on the path so the imports below resolve,
# regardless of which directory this script is run from.
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from evaluate import model_evaluation
from features import TARGET_VARIABLE
from load_data import load_data_demo

data_demo = load_data_demo()
print("Demo dataset overview:") #Giving a small overview of the dataset:
print(data_demo.info())
print(data_demo.head())


#Loading the save RF model from the training/test results:
MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "saved_model.pkl"  # Path to load the model
rf_model_demo = joblib.load(MODEL_PATH)  # Load the saved model from the specified path

#Identifiying our input features and target variable:
X = data_demo.drop(["index", "Date", "Season", TARGET_VARIABLE], axis = 1, errors = "ignore") #Getting our input features, and getting rid of the ones we dont need. [Train_1]
X = X[rf_model_demo.feature_names_in_] #Reorder columns to match the exact order the model was trained on (the demo CSV orders Season_Code differently).
y = data_demo[TARGET_VARIABLE] #Getting our target.

print("Input features:")
print(X.head()) 
print("Target variable:")
print(y.head()) 


#Getting our prediction:
y_pred_RF_demo = rf_model_demo.predict(X) #Making predictions on the demo dataset using the trained random forest model.


#Seeing the results compared to the actual values:
mse, mae, rmse, mape = model_evaluation(y, y_pred_RF_demo) 
print("For the demo results: \n")
print("MSE:", mse)
print("MAE:", mae)
print("RMSE:", rmse)
print("MAPE:", mape)