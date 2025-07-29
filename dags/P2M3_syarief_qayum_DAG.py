'''
=================================================
Milestone 3

Nama  : Syarief Qayum Suaib
Batch : FTDS-043-RMT

Milestone 3 aims to evaluate understanding and application of data engineering and analysis tools and concepts learned in Phase 2, including Apache Airflow, Great Expectations, NoSQL databases (Elasticsearch), and data visualization with Kibana. The main task is to build a data pipeline that extracting data from PostgreSQL, cleans and validates it, and loads it into Elasticsearch for visualization using Kibana.
=================================================
'''

# Import necessary libraries
import pandas as pd
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
import psycopg2 as db
from elasticsearch import Elasticsearch, helpers
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)


# Set Default arguments for the DAG
default_args = {
    'owner': 'syariefqs',
    'start_date': dt.datetime(2025, 6, 30, 15, 20, 0) - timedelta(hours=7),  # Adjusted for UTC-8 timezone
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    'P2M3_syarief_qayum_DAG',
    description='ETL process for CSV files with data preprocessing',
    schedule_interval= '10,20,30 9 * * 6',  # Sabtu jam 09:10, 09:20, 09:30 WIB
    default_args=default_args, 
    catchup=False) as dag:

    # Define the start tasks in the DAG
    start = EmptyOperator(task_id='start')

    @task()
    def fetch_data_from_postgres():
        '''
        Fetches data from PostgreSQL and saves it to a CSV file.
        '''
        conn_string = "dbname='airflow' host='postgres' user='airflow' password='airflow' port='5432'"
        conn = db.connect(conn_string)

        df = pd.read_sql("SELECT * FROM public.table_m3", conn)
        df.to_csv('/opt/airflow/data/P2M3_syarief_qayum_data_raw.csv', index=False)
        print("-------Data Saved------")

    @task()
    def preprocess_data():
        '''
        Cleans data from raw CSV and saves cleaned CSV.
        '''
        print("--- Starting Data Cleaning ---")

        # Load the raw CSV file
        df_cleaned = pd.read_csv('/opt/airflow/data/P2M3_syarief_qayum_data_raw.csv', on_bad_lines='skip',encoding='latin-1')
        initial_rows = len(df_cleaned)
        df_cleaned.drop_duplicates(inplace=True)
        print(f"\nRemoved {initial_rows - len(df_cleaned)} duplicate rows.")

        # Clean column names
        df_cleaned.columns = df_cleaned.columns.str.strip().str.replace(' ', '_').str.lower()
        
        # Drop unnecessary columns
        df_cleaned.drop(columns=['license', 'instant_bookable', 'country_code', 'country'], inplace=True, errors='ignore')
        
        # Drop rows with any NaN values
        string_cols_to_fill = ['host_identity_verified', 'host_name', 'country_code', 'last_review', 'house_rules', 'cancellation_policy']
        for col in string_cols_to_fill:
            if col in df_cleaned.columns:
                df_cleaned[col].fillna('N/A', inplace=True)
        
        # Fill specific numeric columns with zero
        num_cols_to_fill_zero = ['reviews_per_month', 'review_rate_number', 'availability_365', 'minimum_nights', 'number_of_reviews']
        for col in num_cols_to_fill_zero:
            if col in df_cleaned.columns:
                df_cleaned[col].fillna(0, inplace=True)

        # Convert specific columns to numeric, handling currency formats      
        currency_cols = ['price', 'service_fee']
        for col in currency_cols:
            if col in df_cleaned.columns and df_cleaned[col].dtype == 'object':
                df_cleaned[col] = df_cleaned[col].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False)
                df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')
                df_cleaned[col].fillna(0, inplace=True)

        # Impute missing values for specific columns
        if 'construction_year' in df_cleaned.columns:
            df_cleaned['construction_year'].fillna('Unknown', inplace=True)
            df_cleaned['construction_year'] = df_cleaned['construction_year'].astype(str)
            df_cleaned['construction_year'].replace('nan', 'Unknown', inplace=True)
        if 'neighbourhood_group' in df_cleaned.columns:
            df_cleaned['neighbourhood_group'].fillna('Unknown', inplace=True)
        if 'neighbourhood' in df_cleaned.columns:
            df_cleaned['neighbourhood'].fillna('Unknown', inplace=True)
        if 'name' in df_cleaned.columns:
            df_cleaned['name'].fillna('No Name', inplace=True)
        if 'lat' in df_cleaned.columns and 'long' in df_cleaned.columns:
            df_cleaned.dropna(subset=['lat', 'long'], inplace=True)
        if 'calculated_host_listings_count' in df_cleaned.columns and 'availability_365' in df_cleaned.columns:
            df_cleaned['calculated_host_listings_count'] = 365 - df_cleaned['availability_365']


        clean_csv_filename = "/opt/airflow/data/P2M3_syarief_qayum_cleaned.csv"
        df_cleaned.to_csv(clean_csv_filename, index=False)
        print(f"Cleaned data saved to {clean_csv_filename}")

    @task()
    def upload_to_elasticsearch():
        '''
        Loads cleaned data from CSV into Elasticsearch.
        '''

        # Connect to Elasticsearch
        es = Elasticsearch("http://elasticsearch:9200")  
        csv_file = "/opt/airflow/data/P2M3_syarief_qayum_cleaned.csv"
        index_name = "project_m3_index"

        # Read the cleaned CSV file
        df = pd.read_csv(csv_file)

        actions = [
            {
            "_index": index_name,
            "_id": row["id"],
            "_source": row.dropna().to_dict()
        }
        for index, row in df.iterrows()
        ]

        # Bulk upload to Elasticsearch
        response = helpers.bulk(es, actions)
        print(response)

    # Define the end task in the DAG
    end = EmptyOperator(task_id='end')

    # Define Airflow task dependencies  
    start >> fetch_data_from_postgres() >> preprocess_data() >> upload_to_elasticsearch() >> end