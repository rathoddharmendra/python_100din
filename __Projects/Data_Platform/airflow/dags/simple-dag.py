from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("Hello from Python task!")

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    dag_id='simple_test_dag',
    schedule_interval='@daily',  # runs daily
    default_args=default_args,
    catchup=False,
    tags=['example'],
) as dag:

    bash_task = BashOperator(
        task_id='print_hello_bash',
        bash_command='echo "Hello from Bash task!"'
    )

    python_task = PythonOperator(
        task_id='print_hello_python',
        python_callable=say_hello
    )

    bash_task >> python_task
