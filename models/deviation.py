import pandas as pd
import numpy as np


class DeviationChecker:
    def __init__(self, *, test_df, matches, ideal_df, max_devs):
        self.test_df = test_df
        self.matches = matches
        self.ideal_df = ideal_df
        self.max_devs = max_devs

    def check_all(self):
        result = []

        for test_col in self.test_df.columns[1:]:  # skip 'x'
            train_col = test_col.replace("test", "train")
            ideal_func = self.matches.get(train_col)
            if not ideal_func:
                continue

            for index, row in self.test_df.iterrows():
                x_val = row["x"]
                y_val = row[test_col]
                ideal_y_vals = self.ideal_df[self.ideal_df["x"] == x_val][ideal_func].values

                if len(ideal_y_vals) == 0:
                    continue

                ideal_y = ideal_y_vals[0]
                deviation = abs(y_val - ideal_y)
                max_allowed = self.max_devs.get(train_col, float('inf')) * (2 ** 0.5)

                if deviation <= max_allowed:
                    result.append({
                        "x": x_val,
                        "y": y_val,
                        "function": ideal_func,
                        "deviation": deviation
                    })

        return pd.DataFrame(result)
