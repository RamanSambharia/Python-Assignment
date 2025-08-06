from models.data_loader import CSVLoader
from models.matcher import IdealFunctionMatcher
from models.deviation import DeviationChecker
from models.database import DatabaseHandler
from models.plotter import Plotter


def main():
    # Load data
    loader = CSVLoader("data/train.csv", "data/ideal.csv", "data/test.csv")
    train_df, ideal_df, test_df = loader.load_all()

    # Match training functions with ideal functions
    matcher = IdealFunctionMatcher(train_df, ideal_df)
    best_matches, max_devs = matcher.match_all()

    # Check test data against matched ideal functions
    checker = DeviationChecker(
        test_df=test_df,
        matches=best_matches,
        ideal_df=ideal_df,
        max_devs=max_devs
    )
    matched_test_df = checker.check_all()

    # Store everything in SQLite
    db = DatabaseHandler("results.db")
    db.save_all(train_df, ideal_df, test_df, matched_test_df)

    # Visualizations
    plotter = Plotter()
    plotter.plot_training_vs_ideal(train_df, best_matches, ideal_df)
    plotter.plot_test_vs_ideal(matched_test_df)


if __name__ == "__main__":
    main()
