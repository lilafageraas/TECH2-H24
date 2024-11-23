#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:42:52 2024

@author: lilapfageraas
"""

print("Welcome to the prisoner's dilemma")

d = {
     '1' : 'confess'
     '2' : 'stay silent'
     }

choiceA = input('Prisoner A, you are up. Press 1 for "confess" or press 2 to "stay silent":  ')
choiceB = input('Prisoner B, you are up. Press 1 for "confess" or press 2 to "stay silent:  ')

if choiceA in d.keys() and choiceB in d.kys:
print(f'prisoner A chooses to {d[choiceA]} and prisoner B chooses to {d[choiceB]}')
    if choiceA=='1' and choiceB=='1':
        print('you will both serve 2 years')
    elif choiceA=='1' and choiceB=='2':
        print('prisoner A goes free, prisoner B serves 3 years')
    elif choiceA=='2' and choiceB=='1':
        print('prisoner A serves 3 years, prisoner B goes free')
    elif choiceA=='2' and choiceB=='2':
        print('you will both serve 1 year')
else:
    print('invalid selection!')
