from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
MODELS_DIR = ROOT / "models"
RESULTS_DIR = ROOT / "results"
PLOTS_DIR = RESULTS_DIR / "plots"

# Feature columns used for modelling
FEATURE_COLS = [
    "PM2.5", "PM10", "NO2", "SO2", "CO", "O3",
    "temperature", "humidity", "wind_speed",
]
TARGET_COL = "AQI"

RANDOM_STATE = 42
TEST_SIZE = 0.2
