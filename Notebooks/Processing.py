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

from pyspark.sql.functions import col
df_customers_tempview = df_customers_tempview.filter(col("customer_state") == "RJ")


# COMMAND ----------

display(df_customers_tempview)
