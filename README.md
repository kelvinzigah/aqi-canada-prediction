# AQI Canada Prediction

Predicting Air Quality Index (AQI) values across Canadian cities using machine learning.

Goal: Our project goal is to train various machine learning models to accurately predict **future** AQHI values in the Montreal, Trudeau airport region. This will be done by using past historical measurements of pollutants and AQHI values at specific timeframes. 



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
