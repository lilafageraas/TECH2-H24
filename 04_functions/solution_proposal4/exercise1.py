# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:27:51 2024

@author: s14754
"""

def tempConversion(temp, scale):
    """
    Convert temperatures between Fahrenheit and Celsius and return the 
    converted temperature.

    Parameters
    ----------
    temp : float
        The temperature to be converted.
    scale : str
        Takes the value 'F' for Fahrenheit-Celsius conversion and the value 'C'
        for Celsius-Fahrenheit conversion.

    Returns
    -------
    converted_temp : float
        The converted temperature.

    """
    
    # Convert temperature from F->C
    if scale == 'F':
        converted_temp = (5/9) * (temp - 32) 
    
    # Convert temperature from C->F
    else:
        converted_temp = (9/5) * temp + 32
        
    return converted_temp

        
# Code inside this if statement will only be executed when we execute the file
# "exercise1.py" and not when we import the function "tempConversion" in the 
# file "exercise3.py"
if __name__ == '__main__':
    
    from_scale = 'F'
    temp = 32
    
    # Use alternative 1
    converted_temp = tempConversion(temp, from_scale)

    if from_scale == 'F':
        print(f'{temp} degrees Fahrenheit equals {converted_temp:.1f} degrees Celsius.')
    else:
        print(f'{temp} degrees Celsius equals {converted_temp:.1f} degrees Fahrenheit.')
    