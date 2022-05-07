# Databricks notebook source
# import random
import random
 
# List number
List_Numbers = [10, 20, 30, 40, 50, 60,70,80,90,100]
print(f'O number choose: {random.choice(List_Numbers)} \n')
 
# raffle a letter
Palavra = 'Python'
print(f'The letter drawn: {random.choice(Palavra)} \n')

# Random number between 0 and 1
random_number = random.random()
print(f'The number crated is: {random_number} \n')

random_number1 = random.randint(0, 10)
print(f'random number between 1 e 10 foi: {random_number1}')
