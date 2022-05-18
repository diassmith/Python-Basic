# Databricks notebook source
# MAGIC %md
# MAGIC A lambda function is a small anonymous function.
# MAGIC 
# MAGIC A lambda function can take any number of arguments, but it can only have one expression.

# COMMAND ----------

functionSum1 = lambda value: value + 90
functionSum1(10)

# COMMAND ----------

functionSum2 = lambda value1, value2: value1 * value2
functionSum2(10, 100)

# COMMAND ----------

# Lambda Function 
#Checking if the number is even or odd
number = lambda xValue: 'True' if xValue % 2 == 0 else 'False'

print(number( 5 ))
print(number(10))
