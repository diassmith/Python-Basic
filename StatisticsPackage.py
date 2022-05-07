# Databricks notebook source
# MAGIC %md
# MAGIC Functions to calculate mathematical statistics from numerical data and interact with lists

# COMMAND ----------

# Importing the Statistics to work in the lists
import statistics

# Getting the average 
Average = statistics.mean( [10, 20, 30, 40, 55] )
print(f'The average is: {Average} \n')

Median = statistics.median( [20, 15, 35, 41, 65] )
print(f'The Median is: {Median} \n')

Mode = statistics.mode( [10, 25, 35, 45, 70] )
print(f'The mode is: {Mode}')
