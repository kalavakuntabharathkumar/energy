import sqlite3
import pandas as pd

def load_sqlite(df: pd.DataFrame, db_path="energy.db"):
    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA journal_mode=WAL")
        df.to_sql("monthly_consumption", conn, if_exists="replace", index=False)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_state_month ON monthly_consumption(state, month)")
        conn.commit()

def query_state(db_path="energy.db", state=None):
    with sqlite3.connect(db_path) as conn:
        if state:
            return pd.read_sql_query(
                "SELECT * FROM monthly_consumption WHERE state = ? ORDER BY month",
                conn, params=[state]
            )
        return pd.read_sql_query("SELECT * FROM monthly_consumption ORDER BY state, month", conn)
