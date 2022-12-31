# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 08:50:58 2022

@author: Setuhn
"""

try:
    with open("input_1", 'r') as file_open:
        file_txt = [x.split("\n") for x in file_open.read().strip().split("\n\n")]
        
        carr = []
        
        for elf in file_txt:

            carr +=  [sum([int(calory) for calory in elf])]
        
        carr.sort(reverse=True)
            
        print(sum(carr[:3]))

except Exception as e:
    print(e)
