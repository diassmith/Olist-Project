# Databricks notebook source
# DBTITLE 1,Execute the connection notebook
# MAGIC %run /Repos/dias_sth@hotmail.com/Olist-Project/Notebooks/connecting_with_Data_Lake

# COMMAND ----------

# DBTITLE 1,Checking mount
dbutils.fs.ls("/mnt/bronze/customer")

# COMMAND ----------

# DBTITLE 1,Reading the customers file
#read customer parquet files to dataframe and test it
df_customers = spark.read.format("parquet")\
.option("inferSchema","true")\
.option("header","true")\
.option("delimiter",",")\
.load("/mnt/bronze/customer/dbo.olist_customers_dataset.parquet")

display(df_customers.limit(5))

# COMMAND ----------

# DBTITLE 1,checking the Data Schema
df_customers.printSchema()

# COMMAND ----------

# DBTITLE 1,Importing Libraries
from pyspark.sql import *

from pyspark.sql.functions import to_timestamp, date_format

# COMMAND ----------

# DBTITLE 1,Change the datatype and Format
df_customers = df_customers.withColumn("dtLoad",to_timestamp(date_format("dtLoad", 'yyyy-MM-dd HH:mm:ss.SSSS')))

# COMMAND ----------

# DBTITLE 1,Checking the schema after update
df_customers.printSchema()

# COMMAND ----------

# DBTITLE 1,Check the data
display(df_customers)

# COMMAND ----------

# DBTITLE 1,Writting file in data lake
df_customers.write.mode("overwrite").parquet("/mnt/silver/customers")
