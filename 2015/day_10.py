#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 23:20:49 2022

@author: setuhnjimaja
"""
from itertools import groupby

def look_and_say(number: str) -> str:
    new_number = ''
    
    for digit, digit_list in groupby(number):
        new_number += f'{len(list(digit_list))}{digit}'
        
    return new_number
    
number = '1321131112'

# part 1: range(40)

for _ in range(50):
    number = look_and_say(number)
    
print(len(number))