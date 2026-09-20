import pandas as pd
from src.transform import monthly_state_totals

def test_monthly_totals():
    df = pd.DataFrame({
        "state": ["CA", "CA"],
        "month": ["2024-01-01", "2024-01-01"],
        "consumption_mwh": [100, 50],
    })
    result = monthly_state_totals(df)
    assert result.iloc[0]["consumption_mwh"] == 150
