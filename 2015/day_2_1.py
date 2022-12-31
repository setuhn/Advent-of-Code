# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:54:17 2022

@author: jimajas
"""

try:
    with open("input_2", 'r') as file_open:
        file_txt = file_open.readlines()      
        
        wrapping_total = 0
        
        for line in file_txt:
            dimensions_str = line.strip().split("x")
            dimensions = list(map(int, dimensions_str))
            d = [dimensions[0]*dimensions[1], dimensions[0]*dimensions[2], dimensions[1]*dimensions[2]]
            
            wrapping_total += 2*sum(d) + min(d)
            
        print(wrapping_total)
        
except Exception as e:
    print(e)