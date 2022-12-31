# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:43:42 2022

@author: jimajas
"""


def count_parenthesis(input_str):
    counter = 0
    for c in input_str:
        if c == "(": counter +=1
        elif c == ")": counter -=1
        else: print(c)
    
    return counter
            


try:
    with open("input_1", 'r') as file_open:
        file_txt = file_open.read()      
        counter = count_parenthesis(file_txt)
        
        print(counter)
        
except Exception as e:
    print(e)

    
