import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from src.config import RESULTS_DIR, PLOTS_DIR
import numpy as np


def compute_metrics(y_true, y_pred, name: str) -> dict:
    return {
        "model": name,
        "MAE": mean_absolute_error(y_true, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_true, y_pred)),
        "R2": r2_score(y_true, y_pred),
    }


def save_metrics_table(rows: list[dict]) -> None:
    df = pd.DataFrame(rows)
    df.to_csv(RESULTS_DIR / "metrics_table.csv", index=False)
    print(df.to_string(index=False))


def plot_predictions(y_true, y_pred, name: str) -> None:
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(y_true, y_pred, alpha=0.4, s=10)
    lims = [min(y_true.min(), y_pred.min()), max(y_true.max(), y_pred.max())]
    ax.plot(lims, lims, "r--")
    ax.set_xlabel("Actual AQI")
    ax.set_ylabel("Predicted AQI")
    ax.set_title(f"{name} — Actual vs Predicted")
    fig.savefig(PLOTS_DIR / f"{name}_pred.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
