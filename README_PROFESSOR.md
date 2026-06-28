# AQI Canada Prediction — Setup & Run Guide (for grading)

**Course:** COEN 330 — Summer 2026
**Project:** Predicting the next-day Air Quality Health Index (AQHI) for the Montreal–Trudeau Airport region using machine learning.

This guide explains how to set up the project from the provided zip file and run the full pipeline. Everything needed to run the project is already included in the zip — the raw data, the cleaned datasets, and a pre-trained model — so no external downloads are required.

---

## 1. Prerequisites

- **Python 3.10 or newer** installed and on your PATH (check with `python --version`).
- About 200 MB of free disk space (the raw air-quality data is included).

No internet connection is needed after installing the Python packages in Step 3.

---

## 2. Unzip and open a terminal in the project folder

1. Extract the zip file to any location.
2. Open a terminal **inside the extracted folder** (the folder that contains `requirements.txt` and the `src/` directory).

All commands below assume your terminal is in this project root folder.

---

## 3. Create a virtual environment and install dependencies

**Create the environment:**
```bash
python -m venv .venv
```

**Activate it:**

- **Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
  > If PowerShell blocks the activation script, run this once, then activate again:
  > `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

- **Windows (Command Prompt):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

- **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

**Install the required packages:**
```bash
pip install -r requirements.txt
```

This installs pandas, scikit-learn, statsmodels, matplotlib, jupyter, and the other libraries the project uses.

---

## 4. Running the project

There are two ways to run it. **Option A (notebooks)** is the recommended way to review the full workflow and see the plots. **Option B (scripts)** is the fastest way to reproduce the model results from the command line.

The cleaned datasets are already included, so you can run either option immediately.

### Option A — Run the notebooks (recommended)

1. Launch Jupyter from the project root:
   ```bash
   jupyter notebook
   ```
   (Or open the folder in VS Code and open the notebooks there.)

2. **Important:** make sure the notebook is using the `.venv` you created.
   - In VS Code, click the kernel selector in the top-right and choose the `.venv` interpreter.
   - In Jupyter, the default kernel will work as long as you launched it from the activated environment.

3. Open and run the notebooks **in this order**, using **Kernel → Restart Kernel and Run All Cells** for each:

   | Notebook | Purpose |
   |---|---|
   | `notebooks/01_eda.ipynb` | Exploratory data analysis (correlation, ACF/PACF, trends) |
   | `notebooks/03_model_training.ipynb` | Trains and compares all six models |
   | `notebooks/04_evaluation.ipynb` | Evaluation plots and results comparison |

   > Note: `03_model_training.ipynb` takes about **30 seconds** on the ARIMA step, which refits the model 355 times for a rolling one-step-ahead forecast. This is expected, not a freeze.

### Option B — Run the training pipeline from the command line

The training script uses local imports, so it must be run **from inside the `src/` folder**:

```bash
cd src
python train.py
```

This will:
- Load the cleaned dataset,
- Train and tune all six models (Baseline Linear Regression, Linear Regression with lag features, Lasso, Decision Tree, Random Forest, and ARIMA),
- Print the MSE / MAE / RMSE / MAPE for each model,
- Save the trained Random Forest model to `models/saved_model.pkl`.

The results table is also written to `results/metrics_table.csv`.

### Demo: predict on unseen 2019 data

A small demo applies the saved Random Forest model to held-out 2019 data. Run it **from the project root**:

```bash
python demo/predict_sample.py
```

It loads `models/saved_model.pkl`, predicts the next-day AQHI on the 2019 demo dataset, and prints the resulting error metrics.

---

## 5. What is already included in the zip

| Path | Contents |
|---|---|
| `data/raw/` | Original NAPS hourly air-quality data (2019–2024) |
| `data/processed/air_quality_project_dataset.csv` | Cleaned daily dataset (2020–2024) used for training |
| `data/processed/air_quality_project_dataset_Demo.csv` | Cleaned 2019 dataset used by the demo |
| `src/` | All source code (preprocessing, features, models, training, evaluation) |
| `notebooks/` | EDA, model training, and evaluation notebooks |
| `models/saved_model.pkl` | Pre-trained Random Forest model |
| `results/` | Metrics table and result plots |

> **Note:** The data preprocessing step (`src/preprocessing.py`) has already been run, and its output is included in `data/processed/`. You do **not** need to run it to reproduce the results — running the notebooks or `train.py` above is sufficient.

---

## 6. Troubleshooting

- **`ModuleNotFoundError` when running a notebook** — the kernel is not using the `.venv`. Select the `.venv` interpreter (see Step 4, Option A) and re-run.
- **`No module named 'statsmodels'` (or similar)** — the packages were not installed into the active environment. Make sure the `.venv` is activated (Step 3) and re-run `pip install -r requirements.txt`.
- **PowerShell error like `Unexpected token ... in expression or statement`** — this happens if a quoted file path is run directly. Use the plain `python <script>` commands shown above, or prefix a quoted executable path with the call operator `&`.
- **Changes to a `src/*.py` file not taking effect in a notebook** — restart the kernel (Kernel → Restart) so the updated module is re-imported.
