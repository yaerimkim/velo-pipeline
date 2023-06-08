from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 1),
    'retries': 0,
}

test_dag = DAG(
    'kbo-velocity',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)

# Define the BashOperator task
start = BashOperator(
    task_id='start',
    bash_command="""
        
    """,
    dag=test_dag
)

classify_broadcast_channels = BashOperator(
    task_id='broadcast_channels',
    bash_command="""

    """,
    dag=test_dag
)

PTS_data = BashOperator(
    task_id='PTS_data',
    bash_command="""

    """,
    dag=test_dag
)

TRACKMAN_data = BashOperator(
    task_id='TRACKMAN_data',
    bash_command="""

    """,
    dag=test_dag
)

PTS_avg = BashOperator(
    task_id='PTS_avg',
    bash_command="""

    """,
    dag=test_dag
)

TRACKMAN_avg = BashOperator(
    task_id='TRACKMAN_avg',
    bash_command="""

    """,
    dag=test_dag
)

RAW_data = BashOperator(
    task_id='RAW_data',
    bash_command="""

    """,
    dag=test_dag
)

data_analysis = BashOperator(
    task_id='data_analysis',
    bash_command="""

    """,
    dag=test_dag
)

end = BashOperator(
    task_id='end',
    bash_command="""

    """,
    dag=test_dag
)

# Set task dependencies

start >> classify_broadcast_channels 
classify_broadcast_channels >> [TRACKMAN_data, PTS_data]
TRACKMAN_data >> TRACKMAN_avg
PTS_data >> PTS_avg
[PTS_avg, TRACKMAN_avg] >> RAW_data >> data_analysis >> end


