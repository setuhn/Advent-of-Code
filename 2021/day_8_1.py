# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 20:47:59 2022

@author: Setuhn
"""


try:
    with open("input_8", 'r') as file_open:
        patterns = [[block.split(' ') for block in line.strip().split(' | ')] for line in file_open.readlines()]
        
        answer = []
        
        for entry in patterns:
            answer += [digit for digit in entry[1] if len(digit) in [2, 4, 3, 7]]
            
        print(len(answer))
            
        
except Exception as e:
    print(e)