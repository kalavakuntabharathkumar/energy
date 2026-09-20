import pandas as pd
from src.validate import validate_and_clean

def test_invalid_rows_are_removed():
    df = pd.DataFrame({
        "state": ["CA", "TX"],
        "month": ["2024-01-01", "bad"],
        "consumption_mwh": ["100", "oops"],
    })
    clean, rejected = validate_and_clean(df)
    assert len(clean) == 1
    assert rejected == 1
    assert clean.iloc[0]["state"] == "CA"
