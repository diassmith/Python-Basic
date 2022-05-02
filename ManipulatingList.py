# Databricks notebook source
# MAGIC %md
# MAGIC Manipulating Lists
# MAGIC Lists are used to store multiple items in a single variable.
# MAGIC 
# MAGIC Lists are one of the 4 built-in Python data types used to store collections of data, the other 3 are Tuple , Set and Dictionary , all of which have different qualities and uses.<p>
# MAGIC Most used commands:
# MAGIC   
# MAGIC 1. append() - To add an item to the end of the list
# MAGIC   
# MAGIC 2. len() - Calculate the size of the list
# MAGIC   
# MAGIC 3. [  ] - Access positions
# MAGIC   
# MAGIC 4. del() - Delete an element
# MAGIC   
# MAGIC 5. clear() - Clear the list
# MAGIC   
# MAGIC 6. insert() - To insert a list item at a specified index
# MAGIC   
# MAGIC 7. extend() - Append elements from another list to the current list
# MAGIC   
# MAGIC 8. remove() - Removes the specified item
# MAGIC   
# MAGIC 9. pop() - Removes the specified index.
# MAGIC   
# MAGIC 10. sort() - Sort the values
# MAGIC   
# MAGIC 11. copy() - Makes a copy of the List
# MAGIC   
# MAGIC 12. index() - Returns the index of the list element

# COMMAND ----------

# Manipuling datas in List
ListEmpty = []
print('List initial:', ListEmpty, '\n' )

# Inserting values in the List
ListEmpty.append(1)
ListEmpty.append(2)
ListEmpty.append(3)
print('List after append:', ListEmpty, '\n' )

# Size of list
print('List contain:', len(ListEmpty), 'elements', '\n' )

# Getting an item from List
print('Acessing the first element:', ListEmpty[0] )
print('Acessing  the second element:', ListEmpty[1] )
print('Acessing  the last element:', ListEmpty[-1] )
print('Accessing a period:', ListEmpty[0:2], '\n' )

# Removing value from the List
del ListEmpty[1]
print('After romove the item [1]:', ListEmpty, '\n' )

# Cleaning the List
print('After clear the List:', ListEmpty.clear(), '\n' )

# Inserting an value with position
ListInsert = ['Position 1', 'Position 2', 'Position 3']
ListInsert.insert( 0, 'Position 4' )
print( 'After insert the item Position 4 in the position [0]:',ListInsert, '\n' )

# Inserting a List in other List
ListInsert_01 = ['Position 1', 'Position 2', 'Position 3']
ListInsert_02 = ['Position 4', 'Position 5', 'Position 6']
ListInsert_01.extend( ListInsert_02 )
print( 'ListInsert_01', ListInsert_01, '\n' )
print( 'ListInsert_02', ListInsert_02, '\n' )

# Removing itens by the name
ListInsert_01.remove('Position 6')
print( 'After romove by the name:', ListInsert_01, '\n' )

# Removing itens using the index
ListInsert_01.pop(0)
print( 'Removing itens using the index 0', ListInsert_01, '\n' )

# order a list
Alphabetical_List = ['Z', 'C', 'A', 'B', 'L']
Alphabetical_List.sort()
print( Alphabetical_List, '\n' )

# Order a list like reverse
Alphabetical_List.sort( reverse=True )
print( Alphabetical_List, '\n' )

# Copy a list
Alphabetical_List_02 = Alphabetical_List.copy()
print( Alphabetical_List_02, '\n' )

# Identify a index from element in the list
print( Alphabetical_List_02.index('L'), '\n' )
