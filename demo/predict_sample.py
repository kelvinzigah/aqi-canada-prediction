import sys
import pandas as pd
sys.path.append("../src")

from load_data import load_data
from models import random_forest_regression_model #the best model currently
from features import TARGET_VARIABLE
from sklearn.model_selection import train_test_split

#define data
data = load_data()
X = data.drop(["index","Date","Season", TARGET_VARIABLE], axis=1, errors="ignore")
Y = data[TARGET_VARIABLE]
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, shuffle=False)


#define model and retrain
model = random_forest_regression_model()
model.fit(X_train, Y_train)


#unseen dataframe
sample = pd.DataFrame([{
    "Day": 15,
    "Month": 1,
    "NO2": 18.5,
    "O3": 12.0,
    "PM25": 8.3,
    "AQHI_PreviousDay": 1.9,
    "AQHI": 2.1,
    "Season_Code": 0
}])

#prediction
predicted_aqhi = model.predict(sample)[0]

if predicted_aqhi <= 3:
    risk = "Low"
elif predicted_aqhi <= 6:
    risk = "Moderate"
elif predicted_aqhi <= 10:
    risk = "High"
else:
    risk = "Very High"

print(f"Predicted Next-Day AQHI: {predicted_aqhi:.2f}")
print(f"Risk level: {risk}")
