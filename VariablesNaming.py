# Databricks notebook source
# MAGIC %md
# MAGIC 5º Variable naming
# MAGIC We can name variables and data types in several ways:
# MAGIC 
# MAGIC Declare variables on a single command line;
# MAGIC 
# MAGIC Assign a value to several variables;
# MAGIC 
# MAGIC Declare using a List;
# MAGIC 
# MAGIC Combine variables;
# MAGIC 
# MAGIC Operate with mathematical operators;
# MAGIC 
# MAGIC Many others.

# COMMAND ----------

# Variable naming | Ex 1
Apple, Banana, Orange = 1, 2, 3
print( Apple, Banana, Orange, '\n' )

# Variable naming | Ex 2
Morango = Uva = Kiwi = 100
print( Morango, Uva, Kiwi, '\n' )

# Variable naming  | Ex 3
# creating list
Carros = ['BMW', 'TESLA', 'HYNDAI']

# naming variables with list
Marca_01, Marca_02, Marca_03 = Carros
print( Marca_03, '\n' )

# Combine variables | Ex 1
Name = 'Guilherme'
LastName = 'Dias'
Nome_Completo = Name + ' ' + LastName
print( Nome_Completo, '\n' )

# Combinando Variaveis | Exemplo 2
Dolar = 5.50
tax = 0.20
NetValue = Dolar - ( Dolar * tax )
print( NetValue )

# Investiments
investing = 1000
interest_rate = float('10.5')

print(investing * interest_rate)

value_total = (investing * interest_rate) + investing

print(value_total)
