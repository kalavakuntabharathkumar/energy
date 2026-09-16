import pandas as pd

def monthly_state_totals(df: pd.DataFrame):
    return (
        df.assign(month=pd.to_datetime(df["month"]))
          .groupby(["state", "month"], as_index=False)["consumption_mwh"]
          .sum()
          .sort_values(["state", "month"])
    )
