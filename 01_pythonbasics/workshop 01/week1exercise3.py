#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:32:13 2024

@author: lilapfageraas
"""
import random

print ('welcome to the random number generator')

lower_b = int(input('enter a lower bound: '))
print()
upper_b = int(input('enter an upper bound:' ))

rand_num = random.randint(lower_b, upper_b)
print()
print(f'your random draw is {rand_num}')

    
    