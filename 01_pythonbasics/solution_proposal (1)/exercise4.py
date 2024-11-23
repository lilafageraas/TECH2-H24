# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:10:25 2024

@author: s14754
"""

# Print welcome message
print('*'*40)
print('**** Temperature Conversion Program ****')
print('*'*40)
print('This program converts from Fahrenheit to Celsius\n')

# Prompt user for input and convert to float
fahren = float(input('Enter temperature to convert: '))

# Calculate temperature conversion
celsius = (fahren-32) * 5 / 9
    
# Print conversion
print(f'\n{fahren} degree(s) Fahrenheit is {celsius:.0f} degree(s) Celsius.')



