# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:16:27 2022

@author: Setuhn
"""

try:
    with open("input_3", 'r') as file_open:
        bags_list = [line.strip() for line in file_open.readlines()]
        
        answer = 0
        values = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for bag in bags_list:

            c_1 = bag[:len(bag)//2]
            c_2 = bag[len(bag)//2:]
            
            answer += [values.index(item) for item in c_1 if item in c_2][0]
        
        print(answer)
            
        
except Exception as e:
    print(e)