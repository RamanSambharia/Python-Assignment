# 🔍 Function Matching and Analysis with Python

This project implements a complete Python solution to analyze, match, and visualize mathematical functions using CSV data files. The system identifies ideal function fits, evaluates test data, and visualizes everything — storing all results in a local SQLite database.

---

## 📂 Project Overview

You are provided with three CSV files:

- `train.csv`: Contains 4 training functions (`train_func_1` to `train_func_4`) with x-values.
- `ideal.csv`: Contains 50 ideal reference functions (`ideal_func_1` to `ideal_func_50`) with x-values.
- `test.csv`: Contains 2 test functions (`test_func_1`, `test_func_2`) with x-values.

### 🧠 What This Project Does

- **Matches training functions** to their best-fitting ideal functions using least squares minimization.
- **Checks test function values** to see if they fit any of the 4 matched ideal functions.
- **Stores all data and results** in a local SQLite database (`results.db`).
- **Generates visualizations** for:
  - Training vs. matched ideal functions
  - Test values and their deviation thresholds

---

## ✅ Features

| Task                                      | Status                         |
|-------------------------------------------|--------------------------------|
| Load CSV files                            | ✅ via `CSVLoader`             |
| Match 4 training functions to 50 ideal    | ✅ via `IdealFunctionMatcher`  |
| Check test data against ideal matches     | ✅ via `DeviationChecker`      |
| Save everything to SQLite                 | ✅ via `DatabaseHandler`       |
| Plot training vs. ideal functions         | ✅ via `plot_training_vs_ideal()` |
| Plot test matches and deviations          | ✅ via `plot_test_vs_ideal()`  |

---

## 📦 Outputs

- `results.db`: SQLite database storing all datasets and results.
- `training_vs_ideal.html`: Interactive Bokeh plot of training vs matched ideal functions.
- `test_matches.html`: Interactive Bokeh plot of test data vs matched ideal functions with deviation bands.

---

## 🛠 Project Structure

```bash
your-project/
│
├── main.py                  # Orchestrates the full workflow
├── data_loader.py           # Loads CSVs
├── ideal_function_matcher.py # Matches training to ideal functions
├── deviation_checker.py     # Assigns test points based on deviations
├── database_handler.py      # Handles SQLite read/write
├── plotting.py              # Bokeh visualizations
├── tests/                   # Unit tests for components
│   ├── test_matcher.py
│   └── test_deviation.py
└── README.md                # Project documentation

▶️ How to Run
1. Add your data files (train.csv, ideal.csv, test.csv) into the project directory.

2. Install dependencies:

```bash
pip install -r requirements.txt

3. Run the program:

```bash
python main.py

4. Explore the output:

    Open training_vs_ideal.html and test_matches.html in your browser

    Query the results.db SQLite database