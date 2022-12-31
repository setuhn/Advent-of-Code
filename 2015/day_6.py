# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:42:10 2022

@author: Setuhn
"""

import numpy as np
import re

def read_instruction(instruction):
    if 'turn on' in instruction:
        action = True
    elif 'turn off' in instruction:
        action = False
    elif 'toggle'in instruction:
        action = None
    
    coor_1, coor_2 = [coor.split(',') for coor in re.findall(r'\d+,\d+', instruction)]
    col = sorted([int(coor_1[0]), int(coor_2[0])])
    row = sorted([int(coor_1[1]), int(coor_2[1])])
    
    return action, col, row

# # PART 1
# def turn_on(x): return True
# def turn_off(x): return  False
# def toggle(x): return False if x else True
# turn_on_vec = np.vectorize(turn_on)
# turn_off_vec = np.vectorize(turn_off)
# toggle_vec = np.vectorize(toggle)

# grid = np.full((1000, 1000), False, dtype=bool)

# PART 2
turn_on = lambda x: x+1
turn_off = lambda x: (x-1 if x > 0 else 0)
toggle = lambda x: x+2

turn_off_vec = np.vectorize(turn_off)


grid = np.zeros((1000, 1000), dtype = np.int32)

with open("input_6", 'r') as data:
    for instruction in data.readlines():
        action, col, row = read_instruction(instruction)

        if action == True:
            grid[row[0]:row[1]+1, col[0]:col[1]+1] = turn_on(grid[row[0]:row[1]+1, col[0]:col[1]+1])
        
        elif action == False:
            grid[row[0]:row[1]+1, col[0]:col[1]+1] = turn_off_vec(grid[row[0]:row[1]+1, col[0]:col[1]+1])
        
        elif action == None:
            grid[row[0]:row[1]+1, col[0]:col[1]+1] = toggle(grid[row[0]:row[1]+1, col[0]:col[1]+1])
    
    # # PART 1
    # print(np.count_nonzero(grid == True))
    
    # PART 2
    print(np.sum(grid))
    