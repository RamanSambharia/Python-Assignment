import unittest
import pandas as pd
from models.matcher import IdealFunctionMatcher


class TestIdealFunctionMatcher(unittest.TestCase):
    def setUp(self):
        self.train_df = pd.DataFrame({
            "x": [0, 1, 2],
            "train_func_1": [1, 2, 3]
        })

        self.ideal_df = pd.DataFrame({
            "x": [0, 1, 2],
            "ideal_func_1": [1, 2, 3],
            "ideal_func_2": [1.1, 2.1, 3.1]
        })

    def test_best_match(self):
        matcher = IdealFunctionMatcher(self.train_df, self.ideal_df)
        matches, _ = matcher.match_all()
        self.assertEqual(matches["train_func_1"], "ideal_func_1")


if __name__ == '__main__':
    unittest.main()
