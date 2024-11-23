# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:23:38 2024

@author: s14754
"""

# Dictionary mapping choices to actions
d = {
    '1': 'confess',
    '2': 'stay silent'
}


# -----------------------------
# Print Welcome Message
# -----------------------------
print("**********************************")
print("Welcome to the Prisoner's Dilemma.")
print("**********************************")


# -----------------------------
# Prisoner A's Turn
# -----------------------------
print('\nPrisoner A, you are up.')
choiceA = input('Press 1 to "confess", press 2 to "stay silent": ')

# Validate Prisoner A's choice
while choiceA != '1' and choiceA != '2':
    print('Invalid input. Try again.')
    choiceA = input('Press 1 to "confess", press 2 to "stay silent": ')  


# -----------------------------
# Prisoner B's Turn (alt. 1)
# -----------------------------
print('\nPrisoner B, you are up.')

# Loop until a valid input is received
while True:
    choiceB = input('Press 1 to "confess", press 2 to "stay silent": ')
    
    if choiceB == '1' or choiceB == '2':
        break  # Exit loop if valid input is received
    else:
        print('Invalid input. Try again.')
        

# -----------------------------
# Prisoner B's Turn (alt. 2)
# -----------------------------

# Initialize choice to an empty string to ensure the loop starts
#choiceB = ''  

# Loop until a valid input is received
#while choiceB != '1' and choiceB != '2':
#    choiceB = input('Press 1 to "confess", press 2 to "stay silent": ')
#
#    if choiceB != '1' and choiceB != '2':
#        print('Invalid input. Try again.')
    

# -----------------------------
# Display Choices and Outcome
# -----------------------------
print(f'\nPrisoner A chose to {d[choiceA]} and Prisoner B chose to {d[choiceB]}.\n')

# Determine and print the outcome based on the prisoners' choices
if choiceA == '1' and choiceB == '1':
    print('You both get 2 years.')  # Both confess
elif choiceA == '1' and choiceB == '2':
    print('Prisoner A gets 3 years, Prisoner B goes free.')  # A confesses, B stays silent
elif choiceA == '2' and choiceB == '1':
    print('Prisoner A goes free, Prisoner B gets 3 years.')  # A stays silent, B confesses
else:
    print('You both get 1 year.')  # Both stay silent
   
