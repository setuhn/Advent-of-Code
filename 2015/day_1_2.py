# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:49:18 2022

@author: jimajas
"""

def enter_basement(input_str):
    counter = 0
    for i, c in enumerate(input_str):
        if c == "(": 
            counter +=1
        elif c == ")": 
            counter -=1
        else: print(c)
        
        if counter == -1: 
            break
    
    return i+1
            


try:
    with open("input_1", 'r') as file_open:
        file_txt = file_open.read()      
        position = enter_basement(file_txt)
        
        print(position)
        
except Exception as e:
    print(e)