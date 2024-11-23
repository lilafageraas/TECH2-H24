# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:42:17 2024

@author: s14754
"""

import random

#%% Alternative 1: regular for loop  

# Print welcome message
print('*' * 47)
print('**** Welcome to the Random Code Generator! ****')
print('*' * 47)
print('This program generates a random code of digits between 0 and 9.\n')

# Prompt user for the length of the code
code_len = input('Enter the length of the code: ')

# Initialize an empty list to store the generated code
code_lst = []

# Check if the user input is a digit
if code_len.isdigit():
    code_len = int(code_len)  # Convert input to an integer

    # Generate random digits and append them to the code list
    for i in range(code_len):
        num = random.randint(0, 9)  # Generate a random digit between 0 and 9
        code_lst.append(num)

    # Print the generated code
    print(f'Your code is: {code_lst}')

else:
    # Handle invalid input
    print('Invalid input. Code length must be a non-negative integer.')
    
    

#%% Alternative 2: list comprehension
    
# Print welcome message
print('*'*47)
print('**** Welcome to the Random Code Generator! ****')
print('*'*47)
print('This program generates a random code of digits between 0 and 9.\n')

# Prompt user for the length of the code
code_len = input('Enter the length of the code: ')

# Check if the user input is a digit
if code_len.isdigit():
    code_len = int(code_len)  # Convert input to an integer
    
    # Generate the random code using list comprehension
    code_lst = [random.randint(0, 9) for i in range(code_len)]
        
    # Print the generated code
    print('Your code is:', end = ' ')
    for i in code_lst:
        print(i, end = '')  # Use end parameter to print digit side-by-side
        
else:
    # Handle invalid input
    print('Invalid input. Code length must be a non-negative integer.')
    
    

    
    
    
    
    
    