#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 09:10:02 2023

@author: setuhnjimaja
"""

from itertools import combinations

with open('input_17') as data:
    containers = [int(num) for num in data.read().strip().split('\n')]
    
quantity_goal = 150
combinations_goal = []    
    
for i in range(1, len(containers)+1):
    possibilities = combinations(containers, i)   
    
    combinations_goal += [p for p in possibilities if sum(p) == quantity_goal]
    
print(f'Answer part 1: {len(combinations_goal)}')    
    
    
length_list = [len(cg) for cg in combinations_goal]   
min_length = min(length_list) 

print(f'Answer part 2: {length_list.count(min_length)}')