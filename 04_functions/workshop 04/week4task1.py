#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:28:27 2024

@author: lilapfageraas
"""

def tempConversion(temp, scale = 'C'):
    """
    

    Parameters
    ----------
    temp : float
        A temperature to be converted

    scale : str
        indicates the scale of the temperature ("F" or "C")
    
    Returns
    -------
    converted_temp : float
        the converted temperature

    

    """

    if scale == 'F':
        converted_temp = (5/9)*(temp-32)
    else:
        converted_temp = (9/5)*(temp+32)
    return converted_temp
        
tempConversion(0, 'C')

if scale == 'F':
    print(f'{temp} degrees fahrenheit is equal to {converted_temp} degrees celcius')
else:
    print(f'{temp} degrees celcius is equal to {converted_temp} degrees fahrenheit')