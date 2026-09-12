# Automated ETL Pipeline for US State-Level Energy Consumption Analytics

Airflow-oriented ETL project using Python, Pandas, SQLite, Matplotlib, and the EIA Open Data API.

## Pipeline

1. Extract EIA-compatible JSON data.
2. Validate required fields and numeric values.
3. Correct/drop malformed records using explicit validation rules.
4. Load normalized SQLite tables.
5. Produce a monthly state-level trend chart.

The extractor uses an API key from `EIA_API_KEY`. For repeatable local tests, the project also includes a sample JSON fixture.
