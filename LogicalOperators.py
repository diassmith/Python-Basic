# Databricks notebook source
# MAGIC %md
# MAGIC Logical Operators
# MAGIC 
# MAGIC Logical operators are used to combine conditional statements:
# MAGIC 
# MAGIC and (Returns True if both statements are true)
# MAGIC 
# MAGIC or (Returns True if one of the statements is true)

# COMMAND ----------

# Logical Operators - Pt 2
And = 'and'
Ou = 'or'
Negação = 'not'

print('100 is greater than 70 and 70 is greater than 100:', 100 > 70 and 70 > 100 )
print('100 is greater than 70 e 70 is less than  100:', 100 > 70 and 70 < 100 )
print('100 is greater than 70 ou 70 is less than  100:', 100 == 70 or 70 == 100 )
print('100 is greater than 70 ou 70 is less than  100:', 100 > 70 or 70> 100 )
