# from airflow import DAG
# from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
# from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator



# Constants
SOURCE_DIR = "/Users/mac_dee/Documents/Dee/code/python_100din/__Projects/Data_Platform/USE_CASES/cost_international_education"
# SOURCE_DIR = "/opt/airflow/plugins"
TARGET_TABLE = "INTERNATIONAL_EDUCATION"

# Simple cache to remember last update
MOD_TIME_TRACKER = '/tmp/edu_file_last_mod.txt'


def load_to_snowflake():
    # Direct connection
    conn = snowflake.connector.connect(

        user='admin',
        password='UYF92ARdPqybkyk',
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
        warehouse='COMPUTE_WH',
        database='SNOWFLAKE_LEARNING_DB',
        schema='AWS_UNLOAD'
    )

    # Truncate table for overwrite (or skip this to append)
    cur = conn.cursor()
    cur.execute(f"TRUNCATE TABLE IF EXISTS {TARGET_TABLE}")
    cur.close()
    df.columns = [col.upper() for col in df.columns]

    # Load
    success, nchunks, nrows, _ = write_pandas(conn, df, TARGET_TABLE)
    print(f"Loaded {nrows} rows into {TARGET_TABLE}")

    # Save last mod time
    with open(MOD_TIME_TRACKER, 'w') as f:
        f.write(str(last_mod_time))

    conn.close()


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

if __name__ == "__main__":
    load_to_snowflake()
    etl_to_snowflake()
    # create_table