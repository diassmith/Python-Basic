# Databricks notebook source
# MAGIC %md
# MAGIC Input Command
# MAGIC 
# MAGIC The input() function receives as a parameter a string that will be shown as an aid to the user, usually informing him what kind of data the program is expecting to receive.
# MAGIC 
# MAGIC input()

# COMMAND ----------

# input Command
# Send a moment information
Name = input('What\'s your name?')
Age = input('How old are you? ')

print('Your name is:', Name)
print('Your age is:', Age)
