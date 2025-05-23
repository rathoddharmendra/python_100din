from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
import logging


# Constants
SOURCE_DIR = "/opt/airflow/plugins"
TARGET_TABLE = "INTERNATIONAL_EDUCATION"

# Simple cache to remember last update
MOD_TIME_TRACKER = '/tmp/edu_file_last_mod.txt'

def load_to_snowflake():
    # Direct connection
    conn = snowflake.connector.connect(

        user='admin',
        password='',
        account='NIKUIUN-DF48053',
        warehouse='COMPUTE_WH',
        database='SNOWFLAKE_LEARNING_DB',
        schema='AWS_UNLOAD',
        role='ACCOUNTADMIN'
    )

    cursor = conn.cursor()

    # Example: create a table

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS INTERNATIONAL_EDUCATION (
            Country STRING,
            City STRING,
            University STRING,
            Program STRING,
            Level STRING,
            Duration_Years INT,
            Tuition_USD INT,
            Living_Cost_Index FLOAT,
            Rent_USD INT,
            Visa_Fee_USD INT,
            Insurance_USD INT,
            Exchange_Rate FLOAT
        );
    """)

    # Example: load data
    # You could insert rows here or use PUT + COPY INTO (for bulk CSV load)
    # cursor.execute("INSERT INTO international_education VALUES (...)")

    cursor.close()
    conn.close()


def get_latest_file(path:str):
    files = [f for f in os.listdir(path) if f.endswith('.csv')]
    if not files:
        return None
    files = sorted(files, key=lambda f: os.path.getmtime(os.path.join(path, f)), reverse=True)
    return os.path.join(path, files[0])

def etl_to_snowflake():
    file_path = get_latest_file(SOURCE_DIR)
    if not file_path:
        print("No file found.")
        return

    # Check for modification
    last_mod_time = os.path.getmtime(file_path)
    if os.path.exists(MOD_TIME_TRACKER):
        with open(MOD_TIME_TRACKER, 'r') as f:
            cached_time = float(f.read().strip())
        if cached_time == last_mod_time:
            print("No update found.")
            return

    # Extract and transform
    df = pd.read_csv(file_path)

    # Load to Snowflake
    conn = snowflake.connector.connect(
        user='admin',
        password='UYF92ARdPqybkyk',
        account='NIKUIUN-DF48053',
        warehouse='SNOWFLAKE_LEARNING_WH',
        database='SNOWFLAKE_LEARNING_DB',
        schema='AWS_UNLOAD'
    )

    # Truncate table for overwrite (or skip this to append)
    cur = conn.cursor()
    # cur.execute(f"TRUNCATE TABLE IF EXISTS {TARGET_TABLE}")
    cur.close()

    # Load
    df.columns = [col.upper() for col in df.columns]
    success, nchunks, nrows, _ = write_pandas(conn, df, TARGET_TABLE)
    print(f"Loaded {nrows} rows into {TARGET_TABLE}")
    logging.info(f"Loaded {nrows} rows into {TARGET_TABLE}")

    # Save last mod time
    with open(MOD_TIME_TRACKER, 'w') as f:
        f.write(str(last_mod_time))
        print(last_mod_time)
        logging.info(f"Saved last modification time: {last_mod_time}")
    conn.close()

# Airflow DAG definition
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retry_delay': timedelta(minutes=1),
    'start_date': datetime(2025, 5, 8),
    'retries': 1,
}

dag = DAG(
    'mac_etl_to_snowflake',
    default_args=default_args,
    schedule_interval='*/5 * * * *',  # every 1 minute
    catchup=False,
    max_active_runs=2
)

# create_table = SnowflakeOperator(
#     task_id='create_table',
#     sql="""
#     CREATE TABLE IF NOT EXISTS international_education (
#         Country STRING,
#         City STRING,
#         University STRING,
#         Program STRING,	
#         Level STRING,	
#         Duration_Years INT,	
#         Tuition_USD INT,
#         Living_Cost_Index FLOAT,
#         Rent_USD INT,	
#         Visa_Fee_USD INT,	
#         Insurance_USD FLOAT
#     );
#     """,
#     snowflake_conn_id='your_snowflake_conn',
#     dag=dag,
# )

def check_data_quality(**kwargs):
    df = kwargs['ti'].xcom_pull(task_ids='load_data_task')
    
    if df is None or df.empty:
        raise ValueError("DataFrame is empty!")
    
    if df['Country'].isnull().any():
        raise ValueError("Missing values found in 'Country' column!")

    print("✅ Data quality checks passed.")

# quality_check = PythonOperator(
#     task_id='data_quality_check',
#     python_callable=check_data_quality,
#     provide_context=True,
#     dag=dag,
# )


create_table = PythonOperator(
    task_id='create_table',
    python_callable=load_to_snowflake,
    dag=dag,
)
run_etl = PythonOperator(
    task_id='etl_task',
    python_callable=etl_to_snowflake,
    dag=dag,
)

create_table >> run_etl
