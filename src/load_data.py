import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "processed" / "air_quality_project_dataset.csv"
DATA_PATH_DEMO = Path(__file__).resolve().parent.parent / "data" / "processed" / "air_quality_project_dataset_Demo.csv"

#Loading the preprocessed training dataset. This will be called in the main function to load the data before training the model.
def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["Date"]) #df stands for "dataframe" it's how pandas sees data
    return df
 
#Loading the demo dataset, which will be used in demo.py 
def load_data_demo():
    df_demo = pd.read_csv(DATA_PATH_DEMO, parse_dates=["Date"])
    return df_demo

