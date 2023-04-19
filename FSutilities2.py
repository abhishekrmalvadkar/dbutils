# Databricks notebook source
dbutils.fs.cp("dbfs:/FileStore/Order_function.csv","/file_system/folder1")

# COMMAND ----------

dbutils.fs.mv("dbfs:/FileStore/Order_function.csv","/file_system/folder1/duplicate")

# COMMAND ----------

dbutils.fs.ls("/file_system/folder1")

# COMMAND ----------

dbutils.fs.put("dbfs:/FileStore/Order_function.csv","This is from another file",True)
dbutils.fs.head("dbfs:/FileStore/Order_function.csv")

# COMMAND ----------

dbutils.fs.put("dbfs:/FileStore/Hello_world.txt","This is from another file",True)
dbutils.fs.head("dbfs:/FileStore/Hello_world.txt")


# COMMAND ----------

dbutils.fs.rm("dbfs:/FileStore/LOGIN_DETAILS.txt")

# COMMAND ----------

dbutils.notebook.exit("exit")

# COMMAND ----------

dbutils.notebook.run("/April/pyFunctions2",60)

# COMMAND ----------


