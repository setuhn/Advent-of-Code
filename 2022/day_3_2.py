# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:49:00 2022

@author: Setuhn
"""

try:
    with open("input_3", 'r') as file_open:
        bags_list = [line.strip() for line in file_open.readlines()]
        
        answer = 0
        values = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        
        for b1, b2, b3 in [(i, i+1, i+2) for i in range(0, len(bags_list), 3)]:

            answer += [values.index(item) for item in bags_list[b1] if (item in bags_list[b2] and item in bags_list[b3])][0]
        
        print(answer)
            
        
except Exception as e:
    print(e)