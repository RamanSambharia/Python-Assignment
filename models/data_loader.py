import pandas as pd
from utils.exceptions import FileLoadingError


class CSVLoader:
    def __init__(self, train_path, ideal_path, test_path):
        self.train_path = train_path
        self.ideal_path = ideal_path
        self.test_path = test_path

    def load_all(self):
        try:
            train_df = pd.read_csv(self.train_path)
            ideal_df = pd.read_csv(self.ideal_path)
            test_df = pd.read_csv(self.test_path)
            return train_df, ideal_df, test_df
        except Exception as e:
            raise FileLoadingError(f"Failed to load CSV files: {str(e)}")
