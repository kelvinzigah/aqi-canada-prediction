# AQI Canada Prediction

Predicting Air Quality Index (AQI) values across Canadian cities using machine learning.

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

```bash
pip install -r requirements.txt
```

## Workflow

Run notebooks in order:

1. `01_eda.ipynb` — Exploratory data analysis
2. `02_preprocessing.ipynb` — Cleaning and feature engineering
3. `03_model_training.ipynb` — Train and tune models
4. `04_evaluation.ipynb` — Evaluate and compare results

For a quick prediction, run `demo/predict_sample.py`.

## Course

COEN 330 — Summer 2026
