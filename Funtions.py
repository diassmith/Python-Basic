# Databricks notebook source
# MAGIC %md
# MAGIC A function is a block of code that is only executed when called.
# MAGIC 
# MAGIC You can pass data, known as parameters, to a function.
# MAGIC 
# MAGIC A function can return data as a result.

# COMMAND ----------

#creating function without parameters
def welcome():
    print('python welcome function')

#run funtion welcome
welcome()


# COMMAND ----------

#creating fuction with parameters
def sum(value1, value2):
    sum = value1 + value2
    print(sum)

#run function sum
sum(10,10)
    

# COMMAND ----------

#importing random package
import random

#start loop
for loop in range(0,10):
    
    #creating variable that will be set in parameters
    vl1 = random.randint(1,10)
    vl2  = random.randint(1,10)
    
    #print which round is
    print(loop)
    #print the random value
    print(vl1,vl2)
    #run the function sum
    sum(vl1,vl2)
    print("=================")
