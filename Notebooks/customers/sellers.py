# Databricks notebook source
# DBTITLE 1,Execute notebook connection
# MAGIC %run /Repos/dias_sth@hotmail.com/Olist-Project/Notebooks/connecting_with_Data_Lake

# COMMAND ----------

# DBTITLE 1,Checking the files in bronze layer sellers folder
dbutils.fs.ls("/mnt/bronze/sellers")

# COMMAND ----------

# DBTITLE 1,Reading the sellers files/folder
#read sellers parquet file to dataframe and test it
df_sellers = spark.read.format("parquet")\
.option("inferSchema","true")\
.option("header","true")\
.option("delimiter",",")\
.load("/mnt/bronze/sellers/dbo.olist_sellers_dataset.parquet")

display(df_sellers.limit(5))

# COMMAND ----------

# DBTITLE 1,Checking data schema
df_sellers.printSchema()

# COMMAND ----------

# DBTITLE 1,Importing the libraries
from pyspark.sql import *

from pyspark.sql.functions import *

# COMMAND ----------

# DBTITLE 1,Updating the datatype
df_sellers = df_sellers.withColumn("dtLoad",to_timestamp(date_format("dtLoad", 'yyyy-MM-dd HH:mm:ss.SSSS')))

# COMMAND ----------

# DBTITLE 1,Checking schema
df_sellers.printSchema()

# COMMAND ----------

display(df_sellers)

# COMMAND ----------

# DBTITLE 1,Writting file in data lake
df_sellers.write.mode("overwrite").parquet("/mnt/silver/sellers")
