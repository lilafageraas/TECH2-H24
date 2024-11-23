#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:36:01 2024

@author: lilapfageraas
"""


import random

# Print welcome message
print('*'*49)
print('**** Welcome to the Random Number Generator! ****')
print('*'*49)
print('This program draws a random integer between an upper and lower bound.\n')

# Prompt user for upper and lower bounds
lower = int(input('Please enter a lower bound: '))
upper = int(input('Please enter an upper bound: '))

# Draw random number
rand_num = random.randint(a = lower, b = upper)
print(f'\nYou asked for a random number between {lower} and {upper}.')
print(f'Your random draw is... {rand_num}!')