# Databricks notebook source
print ("hello world")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "blah"

# COMMAND ----------

# MAGIC %run ./includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

files = dbutils.fs.ls("/databricks-datasets/")
print(files)

# COMMAND ----------

display(files)
