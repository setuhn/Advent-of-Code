# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 18:35:31 2022

@author: Setuhn
"""

import re 

def is_nice(string):
    string = string.lower()
    
    if sum([True for x in ['ab', 'cd', 'pq', 'xy'] if x in string]) == True:
        return False
    
    elif (len(re.findall(r'[aeiou]', string)) >= 3) and re.search(r'([a-z])\1', string):
        return True
    
    else:
        return False

try:
    with open("input_5", 'r') as data:
        
        strings_list = data.readlines()
        
        print(list(map(is_nice, strings_list)).count(True))
    
except Exception as e:
    print(e)