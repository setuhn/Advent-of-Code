# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 21:06:45 2022

@author: Setuhn
"""

try:
    with open("input_2", 'r') as data:
        
        total_ribbon = 0
        
        for line in data:
            dimensions = sorted(list(map(int, line.strip().split("x"))))
            
            total_ribbon += 2*dimensions[0]+2*dimensions[1] + dimensions[0] * dimensions[1] * dimensions[2]

        print(total_ribbon)
        
except Exception as e:
    print(e)