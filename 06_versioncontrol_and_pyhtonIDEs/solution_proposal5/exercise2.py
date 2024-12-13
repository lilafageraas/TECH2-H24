# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 13:35:21 2024

@author: s14754
"""

import random
import string

def generate_password(length):
    """
    Generates a password of random letters with a single digit and symbol. The
    password length must at least be 4 characters, and the password will always
    start with a letter.

    Parameters
    ----------
    length : int
        Password length.

    Returns
    -------
    password : str
        Generated password.

    """
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    # Check that the length is at least 4 characters
    if length < 4:
        print('Password length must be at least 4 characters')
        password = '' # Password is simply an empty string
        
    else:
        # Generate list with random letters
        chars = random.choices(letters, k = length - 3)  # Reduce length to add space for symbol, digit and first letter
        
        # Generate a random digit and symbol 
        digit = random.choice(digits) 
        symbol = random.choice(symbols)
        
        # Add the letters, symbol and digit in a list
        password_lst = chars + [digit] + [symbol]
        
        # Shuffle the list 
        random.shuffle(password_lst)  
        
        # Add random letter at the beginning of list
        first_char = random.choice(letters)
        password_lst.insert(0, first_char)
        
        # Alternative 1: use for loop to add each item in the list to a string
        password = ''
        for char in password_lst:
            password += char
    
        # Alternative 2: use the join method
        #password = ''.join(password_lst)

    return password


if __name__ == '__main__':
    # Generate password of 10 random characters
    password_length = 10
    password = generate_password(password_length)
    print('Generated Password:', password)