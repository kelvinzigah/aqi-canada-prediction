# AQI Canada Prediction

Predicting next-day Air Quality Health Index (AQHI) values for the Montreal Trudeau Airport region using machine learning.

The AQHI is a Canadian government scale (1 to 10+) that measures how harmful outdoor air is to human health. It is calculated from three pollutants: O3, NO2, and PM2.5. We trained five regression models on historical NAPS pollutant data (2020 to 2024) to predict what the next day AQHI will be.

## Results

| Model | RMSE | MAE | MAPE |
|---|---|---|---|
| Baseline Linear Regression | 0.407 | 0.313 | 14.2% |
| Linear Regression with Lag Features | 0.401 | 0.307 | 13.7% |
| Lasso Regression | 0.406 | 0.312 | 14.0% |
| Decision Tree | 0.440 | 0.337 | 14.9% |
| **Random Forest** | **0.404** | **0.303** | **13.6%** |

Random Forest was the best performing model with an average error of 0.30 AQHI points on the 2024 test set.



## Project Structure

```
aqi-canada-prediction/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_evaluation.ipynb
├── src/
│   ├── config.py
│   ├── load_data.py
│   ├── preprocessing.py
│   ├── features.py
│   ├── models.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
├── models/
│   └── saved_model.pkl
├── results/
│   ├── metrics_table.csv
│   └── plots/
├── demo/
│   └── predict_sample.py
├── report/
│   └── final_report.pdf
├── requirements.txt
└── README.md
```

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/kelvinzigah/aqi-canada-prediction.git
cd aqi-canada-prediction
```

**2. Create the virtual environment**
```bash
python -m venv .venv
```

**3. Activate it**

- Windows (PowerShell):
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- Mac/Linux:
  ```bash
  source .venv/bin/activate
  ```

**4. Install dependencies**
```bash
pip install -r requirements.txt
```

**5. Verify**
```bash
pip list
```

You should see packages like `pandas`, `scikit-learn`, `jupyter`, etc.

> To deactivate the venv when done: run `deactivate`

## Workflow

Run notebooks in order:

1. `01_eda.ipynb` — Exploratory data analysis
2. `02_preprocessing.ipynb` — Cleaning and feature engineering
3. `03_model_training.ipynb` — Train and tune models
4. `04_evaluation.ipynb` — Evaluate and compare results

For a quick prediction, run `demo/predict_sample.py`.

## Course

COEN 330 — Summer 2026
