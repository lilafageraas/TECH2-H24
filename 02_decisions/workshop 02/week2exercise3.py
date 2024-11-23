#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:18:55 2024

@author: lilapfageraas
"""

print('welcome to the temperature converter')

#prompt the user for the selected conversion and the temperature to convert
initial_T = input('press "F" to select fahrenheit to celcius and "C" to select celcius to fahrenheit: ')
print()
temp = input('what temperature do you want to convert? ')

if initial_T in ['F', 'C'] and temp.isdigit:
    if initial_T == 'F':
        converted_T = (5/9)*(float(temp) - 32)
        print(f'the temperature is {converted_T:.2f} degrees celcius')
    else:
        converted_T = (9/5)*(float(temp) + 32)
        print(f'the temperature is {converted_T:.2f} degrees fahrenheit')
else:
    print('the input is not valid, you must choose F or C and the temperature must be a number')
    

