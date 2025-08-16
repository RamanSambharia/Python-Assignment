# 🔍 Function Matching and Analysis with Python

This project implements a complete Python solution to analyze, match, and visualize mathematical functions using CSV data files. It identifies ideal function fits, evaluates test data, and visualizes results — storing everything in a local SQLite database.

---

## 📂 Project Overview

You are provided with three CSV files:

- `train.csv`: Contains 4 training functions (`train_func_1` to `train_func_4`) with x-values.
- `ideal.csv`: Contains 50 ideal reference functions (`ideal_func_1` to `ideal_func_50`) with x-values.
- `test.csv`: Contains 2 test functions (`test_func_1`, `test_func_2`) with x-values.

### 🧠 What This Project Does

- Matches each training function to its best-fitting ideal function using least squares.
- For each test point, checks if it can be matched to any of the 4 selected ideal functions based on a deviation threshold.
- Saves all data, matches, and results to a SQLite database (`results.db`).
- Generates interactive plots using Bokeh:
  - Training vs. Ideal functions
  - Test matches with deviation overlays

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
- `training_vs_ideal.html`: Interactive plot of training vs matched ideal functions.
- `test_matches.html`: Interactive plot of test points and their deviations.

---

## 🛠 Project Structure

```bash
project/
│
├── main.py                    # Runs the complete pipeline
├── data_loader.py             
├── ideal_function_matcher.py  
├── deviation_checker.py       
├── database_handler.py        
├── plotting.py               
├── tests/                     # Unit tests
│   ├── test_matcher.py
│   └── test_deviation.py
├── data/                     # csv files
│   ├── ideal.csv
│   ├── test.csv
│   └── train.csv
├── models/                     
│   ├── base.py
│   ├── data_loader.py        # CSV loading
│   ├── database.py           # SQLite integration
│   ├── deviation.py          # Test point deviation logic
│   ├── matcher.py            # Function matching logic
│   └── plotter.py            # Bokeh visualizations
└── README.md


