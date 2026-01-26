from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world_task():
    print("Hello from Airflow worker!")

with DAG(
    dag_id='demo_hello_world',
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=['demo']
) as dag:

    task = PythonOperator(
        task_id='say_hello',
        python_callable=hello_world_task
    )
