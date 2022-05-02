# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC 9- String Slicing
# MAGIC Strings are lists of bytes representing characters.
# MAGIC 
# MAGIC We can access their positions using Brackets
# MAGIC 
# MAGIC String [Start Position: End Position]

# COMMAND ----------

# Strings
String = 'Working with Python'
print( "type"+ str(type(String)) )
print( "tamaho:" + str(len(String)) )

print( String[0] )
print( String[6] )
print( String[-1] )
print( String[-10:] )
print( String[0:10] )
