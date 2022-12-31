# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:03:24 2022

@author: Setuhn
"""

try:
    with open("input_8", 'r') as file_open:
        patterns = [[block.split(' ') for block in line.strip().split(' | ')] for line in file_open.readlines()]
        
        
        print(patterns)
            
        
except Exception as e:
    print(e)