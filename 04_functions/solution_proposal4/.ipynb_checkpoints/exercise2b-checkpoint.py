# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:32:12 2024

@author: s14754
"""

"""
Example 11.1.4 from TECH1: 
    When investing in a savings account, which of the following offers are 
    better: (i) 5.9% with interest paid quarterly; or (ii) 6% with interest
    paid twice a year?
"""

# Note: importing the function "effective_interest_rate" will only work if the 
# files "exercise2a.py" and "exercise2b.py" are located in the same folder and 
# your working directory is set to the folder where these files are located
from exercise2a import effective_interest_rate


# Option (i)
int_rate1 = 5.9
print(f'Offer (i): interest rate of {int_rate1:.2f}% paid quarterly')
eff_rate1 = effective_interest_rate(int_rate1/100, 4)
print(f'Effective interest rate is {100*eff_rate1:.2f}%\n')

# Option (ii)
int_rate2 = 6
print(f'Offer (ii): interest rate of {int_rate1:.2f}% paid twice a year')
eff_rate2 = effective_interest_rate(int_rate2/100, 2)
print(f'Effective interest rate is {100*eff_rate2:.2f}%\n')