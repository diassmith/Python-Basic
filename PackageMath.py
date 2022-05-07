# Databricks notebook source
# MAGIC %md
# MAGIC Python has a set of built-in math functions, including an extensive math module, which allows you to perform math tasks on numbers.

# COMMAND ----------

import math

# No using Math

# Min and Max
Tupla = (10, 15, 5, 8, 20)
print( min(Tupla) )
print( max(Tupla) )
# ABS  return the absolute value(positive) from number.
print( abs(-7.25) )

# Return the pow (it's like 3 * 3 * 3 * 3)
print( pow(3, 4) )

# Square root
Root_Square = math.sqrt( 81 )
print( Root_Square )

# Rounding

# Rouding a number to up more than close to next
print( math.ceil(1.4) )

# Rounding a number to down
print( math.floor(1.4) )

# return the PI number
print( math.pi )
