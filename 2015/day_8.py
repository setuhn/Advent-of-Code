#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 18:38:35 2022

@author: setuhnjimaja
"""
# 1650 too high

def remove_special_character(string):
    
    string = string.replace('\\\\', '0').replace('\\"', '0')
    
    i = string.find('\\x')
    
    while i != -1:
        string = string.replace(string[i:i+4], '0')
        i = string.find('\\x')

    return string

answer_1 = 0
answer_2 = 0

def mutate_special_character(string):
    string = string.replace('\\', '\\\\').replace('"', '\\"')
    
    return f'"{string}"'

santas_list = []

with open('input_8') as data:
    for line in data.readlines():
        santas_list.append(line)
        
        line = line.strip()
        answer_1 += len(line)
        answer_2 -= len(line)
        
        line_1 = remove_special_character(line[1:-1])
        line_2 = mutate_special_character(line)
        
        answer_1 -= len(line_1)
        answer_2 += len(line_2)
        
        
print('Answer part 1:', answer_1)
print('Answer part 2:', answer_2)