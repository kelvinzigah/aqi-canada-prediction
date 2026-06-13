import pandas as pd
from sklearn.preprocessing import StandardScaler


def add_rolling_mean(df: pd.DataFrame, col: str, window: int = 7) -> pd.DataFrame:
    result = df.copy()
    result[f"{col}_roll{window}"] = df[col].rolling(window, min_periods=1).mean()
    return result


def scale(X_train: pd.DataFrame, X_test: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, StandardScaler]:
    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)
    return X_train_scaled, X_test_scaled, scaler
