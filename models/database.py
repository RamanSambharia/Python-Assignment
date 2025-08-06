import sqlite3

class DatabaseHandler:
    def __init__(self, db_path):
        self.db_path = db_path

    def save_all(self, train_df, ideal_df, test_df, matched_df):
        conn = sqlite3.connect(self.db_path)
        train_df.to_sql("train", conn, if_exists="replace", index=False)
        ideal_df.to_sql("ideal", conn, if_exists="replace", index=False)
        test_df.to_sql("test", conn, if_exists="replace", index=False)
        matched_df.to_sql("matched_test_results", conn, if_exists="replace", index=False)
        conn.close()
