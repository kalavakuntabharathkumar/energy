import pandas as pd

REQUIRED = ["state", "month", "consumption_mwh"]

def validate_and_clean(df: pd.DataFrame):
    frame = df.copy()
    missing = [c for c in REQUIRED if c not in frame.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    frame["consumption_mwh"] = pd.to_numeric(frame["consumption_mwh"], errors="coerce")
    frame["month"] = pd.to_datetime(frame["month"], errors="coerce")
    frame["state"] = frame["state"].astype("string").str.strip()
    frame.loc[frame["consumption_mwh"] < 0, "consumption_mwh"] = pd.NA
    before = len(frame)
    frame = frame.dropna(subset=REQUIRED)
    return frame, before - len(frame)
