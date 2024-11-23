#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:08:18 2024

@author: lilapfageraas
"""

#The prisoner’s dilemma is a common example used in game theory. One example of the game is illustrated in the table below.
#Write a program that implements the game:
#Prompt the inputs from prisoner A and B (stay silent or confess) and check that inputs are valid, e.g.:
#Press “1” to stay silent or “2” to confess
#Display the outcome of the game, i.e., prison sentences of prisoner A and B

print("Welcome to the prisoner's dilemma")

choiceA = input('Prisoner A, you are up. Press 1 for "confess" or press 2 to "stay silent":  ')
choiceB = input('Prisoner B, you are up. Press 1 for "confess" or press 2 to "stay silent:  ')

if choiceA in ['1','2'] and choiceB in ['1','2']:
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
