# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:03:01 2024

@author: s14754
"""

# Dict to map selection to temperature scale
d = {
     'F' : 'Fahrenheit',
     'C' : 'Celsius',
     'K' : 'Kelvin'
     }


print('This program converts temperatures between Fahrenheit/Celsius/Kelvin\n')

# Prompt user for temperature and convert to float
temp = float(input('Enter temperature: '))

# Prompt user for temperature scale to convert from and to
fromScale = input('Is this in (F)ahrenheit, (C)elsius or (K)elvin?: ').upper()
toScale = input('Convert to (F)ahrenheit, (C)elsius or (K)elvin?: ').upper()

# Converting from Fahrenheit...
if fromScale == 'F':
    # ...to Celsius
    if toScale == 'C':
        converted_temp = (temp - 32) * 5/9
    # ...to Kelvin
    elif toScale == 'K':
        converted_temp = (temp - 32) * 5/9 + 273.15
    # ...to Fahrenheit
    else:
        converted_temp = temp
        
# Converting from Celsius...
elif fromScale == 'C':
    # ...to Fahrneheit
    if toScale == 'F':
        converted_temp = (9/5 * temp) + 32
    # ...to Kelvin
    elif toScale == 'K':
        converted_temp = temp + 273.15
    # ...to Celsius
    else:
        converted_temp = temp
        
# Converting from Kelvin...   
else:
    # ...to Fahrenheit
    if toScale == 'F':
        converted_temp = (9/5 * (temp - 273.15)) + 32
    # ...to Celsius
    elif toScale == 'C':
        converted_temp = temp - 273.15
    # ...to Kelvin
    else:
        converted_temp = temp 
    
# Print conversion
print(f'{temp:.1f} degrees {d[fromScale]} equals {converted_temp:.1f} degrees {d[toScale]}')

