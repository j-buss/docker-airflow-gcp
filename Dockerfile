FROM puckel/docker-airflow

ARG AIRFLOW_USER_HOME=/usr/local/airflow
COPY config/airflow.cfg ${AIRFLOW_USER_HOME}/airflow.cfg
COPY config/requirements.txt /requirements.txt

COPY script/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["webserver"]
