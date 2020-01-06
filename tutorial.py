from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from email_script import send_email
from datetime import datetime, timedelta
import smtplib, ssl

default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    'tutorial3', default_args=default_args, schedule_interval=timedelta(days=1))

t4 = PythonOperator(
    dag=dag,
    task_id='task_send_email',
    provide_context=False,
    python_callable=send_email,
    )



