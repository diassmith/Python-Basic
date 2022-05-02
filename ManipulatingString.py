# Databricks notebook source
# MAGIC %md
# MAGIC String Manipulation
# MAGIC 
# MAGIC A data type widely used in everyday life are strings, or strings of characters (or sequences of characters). The string data type, or str as it is called in Python, has a number of useful operations associated with it. These operations make Python a very suitable language for text manipulation. Some commonly used functions:
# MAGIC     
# MAGIC 1. replace() - change the string for another string.  
# MAGIC 2. startswith() - return if the word start with something (boolen)
# MAGIC 3. endswith() - return if the word end with something (boolen)
# MAGIC 4. count() - count the letters that there are in a string
# MAGIC 5. capitalize() - capitalize the first letter from the word
# MAGIC 6. isdigit() - checking if the string has numbers
# MAGIC 7. isalnum() - checking if he string is alphanumeric (just have letters and Numbers).
# MAGIC 8. upper() - trasform all letters on lowercase
# MAGIC 9. lower() - transform all letter on lowercase
# MAGIC 10. find () - search something in string
# MAGIC 11. strip() - Remove the spaces before and in the final of the string
# MAGIC 12. split() - lets you split the variable content according to specified conditions example: ","

# COMMAND ----------

# Defining a string.
String = 'Hello Python!'
print( String )
print( type( String ) )
print( len( String ) )

# concat
print( String + ' I\'m specializing in Python...' )

# change a substring for other thing.
Substituir = String.replace('Hello', 'Hey')
print( Substituir )

# The string start with "Hello"?
print( "start with: " + str(String.startswith('Hello')) )

# The string end with "Python"?
print( String.endswith('Pyhton') )

# Count how much letter appear in the string?
print("How much letters O appear in String: " + str(String.count('o')) )

# Capitalize the first letter of the first word
String02 = 'dias guilherme'
print( String02.capitalize() )

# Checking if the strig has numbers
String03 = '2468'
String04 = '2468ABC'
print( String03.isdigit() )
print( String04.isdigit() )

# Checking if he string is alphanumeric (just have letters and Numbers).
print( '246abc'.isalnum() )

# Capitalize everything 
print( String.upper() )

# Tranform all in lowercase
print( String.lower() )

# Search something in string
print("found the string in this position: " + str( String.find('!')) )

# Remove the spaces before and in the final of the string
String05 =' Hello Python! '
print( String05.strip() )

# lets you split the variable content according to specified conditions example: ","
String06 ='String 1 nota 10, String 2 nota 9, String 3 nota 8 '
print( String06.split(',') )
