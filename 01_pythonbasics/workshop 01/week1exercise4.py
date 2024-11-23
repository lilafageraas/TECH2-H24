#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:25:09 2024

@author: lilapfageraas
"""


print('welcome to the temperature converter')

temp_F = input('insert your temperature in fahrenheit: ')
temp_C = 5/9*(float(temp_F)-32)
print(f'the temperature in degrees celcius is {int(temp_C)}')