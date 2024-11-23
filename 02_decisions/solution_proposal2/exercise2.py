# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 13:06:04 2024

@author: s14754
"""

# Dict that maps numbers to choices
d = {
     '1' : 'confess',
     '2' : 'stay silent'
     }


# Print welcome message
print('**********************************')
print("Welcome to the Prisoner's Dilemma.")
print('**********************************')

# Prompt user for inputs
choiceA = input('\nPrisoner A, you are up.\nPress 1 for "confess", press 2 for "stay silent": ')
choiceB = input('\nPrisoner B, you are up.\nPress 1 for "confess", press 2 for "stay silent": ')

# Check that choices are valid
if choiceA in d.keys() and choiceB in d.keys():
    
    # Print choices using dict
    print(f'\nPrisoner A chose to {d[choiceA]} and prisoner B chose to {d[choiceB]}.\n')

    if choiceA == '1' and choiceB == '1':
        print('You both get 2 years.')
        
    elif choiceA == '1' and choiceB == '2':
        print('Prisoner A gets 3 years, prisoner B goes free.')
        
    elif choiceA == '2' and choiceB == '1':
        print('Prisoner A goes free, prisoner B gets 3 years.')
    
    elif choiceA == '2' and choiceB == '2':
        print('You both get 1 year.')
   
# Print that choices are invalid
else:
    print('\nInvalid inputs!')
    print('You can only press "1" or "2"')