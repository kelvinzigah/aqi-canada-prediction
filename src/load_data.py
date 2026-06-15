import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "processed" / "air_quality_project_dataset.csv"

#Loading the preprocessed training dataset. This will be called in the main function to load the data before training the model.
def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["Date"]) #df stands for "dataframe" it's how pandas sees data
    return df
 
def split_data(df):
    train = df[df["Date"].dt.year <= 2023].copy() #training data
    test = df[df["Date"].dt.year == 2024].copy() #test data

    return train, test

FEATURES = [
    "Day", "Month", "Season_Code", "NO2", "O3", "PM25", "AQHI", "AQHI_PreviousDay"
]

TARGET = "AQHI_NextDay" #label

def get_X_Y(df):
    X = df[FEATURES]
    Y = df[TARGET]
    return X,Y


