#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 23:34:21 2024

@author: lilapfageraas
"""

#initialize empty dictionary
phone_book = {}

#initialize a variable to control the loop
continue_pb = True

while continue_pb:
    name = input('insert the name or press "enter" to finish creating phone book: ')
    if name == '':
        continue_pb = False
    else:
        number = input(f'what number would you like to attach to {name}: ')
        print(f'Added {name} with phone number {number} to the phonebook.\n')
        phone_book[name] = number

for name, number in phone_book.items():
    print (f'{name}: {number}')