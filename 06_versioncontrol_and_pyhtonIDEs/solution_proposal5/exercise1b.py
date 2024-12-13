# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 16:23:59 2024

@author: s14754
"""

from exercise1a import check_combinations


def main():
    """
    Finds and prints all of the solutions to the MathTechQuest problem.

    Returns
    -------
    None.

    """
    
    # Get all valid combinations
    print('Checking for solutions...')
    valid_combinations = check_combinations()

    # Print number of valid combinations (if there are any)
    if valid_combinations:
        print(f"\nNumber of solutions to this problem: {len(valid_combinations)}")
        
        # Ask user if all combinations should be printed
        choice = input('\nPrint all solutions? Press "Y" for yes, and "N" for no: ').upper()
        if choice == 'Y':
            print_combinations(valid_combinations)
            
    else:
        print("No combinations found where eq1 equals eq2.")
        
        

def print_combinations(combinations):
    """
    Prints all of the solutions to the MathTechQuest problem.

    Parameters
    ----------
    combinations : List
        List with the combinations that solves the problem.

    Returns
    -------
    None.

    """
    
    for n, comb in enumerate(combinations):
        a, b, c, d, e, f, g, h, i, j = comb
        
        # Calculate the value of equation 1
        abc = int(a + b + c)
        de = int(d + e)
        eq1 = abc * de
        
        # Calculate the value of equation 2
        fgh = int(f + g + h)
        ij = int(i + j)
        eq2 = fgh * ij
        
        print(f'Solution number {n+1}:')
        print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}, g = {g}, h = {h}, i = {i}, j = {j}')
        print(f"abc*de = {abc} * {de} = {eq1}")
        print(f"fgh * ij = {fgh} * {ij} = {eq2}\n")


if __name__ == '__main__':
    main()





