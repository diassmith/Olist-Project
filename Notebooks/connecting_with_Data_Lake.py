# Databricks notebook source
# MAGIC %md
# MAGIC # Mounting Data lakes

# COMMAND ----------

# DBTITLE 1,Doing connection with data lake
spark.conf.set(
    "fs.azure.account.key.adlsolist.dfs.core.windows.net",
    dbutils.secrets.get(scope="olistScope",key="datalakekey"))

# COMMAND ----------

# DBTITLE 1,Authenticating in Data Lake storage
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": dbutils.secrets.get(scope="olistScope",key="clientIdKey"),  
          "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="olistScope",key="adbkey"),
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/"+dbutils.secrets.get(scope="olistScope", key="directoryIdKey")+"/oauth2/token"}


# COMMAND ----------

# DBTITLE 1,Creating the 3 layers
#setting the layers that you would like create
layers = ["bronze", "silver", "gold"]
for layer in layers:
    try:
        dbutils.fs.mount(
            source = "abfss://"+layer+"@adlsolist.dfs.core.windows.net",
            mount_point = "/mnt/"+layer+"/",
            extra_configs = configs)
    except:
            print("")

# COMMAND ----------

# DBTITLE 1,checking the mnt
# MAGIC %fs ls /mnt/

# COMMAND ----------

# DBTITLE 1,removing
#dbutils.fs.unmount("/mnt/landing")
#dbutils.fs.unmount("/mnt/processing")
#dbutils.fs.unmount("/mnt/curated")

# COMMAND ----------

# DBTITLE 1,Checking the landing
dbutils.fs.ls("/mnt/bronze")
