# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 18:35:31 2022

@author: Setuhn
"""

import re 

def is_nice(string):
    string = string.lower()
    
    if re.search(r'(.)(.).*\1\2', string) and re.search(r'(.).\1', string):
        return True
    
    else:
        return False

try:
    with open("input_5", 'r') as data:
        
        strings_list = data.readlines()
        
        print(list(map(is_nice, strings_list)).count(True))
    
except Exception as e:
    print(e)