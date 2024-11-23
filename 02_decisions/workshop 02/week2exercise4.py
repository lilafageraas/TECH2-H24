#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:36:46 2024

@author: lilapfageraas
"""

import random

print('welcome to the temperature converter')

initial_type_T = input('choose C to convert from celcius, F to convert from fahrenheit, and K to convert from kelvin: ')
print()
converted_type_T = input('choose C to convert to celcius, F to convert to fahrenheit, and K to convert to kelvin: ')
print()
initial_temp = input('what temperature would you like to convert? ')

if initial_type_T == 'C':
    if converted_type_T == 'F':
        converted_temp = (9/5)*(float(initial_temp) + 32)
        print()
        print(f"{initial_temp} in degrees celcius is equal to {converted_temp} fahrenheit")
    elif converted_type_T == 'K':
        converted_temp = float(initial_temp) + 273.15
        print()
        print(f"{initial_temp} in degrees celcius is equal to {converted_temp} kelvin")
elif initial_type_T == 'F':
    if converted_type_T == 'C':
        converted_temp = (5/9)*(int(initial_temp) - 32)
        print()
        print(f"{initial_temp} in degrees fahrenheit is equal to {converted_temp} celcius")
    elif converted_type_T == 'K':
        converted_temp = (initial_temp-32)*5/9 + 237.15
        print()
        print(f"{initial_temp} in degrees fahrenheit is equal to {converted_temp} kelvin")
elif initial_type_T == 'K':
    if converted_temp == 'C':
        converted_temp = initial_temp - 237.15
        print()
        print(f"{initial_temp} in kelvin is equal to {converted_temp} celcius")
    elif converted_temp == 'F':
        converted_temp = (9/5 * (K - 237.15)) +32
        print(f"{initial_temp} in kelvin is equal to {converted_temp} fahrenheit")
        