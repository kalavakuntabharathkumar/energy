from datetime import datetime
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from src.pipeline import run

with DAG(
    dag_id="energy_consumption_etl",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    PythonOperator(task_id="extract_validate_transform_load", python_callable=run)
