# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 09:44:41 2024

@author: s14754
"""

from random import randint


def randomCharacter(characters):
    """
    Returns a single character from a random index in a sequence of characters.

    Parameters
    ----------
    characters : str
        A sequence of characters.

    Returns
    -------
    rand_char : str
        A random character from the sequence.

    """
    
    # Check that sequence is not empty
    if len(characters) == 0:
        print('The sequence is empty.')
        return ''  # Return empty string
    
    else:
        # Draw a random index given the length of the sequence
        n = len(characters)
        i = randint(0, n-1)
        
        # Extract character at random index
        rand_char = characters[i]
        
        return rand_char
    


if __name__ == '__main__':
    letter = randomCharacter('abcdefghijklmnopqrstuvwxyz')
    print(f'Random letter: {letter}')
    
    print()
    
    digit = randomCharacter('0123456789')
    print(f'Random digit: {digit}')
    
    print()

    char = randomCharacter('')
    print(f'Random character: {char}')