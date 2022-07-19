# Databricks notebook source
# MAGIC %md
# MAGIC # Readings CSVs in Landing Data Lake to DataFrames

# COMMAND ----------

# DBTITLE 1,Run the connection notebook
# MAGIC %run /Repos/dias_sth@hotmail.com/Olist-Project/Notebooks/connecting_with_Data_Lake

# COMMAND ----------

# DBTITLE 1,Reading Customers csv
#read customer csv to dataframe and test it
df_customers = spark.read.format("csv")\
.option("inferSchema","true")\
.option("header","true")\
.option("delimiter",",")\
.load("/mnt/landing/dbo.olist_customers_dataset.csv")

display(df_customers.limit(5))

# COMMAND ----------

# DBTITLE 1,Reading geolocation csv
df_geolocation = spark.read.format("csv")\
.option("inferSchema", "true")\
.option("header","true")\
.option("delimiter",",")\
.load("/mnt/landing/dbo.olist_geolocation_dataset.csv")

display(df_geolocation.limit(5))

# COMMAND ----------

# DBTITLE 1,Reading order_items csv
df_order_items = spark.read.format("csv")\
.option("inferSchema", "true")\
.option("header","true")\
.option("delimiter",",")\
.load("/mnt/landing/dbo.olist_order_items_dataset.csv")

display(df_order_items.limit(5))

# COMMAND ----------

# DBTITLE 1,Reading Order_payments csv
df_order_payments = spark.read.format("csv")\
.option("inferSchema", "true")\
.option("header","true")\
.option("delimiter",",")\
.load("/mnt/landing/dbo.olist_order_payments_dataset.csv")

display(df_order_payments.limit(5))

# COMMAND ----------

# DBTITLE 1,Reading Order_reviews csv
df_order_reviews = spark.read.format("csv")\
.option("inferSchema", "true")\
.option("header","true")\
.option("delimiter",",")\
.load("/mnt/landing/dbo.olist_order_reviews_dataset.csv")

display(df_order_reviews.limit(5))

# COMMAND ----------

# DBTITLE 1,Reading Orders csv
df_orders = spark.read.format("csv")\
.option("inferSchema", "true")\
.option("header","true")\
.option("delimiter",",")\
.load("/mnt/landing/dbo.olist_orders_dataset.csv")

display(df_orders.limit(5))

# COMMAND ----------

# DBTITLE 1,Reading Sellers csv
df_sellers = spark.read.format("csv")\
.option("inferSchema", "true")\
.option("header","true")\
.option("delimiter",",")\
.load("/mnt/landing/dbo.olist_sellers_dataset.csv")

display(df_sellers.limit(5))

# COMMAND ----------

# DBTITLE 1,Reading Product csv
df_product_category_name_translation = spark.read.format("csv")\
.option("inferSchema", "true")\
.option("header","true")\
.option("delimiter",",")\
.load("/mnt/landing/dbo.olist_product_category_name_translation.csv")

display(df_product_category_name_translation.limit(5))
