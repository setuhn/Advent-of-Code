# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:43:42 2022

@author: jimajas
"""

try:
    with open("input_1", 'r') as file_open:
        file_txt = [x.split("\n") for x in file_open.read().strip().split("\n\n")]
        
        carr = []
        
        for elf in file_txt:

            carr += [sum([int(calory) for calory in elf])]
            
        carr.sort(reverse=True)
        
        print(carr[0])

except Exception as e:
    print(e)

    
