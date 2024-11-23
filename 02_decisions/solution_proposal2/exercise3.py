# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 13:36:29 2024

@author: s14754
"""

print('This program will convert temperatures (Fahrenheit/Celsius)')
print('Enter "F" to convert from Fahrenheit to Celsius')
print('Enter "C" to convert from Celsius to Fahrenheit\n')

# Prompt user for selection
choice = input('Enter selection: ')

# Check that selection is valid
if choice.upper() in ('F', 'C'):
    
    # Prompt user for temperature
    temp = input('Enter temperature to convert: ')

    # Check that temperature is a number
    try:
        # Convert temperature to float
        temp = float(temp)   
        
        # Convert Fahrenheit -> Celsius
        if choice.upper() == 'F':
            converted_temp = (temp - 32) * 5 / 9
            print(f'\n{temp} degrees Fahrenheit equals {converted_temp:.1f} degrees Celsius.')

        # Convert Celsius -> Fahrenheit
        else:
            converted_temp = (9 / 5) * temp + 32
            print(f'\n{temp} degrees Celsius equals {converted_temp:.1f} degrees Fahrenheit.')
        
    # Print that temperature is not a number
    except:
        print('\nINVALID INPUT')
        print('Temperature must be a number')
    
# Print that selection is invalid
else:
    print('\nINVALID INPUT')
    print('You must select "F" or "C"')





