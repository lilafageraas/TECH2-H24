# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:08:22 2024

@author: s14754
"""

# Initialize an empty dictionary to store the phonebook
phonebook = {}

# Initialize a variable to control the loop
continue_input = True  

while continue_input:
    # Prompt the user for a name
    name = input('Enter a name (or press "enter" to exit): ')

    if name == '':
        continue_input = False  # Set the condition to False to terminate the loop
    else:
        # Prompt the user for a phone number
        phone_number = input(f'Enter the phone number for {name}: ')

        # Add the name and phone number to the phonebook
        phonebook[name] = phone_number

        print(f'Added {name} with phone number {phone_number} to the phonebook.\n')



# Print the final phonebook
print('\nFinal Phonebook:')
for name, number in phonebook.items():
    print(f'{name}: {number}')






