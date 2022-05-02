# Databricks notebook source
# MAGIC %md
# MAGIC Data Types
# MAGIC 
# MAGIC Lists - Are created using [ ] (Brackets)
# MAGIC 
# MAGIC Tuples - Are created using ( ) (Parenthesis)
# MAGIC 
# MAGIC Dictionaries - Are created using { } (braces)
# MAGIC 
# MAGIC These data types can receive any type of information, including Arithmetic Operations

# COMMAND ----------

# Datatype
List_Ex_1 = [2, 4, 6, 8, 10]
List_Ex_2 = ['Name', 'House', 'Apple', 1, 4]
List_Ex_3 = [1, 'House', True, False]

print(List_Ex_2)

# COMMAND ----------

# Tuples are immutable (Does not change)
Tuple_Ex_1 = ( 2, 4, 6, 8 )
Tuple_Ex_2 = ( 'Dias', 'Guilherme', 6 )

print(Tuple_Ex_2)

# COMMAND ----------

# Dictionary are for organizing the data (Key, Value)
Dictionary = { 'Name':"Dias", 'Year':2022 }
print(Dictionary)
