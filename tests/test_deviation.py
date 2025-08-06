import unittest
import pandas as pd
from models.deviation import DeviationChecker


class TestDeviationChecker(unittest.TestCase):
    def setUp(self):
        self.test_df = pd.DataFrame({
            "x": [1],
            "test_func_1": [2.0]
        })
        self.ideal_df = pd.DataFrame({
            "x": [1],
            "ideal_func_1": [2.0]
        })

        # Matches test_func_1 to ideal_func_1 via train_func_1
        self.matches = {"train_func_1": "ideal_func_1"}
        self.max_devs = {"train_func_1": 0.1}

    def test_deviation_within_bounds(self):
        checker = DeviationChecker(
            test_df=self.test_df,
            matches=self.matches,
            ideal_df=self.ideal_df,
            max_devs=self.max_devs
        )
        result_df = checker.check_all()
        self.assertFalse(result_df.empty)
        self.assertEqual(result_df.iloc[0]["function"], "ideal_func_1")


if __name__ == '__main__':
    unittest.main()
