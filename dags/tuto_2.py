"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.bigquery_check_operator import BigQueryCheckOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2019, 7, 25),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("tutorial-2", default_args=default_args, schedule_interval=timedelta(1))

t1 = BashOperator(task_id="print_date", bash_command="date", dag=dag)

t2 = BigQueryCheckOperator(
        task_id='bq_check',
        sql='''
        #standardSQL
        SELECT
          count(*)
        FROM
          `bigquery-public-data.bls.cpi_u`
        ''',
        use_legacy_sql=False,
        dag=dag
    )
