- #
- @see https://github.com/epahomov/docker-spark.git
- docker run -it epahomov/docker-spark:lightweighted /spark/bin/pyspark
- sc.parallelize(range(0, 10)).count()
- docker run -it epahomov/docker-spark:lightweighted /spark/bin/spark-shell
