import pandas as pd
from pathlib import Path
from src.config import DATA_RAW, DATA_PROCESSED


def load_raw(filename: str) -> pd.DataFrame:
    path = DATA_RAW / filename
    return pd.read_csv(path)


def load_processed(filename: str = "aqi_processed.csv") -> pd.DataFrame:
    path = DATA_PROCESSED / filename
    return pd.read_csv(path)


def save_processed(df: pd.DataFrame, filename: str = "aqi_processed.csv") -> None:
    path = DATA_PROCESSED / filename
    df.to_csv(path, index=False)
