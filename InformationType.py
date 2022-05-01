# Databricks notebook source
# MAGIC %md
# MAGIC 6º Information Type
# MAGIC In programming, the data type is an important concept. Variables can store data of different types, and different types can do different things. Python has the following built-in data types by default, in these categories:
# MAGIC     
# MAGIC Text Type: str
# MAGIC 
# MAGIC Numeric Types: int, float, complex
# MAGIC 
# MAGIC Sequence Types: list, tuple, range
# MAGIC 
# MAGIC Mapping Type: dict
# MAGIC 
# MAGIC Set Types: set, frozenset
# MAGIC 
# MAGIC Boolean Type: bool
# MAGIC 
# MAGIC Binary Types: bytes, bytearray, memoryview

# COMMAND ----------

# Creeating information type tipos de informações
String = str('Hello world!')
Int = int(100)
Float = float(9.99)
Complex = complex(1j)
List = list( ('Orange', 'Watermello', 'coco') )
Tuple = tuple( ('Banana', 'pinaple', 'kiwi') )
Range = range(10)
Dictionary = dict(nome='Dias', age=23)
Set = set( ('Maça', 'Morango', 'Pera') )
Fronzet = frozenset( ('Maça', 'Morango', 'Pera') )
Boolean = bool(5)
Bytes = bytes(5)
ByteArray = bytearray(5)
Memoryview = memoryview( bytes(5) )

from datetime import datetime
Date = datetime.today().date()

# Showing the values
print( type(String) )
print( type(Int) )
print( type(Float) )
print( type(Complex) )
print( type(List) )
print( type(Tuple) )
print( type(Range) )
print( type(Dictionary) )
print( type(Set) )
print( type(Fronzet) )
print( type(Boleano) )
print( type(Bytes) )
print( type(ByteArray) )
print( type(Memoryview) )
print( type(Date) )
