# Databricks notebook source
dbutils.widgets.combobox(name="animals",defaultValue="dog",choices=["dog","lion","cat","tiger"],label="Select the animal")

# COMMAND ----------

dbutils.widgets.dropdown(name="cities",defaultValue="Pune", choices=["Bengaluru","Mumbai","Pune","Delhi"],label="Select the city")

# COMMAND ----------

dbutils.widgets.multiselect(name="states",defaultValue="karnataka", choices=["karnataka","maharashtra","AP","Delhi"],label="Select the state")

# COMMAND ----------

dbutils.widgets.text(name="Name",defaultValue="Abhishek R Malvadkar", label="Full Name")

# COMMAND ----------

dbutils.widgets.get("Name")

# COMMAND ----------

dbutils.widgets.getArgument("Name","Please enter valid widget Name")

# COMMAND ----------

dbutils.widgets.remove("Nameeee")

# COMMAND ----------


