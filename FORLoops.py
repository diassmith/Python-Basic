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

for position, P in enumerate( List_Country ):
  print( position / 4 , P )

# COMMAND ----------

# for + LISTa + IF + RANGE
List_Numeric = [ Numero for Numero in range(1, 100, 5) ]
Store = []

for x in List_Numeric:

  if x % 2 == 0:
    Store.append( x )

print( Store )

from pandas import DataFrame
print( DataFrame(Armazenar) )
