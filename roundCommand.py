# Databricks notebook source
# MAGIC %md
# MAGIC 7º Round command
# MAGIC When working with floating numbers, we can round the value using a native Python command
# MAGIC 
# MAGIC round( value, number of places)

# COMMAND ----------

# Round Command
# Round will around values

Value = 10.1230234

print( round( Value, 1 ) )
print( round( Value, 2 ) )
print( round( Value, 3 ) )
print( round( Value, 5 ) )
