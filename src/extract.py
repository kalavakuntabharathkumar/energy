import os
import requests
import pandas as pd

def fetch_eia(url=None, api_key=None, start="2024-01", end="2024-12"):
    url = url or os.getenv("EIA_URL")
    api_key = api_key or os.getenv("EIA_API_KEY")
    params = {
        "api_key": api_key,
        "frequency": "monthly",
        "data[0]": "consumption",
        "start": start,
        "end": end,
        "length": 5000,
    }
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return pd.DataFrame(response.json()["response"]["data"])

def load_fixture(path="data/sample_energy.csv"):
    return pd.read_csv(path)
