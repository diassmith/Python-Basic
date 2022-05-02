# Databricks notebook source
import datetime

# Today
Today = datetime.datetime.today().date()
print( f'Today is: {Today} \n' )

# Setting a Date
Date = datetime.date(2020, 10, 1)
print( f'Building a Date {Date} \n' )

# Acessing the attributes from Date
Year = Date.year
Month = Date.month
Day = Date.day
print(f'Today is {Day} of month {Month} of year {Year} \n')

# Operation
Interval = Date - Today
print(f'It\'s been {Interval} days \n' )

# fixing format
NewFormat = Today.strftime('%d/%m/%y')
print( f'Today is(Format): {NewFormat} \n' )

# Increase the days or decrease
print( f'Increase 30 days, {Today + datetime.timedelta(days = 30)}' )
print( f'Decrease 30 days, {Today - datetime.timedelta(days = 30)}' )
