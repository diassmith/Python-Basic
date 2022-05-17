# Databricks notebook source
# MAGIC %md
# MAGIC Python's For loop is used for sequential traversal, i.e. it is used to iterate over an iterable like string, tuple, list, etc. It falls under the defined iteration category. Defined iterations means that the number of repetitions is specified explicitly in advance.
# MAGIC 
# MAGIC for variable in object:

# COMMAND ----------

# For [ Loop ]

for x in range(10):
  print( x * 2  ) 

# COMMAND ----------

# For [ Loop ]
# 1 until 10 
for x in range(1,10):
  print( x * 1  ) 

# COMMAND ----------

# For [ Loop ]
#range 0 until 100 but print 5 in 5 number
for x in range(0, 100, 5):
  print( x * 1  ) 

# COMMAND ----------


