#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:55:53 2023

@author: setuhnjimaja
"""
open_bracket = ['(', '[', '{', '<']
close_bracket = [')', ']', '}', '>']

points_table ={
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
    }

points_table_2 = {
    ')': 1, 
    ']': 2,
    '}': 3,
    '>': 4
    }

def check_line(line: str) -> tuple:
    expected_bracket = []
    
    for char in line:
        
        if char in open_bracket:
            
            expected_bracket += [close_bracket[open_bracket.index(char)]]
            
        elif char == expected_bracket[-1]:
            expected_bracket.pop()
            
        else:
            return (True, char)
    return (False, reversed(expected_bracket))         
        

with open('input_10') as data:
    
    navigation_subsystem = data.read().strip().split('\n')
    
    
points = 0
points_2 = []
for line in navigation_subsystem:
    illegal, result = check_line(line)
    
    if illegal :
        points += points_table[result]
        
    else:
        points_2_line = 0
        for char in result:
            points_2_line *= 5
            points_2_line += points_table_2[char] 
            
        points_2 += [points_2_line]
        
        
print('Answer part1:', points)
print('Answer part1:', sorted(points_2)[len(points_2)//2])
    