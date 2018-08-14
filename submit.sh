#!/bin/bash
export SPARK_HOME=/spark

if [ -f "${SPARK_APPLICATION_PYTHON_LOCATION}" ]; then
        echo "Submit application ${SPARK_APPLICATION_PYTHON_LOCATION} to Spark master ${SPARK_MASTER_URL}"
else
    export SPARK_APPLICATION_PYTHON_LOCATION=/app/app.py
    echo "Submit default application /app/app.py"
fi


if [ -f "${SPARK_APPLICATION_JAR_LOCATION}" ]; then
        echo "Submit application ${SPARK_APPLICATION_JAR_LOCATION} to Spark master ${SPARK_MASTER_URL}"
else
    export SPARK_APPLICATION_JAR_LOCATION=/app/jars/mysql-connector-java-5.1.4.jar
    echo "Submit default application ${SPARK_APPLICATION_JAR_LOCATION}"
fi

/spark/bin/spark-submit \
    --jars ${SPARK_APPLICATION_JAR_LOCATION} \
    ${SPARK_APPLICATION_PYTHON_LOCATION}
    # --master ${SPARK_MASTER_URL} \


