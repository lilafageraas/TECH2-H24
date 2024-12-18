# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:53:50 2024

@author: s14754
"""

from random import randint
from exercise4a import randomCharacter


def main():
    """
    Displays a random password of a user-supplied length. 

    Returns
    -------
    None.

    """
    
        
    # Print program welcome
    print('**************************************************')
    print('*********** Password Generator Program ***********')
    print('**************************************************')
    print('This program generates a random password of lowercase letters with one digit and symbol')
    
    # Prompt the user for the length of the password (minimum 3)
    l = getLength()
    
    # Generate the random password
    pw = makePassword(l)
    
    print(f'\nGenerated password: {pw}')
    
    
def getLength():
    """
    Prompt the user to supply the number of character in the password. The user
    is re-prompted until an integer of at least 3 is supplied.

    Returns
    -------
    int
        Number of characters in the password.

    """
    
    while True:
        try:
            length = int(input('\nEnter the password length (minimum 3): '))
            if length >= 3:
                return length
            else:
                print('Password length must be at least 3. Please try again.')
        except:
            print('Invalid input. Please enter a valid integer.')
            

def makePassword(length):
    """
    Generate a random password consisting of lowercase letters and with a 
    digit (0-9) and symbol (+-*/?!@#$%&) inserted at random locations in the 
    password (but not at the start of the password).

    Parameters
    ----------
    length : int
        Number of characters in the password.

    Returns
    -------
    password : str
        Random password.

    """
    
    # Check that password length is at least three characters
    if length < 3:
        print('Password length must be at least 3 to include one starting letter, one digit, and one symbol.')
        
    else:
        # Initialize empty list to store characters
        password_lst = []
        
        # Draw random letters and add to list
        for i in range(length-2):  # Draw two letters less than the length of the password
            letter = randomCharacter('abcdefghijklmnopqrstuvwxyz')
            password_lst.append(letter)
            
        # Draw a random digit and insert at random index in list
        digit = randomCharacter('0123456789')
        password_lst.insert(randint(1, len(password_lst)), digit)  # Not inserted at the start
        
        # Draw random symbol and insert at random index in list
        symbol = randomCharacter('+-*/?!@#$%&')
        password_lst.insert(randint(1, len(password_lst)), symbol)  # Not inserted at the start
        
        # Use for loop to join all characters in list to a string...
        password = ''
        for char in password_lst:
            password += char
            
        # ...or use instead the join method for a nice one-line solution
        #password = ''.join(password_lst)
        
        return password



if __name__ == '__main__':
    main()
    

