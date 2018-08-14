#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyspark
from pyspark.sql import SQLContext
from pyspark.sql import HiveContext
from pyspark.sql import SparkSession

#开头重载编码
#解决Python写入文件编码问题(UnicodeEncodeError: 'ascii' codec can't encode characters in...)
import sys
reload(sys)
sys.setdefaultencoding('utf8')

###
# http://spark.apache.org/docs/latest/sql-programming-guide.html#hive-tables
###

# from pyspark.context import SparkContext
# from pyspark.sql.session import SparkSession

# from pyspark import SparkConf, SparkContext
# conf = SparkConf().setMaster("local").setAppName("helloSpark")
# sc = SparkContext(conf == conf)
sc = pyspark.SparkContext()
log4jLogger = sc._jvm.org.apache.log4j
logger = log4jLogger.LogManager.getLogger(__name__)
logger.warn("pyspark script logger initialized,Hello")

sqlContext = SQLContext(sc)
hiveContext = HiveContext(sc)
sparkSession = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()
logger.warn('sc getted!')
logger.warn('sql_ctx getted!')
logger.warn('hive_ctx getted!')
logger.warn('SparkSession getted!')

# """
# region test begin
# """
# df = sparkSession.read.json("/app/resources/people.json")
# print(df.printSchema())
# logger.warn(df.show(3))
# df.registerTempTable('tmp_people')
# sqlContext.sql("select * from tmp_people limit 2").show()


# df = sparkSession.read.json("/app/resources/sex.json")
# print(df.printSchema())
# logger.warn(df.show(3))
# df.registerTempTable('tmp_sex')
# sqlContext.sql("select * from tmp_sex limit 2").show()

# logger.warn('join begin!')
# res_df = sqlContext.sql("select tmp_sex.uid,tmp_sex.sex,tmp_people.name from tmp_people left join tmp_sex on tmp_people.uid=tmp_sex.uid")
# logger.warn('join done!')

# # # 保存到本地csv 
# res_df.show()
# # # @see https://stackoverflow.com/questions/31385363/how-to-export-a-table-dataframe-in-pyspark-to-csv
# # # res_df.write.csv('/app/resources/res.csv', header = 'true')
# # # res_df.coalesce(1).write.csv('/app/resources/res3.csv', header = 'true')
# # res_df.repartition(1).write.format('com.databricks.spark.csv').save("/app/resources/res2.csv",header = 'true')

# # # pip install pandas
# # import pandas
# # res_df.toPandas().to_csv('/app/resources/res2.csv')
# """
# region end
# """

# region begin
# read mysql as df
"""
need set:
spark.driver.extraClassPath 
"""
tag_results = sqlContext.read.format("jdbc").options(
    url="jdbc:mysql://xiangke.local:3306/hsin?zeroDateTimeBehavior=convertToNull",
    driver = "com.mysql.jdbc.Driver",
    dbtable = "judge_result",
    user="hadoop",
    password="hadoop").load()
print(tag_results.printSchema())
# tag_results.show()
# spark_session.read.format("jdbc").options(...).load() 
# endregion

# sc.parallelize(range(0, 100000)).count()

logger.error("Done!")