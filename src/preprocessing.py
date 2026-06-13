import pandas as pd
from src.config import FEATURE_COLS, TARGET_COL


def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    min_count = int((1 - threshold) * len(df))
    return df.dropna(axis=1, thresh=min_count).dropna()


def encode_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    cat_cols = df.select_dtypes(include="object").columns.tolist()
    return pd.get_dummies(df, columns=cat_cols, drop_first=True)


def select_features(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    available = [c for c in FEATURE_COLS if c in df.columns]
    X = df[available].copy()
    y = df[TARGET_COL].copy()
    return X, y


def run(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    df = drop_missing(df)
    df = encode_categoricals(df)
    return select_features(df)
