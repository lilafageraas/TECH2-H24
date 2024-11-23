#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:27:16 2024

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

eff_rate = effective_interest_rate (0.059, 4)
print(f' offer 1 is {eff_rate*100:.2f} %')

print()

eff_rate = effective_interest_rate (0.06, 2)
print(f' offer 2 is {eff_rate*100:.2f} %')