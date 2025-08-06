import numpy as np


class IdealFunctionMatcher:
    def __init__(self, train_df, ideal_df):
        self.train_df = train_df
        self.ideal_df = ideal_df

    def match_all(self):
        matches = {}
        max_devs = {}
        x = self.train_df['x']
        for col in self.train_df.columns[1:]:
            y_train = self.train_df[col]
            best_match = None
            min_ssd = float('inf')
            max_dev = 0

            for ideal_col in self.ideal_df.columns[1:]:
                y_ideal = self.ideal_df[ideal_col]
                ssd = np.sum((y_train - y_ideal[:len(y_train)]) ** 2)
                if ssd < min_ssd:
                    min_ssd = ssd
                    best_match = ideal_col
                    max_dev = np.max(np.abs(y_train - y_ideal[:len(y_train)]))

            matches[col] = best_match
            max_devs[col] = max_dev
        return matches, max_devs
