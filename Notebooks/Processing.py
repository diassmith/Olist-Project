# Databricks notebook source
# MAGIC %run /Repos/dias_sth@hotmail.com/Olist-Project/Notebooks/Reading_files_from_landing

# COMMAND ----------

# DBTITLE 1,Creating TempView
df_customers.createOrReplaceTempView("customers_tempview")

# COMMAND ----------

# DBTITLE 1,Select tempview
# MAGIC %sql
# MAGIC SELECT * FROM customers_tempview

# COMMAND ----------

# DBTITLE 1,Transforming tempview in DataFrame
df_customers_tempview = spark.table('customers_tempview')
display(df_customers_tempview)

# COMMAND ----------

# DBTITLE 1,Getting the distinct value in state
df_customers_tempview.select('customer_state').distinct().show()

# COMMAND ----------

# DBTITLE 1,Doing filter to get just 1 State
from pyspark.sql.functions import col
df_customers_tempview = df_customers_tempview.filter(col("customer_state") == "RJ")


# COMMAND ----------

display(df_customers_tempview)

# COMMAND ----------

# DBTITLE 1,Writting Filtered Parquet to Processing layer into Data lake
df_customers_tempview.write.mode("overwrite").parquet("/mnt/processing/customers_RJ.parquet")

# COMMAND ----------

# DBTITLE 1,Reading the parquet files from Processing zone 
df_customers_parquet = spark.read.parquet("/mnt/processing/customers_RJ.parquet")
display(df_customers_parquet)

# COMMAND ----------

# DBTITLE 1,Creating a tempview from parquet file
df_customers_parquet.createOrReplaceTempView("CustomersParquetTable")
custparkSQL = spark.sql("select * from CustomersParquetTable")
display(custparkSQL)
