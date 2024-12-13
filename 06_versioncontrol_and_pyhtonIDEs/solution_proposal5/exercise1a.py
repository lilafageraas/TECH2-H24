# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:23:38 2024

@author: s14754
"""

import itertools


def check_combinations():
    """
    Generates all combinations of the digits 0-9 and returns the combinations
    of numbers that satisfies the equation (abc*de) -(fgh*ij) = 0 where the
    variables a-j is equal to a unique digit.

    Returns
    -------
    valid_combinations : list
        List with the combinations of digits 0-9 that satisfies the equation.

    """

    # Create list of all digits 0-9 as str
    digits = [str(i) for i in range(10)]
    
    # Generate all permutations of the digits 0-9
    all_permutations = itertools.permutations(digits)
    
    # Initialize a list to store all valid combinations
    valid_combinations = []
        
    # Iterate over each permutation
    for perm in all_permutations:
        a, b, c, d, e, f, g, h, i, j = perm
        
        # Calculate the variables
        abc = int(a + b + c)
        de = int(d + e)
        fgh = int(f + g + h)
        ij = int(i + j)
        
        # Calculate the equation
        eq = (abc*de) - (fgh*ij)
        
        # Append combination to list if the equations is equal to zero
        if eq == 0:
            valid_combinations.append(perm)

    return valid_combinations


if __name__ == '__main__':
    solutions = check_combinations()
    print(f'There are {len(solutions)} solutions to the MathTechQuest problem.')