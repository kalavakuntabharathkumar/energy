from .extract import load_fixture
from .validate import validate_and_clean
from .transform import monthly_state_totals
from .load import load_sqlite
from .visualize import plot_state

def run():
    raw = load_fixture()
    clean, rejected = validate_and_clean(raw)
    totals = monthly_state_totals(clean)
    load_sqlite(totals)
    if not totals.empty:
        plot_state(totals, totals.iloc[0]["state"])
    print(f"Loaded {len(totals)} rows; rejected {rejected} malformed rows.")

if __name__ == "__main__":
    run()
