# Databricks notebook source
# Importing Lib
import time

print('This print has been fast!')
time.sleep(2.5)
print('This print has been happened after 2.5 seconds \n')

# Get the Local now
Now = time.localtime()
print( type(Now) )
print( Now )
print( time.strftime('%m/%d/%Y, %H:%M:%S', Now ), '\n' )

# Convert string to Time
TimeText = '21 June, 2018'
Conversion = time.strptime(TimeText, '%d %B, %Y')
print('converson', Conversion)
