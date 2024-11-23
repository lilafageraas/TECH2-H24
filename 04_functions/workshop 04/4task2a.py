#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:48:45 2024

@author: lilapfageraas
"""
    
    
def effective_interest_rate(r, n):
    """
    

    Parameters
    ----------
    r : float
        the annual interest rate
    n : int
        number of times that the interest rate is added during the year

    Returns
    -------
    float
        the effective interest rate

    """
    return (1+ (r/n))**n - 1

if __name__ == '__main__':
    
   r = 0.09
    
    #option A
    print(f'Option (a): annual interest rate of {r*100} added each quarter')
    eff_rate = effective_interest_rate (r, 4)
    print(f'the effective interest is {100*eff_rate:.2f} %')
    
    print()
    
    #option B
    eff_rate = effective_interest_rate (r, 12)
    print(f'Option (b): annual interest rate of {r*100} added each month')
    print(f'the effective interest is {100*eff_rate:.2f} %')



    