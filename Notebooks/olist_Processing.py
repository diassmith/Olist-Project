# Databricks notebook source
# MAGIC %md
# MAGIC # Mounting Data lakes

# COMMAND ----------

# DBTITLE 1,Authenticating in Data Lake storage
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": dbutils.secrets.get(scope="olistScope",key="clientIdKey"),  
          "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="olistScope",key="adbkey"),
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/"+dbutils.secrets.get(scope="olistScope", key="directoryIdKey")+"/oauth2/token"}


# COMMAND ----------

layers = ["landing", "processing", "curated"]
for layer in layers:
    try:
        dbutils.fs.mount(
            source = "abfss://"+layer+"@adlsolist.dfs.core.windows.net",
            mount_point = "/mnt/"+layer+"/",
            extra_configs = configs)
    except:
            print("")

# COMMAND ----------

# MAGIC %fs ls /mnt/

# COMMAND ----------

dbutils.fs.unmount("/mnt/")

# COMMAND ----------

dbutils.fs.ls("/mnt/landing")
