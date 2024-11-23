# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:51:42 2024

@author: s14754
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

