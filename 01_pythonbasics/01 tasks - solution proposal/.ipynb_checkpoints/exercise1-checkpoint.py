# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:29:52 2024

@author: s14754
"""

# Welcome message
print('This program divides two integer values.\n')

# Prompt user for input and convert to integer
num1 = int(input('Enter the first integer: '))
num2 = int(input('Enter the second integer: '))

# Store division in new variable
res = num1 / num2

# Display result with two decimals
print(f'{num1} / {num2} = {res:.1f}')

# Alternatively, pass the calculation directly to the f-string
#print(f'{num1} / {num2} = {num1 / num2:.2f}')