# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:04:01 2024

@author: s14754
"""

"""
Example 11.1.3 from TECH1: 
    What is the effective yearly rate R corresponding to an annual interest
    rate of 9% with interest compunded: (a) each quarter; (b) each month?
"""


def effective_interest_rate(r, n):
    """
    Calculate the effective interest rate given the annual interest rate 
    and number of times during a year that the interest rate is added to the 
    principle amount.

    Parameters
    ----------
    r : float
        Yearly interest rate.
    n : integer
        Number of times that the interest rate is added during a year.

    Returns
    -------
    float
        Effective annual interest rate.

    """
    
    return (1 + r/n)**n - 1



if __name__ == '__main__':
    
    annual_rate = 0.09
    
    # Option (a)
    print(f'Option (a) Annual interest rate of {100*annual_rate:.2f}% added each quarter:')
    eff_rate1 = effective_interest_rate(annual_rate, 4)
    print(f'Effective annual interest rate is {100*eff_rate1:.2f}%\n')
    
    # Option (b)
    print(f'Option (b) Annual interest rate of {100*annual_rate:.2f}% added each month:')
    eff_rate2 = effective_interest_rate(annual_rate, 12)
    print(f'Effective annual interest rate is {100*eff_rate2:.2f}%\n')

