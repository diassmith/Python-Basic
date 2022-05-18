# Databricks notebook source
# MAGIC %md
# MAGIC Python While Loop is used to execute a block of statements repeatedly until a certain condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed. While loop falls under the category of undefined iteration. Indefinite iteration means that the number of times the loop runs is not specified explicitly in advance.
# MAGIC 
# MAGIC while expression:
# MAGIC 
# MAGIC loop

# COMMAND ----------

# While
Loop = 0

while Loop <= 10:
  print( Loop )
  Loop += 1

# COMMAND ----------

# While
Loop = 0

while Loop <= 10:
  print( Loop )
  Loop += 1

  if Loop == 5:
    
    for c in range(10):
      print(c)

# COMMAND ----------

# While True
import random

while True:

  Player1 = random.randint(0, 6)
  Player2 = random.randint(5, 10)

  if Player1 > Player2:
    print(Player1, '-', Player2, 'Finaly !!!!!!!!!!!')
    break

  else:
    print(Player1, '-', Player2)
