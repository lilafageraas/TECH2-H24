# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:36:49 2024

@author: s14754
"""

#%% Simple program
# Note that there are several cases in which the while loop will never terminate 
# e.g., if the user set both initial savings and annual savings to zero

# Print welcome message
print('='*50)
print('Welcome to the Million Kroner Savings Calculator!')
print('='*50)
print('Calculate how many years it takes to save 1 million NOK\n')

# Prompt user for inputs
initial_savings = float(input('Enter your initial savings amount (in NOK): '))
annual_savings = float(input('Enter your annual savings amount (in NOK): '))
annual_interest_rate = float(input('Enter the annual interest rate (in %): '))

# Initialize variables
current_savings = initial_savings
years = 0

TARGET = 1000000

# Calculate the number of years until the savings account reaches 1 million NOK
while current_savings < TARGET:
    # Add savings and interest to current savings
    current_savings = (current_savings + annual_savings) * (1 + annual_interest_rate/100)
    
    # Increment years
    years = years + 1
    
# Print the result
print(f'\nIt will take {years} years to save 1 million NOK.')
    


#%% Check user-supplied inputs
# This program handles errors by checking that the user supplied inputs are 
# floats and it ensures that the program eventually terminates by requiring 
# the initial savings and interest rate to be positive


# === Welcome Section ===

# Print welcome message
print('='*50)
print('Welcome to the Million Kroner Savings Calculator!')
print('='*50)
print('Calculate how many years it takes to save 1 million NOK\n')


# === Input and Validation Section ===

# Input and validation for initial savings
while True:
    try:
        initial_savings = float(input('Enter your initial savings amount (in NOK): '))
        if initial_savings <= 0:
            print('Please enter a positive number.')
        else:
            break
    except:
        print('Invalid input. Please enter a valid number.')
        
# Input and validation for annual savings
while True:
    try:
        annual_savings = float(input('Enter your annual savings amount (in NOK): '))
        if annual_savings < 0:
            print('Please enter a non-negative number.')
        else:
            break
    except:
        print('Invalid input. Please enter a valid number.')

# Input and validation for annual interest rate
while True:
    try:
        annual_interest_rate = float(input('Enter the annual interest rate (in %): '))
        if annual_interest_rate <= 0:
            print('Please enter a positive number.')
        else:
            break
    except:
        print('Invalid input. Please enter a valid number.')
        
        
# === Calculation Section ===

# Initialize variables
current_savings = initial_savings
years = 0

# Calculate the number of years until the savings account reaches 1 million NOK
while current_savings < 1000000:
    current_savings += annual_savings  # Add savings
    current_savings *= (1 + annual_interest_rate/100)  # Multiply with interest rate    
    years = years + 1  # Increment years
    
    
# === Output Section ===

# Print the result
print(f'\nIt will take {years} years to save 1 million NOK.')
