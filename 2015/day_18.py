#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 09:10:02 2023

@author: setuhnjimaja
"""
# This is an implementation of the Game of Life
import numpy as np
import scipy

def light_up_corners(array):
    array[0, 0] = 1
    array[0, -1] = 1
    array[-1, 0] = 1
    array[-1, -1] = 1
    
    return array

grid = []

with open('input_18') as data:
    for line in data.readlines():
        grid.append([1 if char == '#' else 0 for char in line.strip()])       

grid_np = np.array(grid)
# Part 2
grid_np = light_up_corners(grid_np)


turn = 100
# A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
# A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
for _ in range(turn):
    grid_convoluted = scipy.signal.convolve2d(grid_np, np.ones((3,3)), mode='same')
    grid_convoluted -= grid_np
    
    grid_np_next = grid_np.copy()
    grid_np_next[(grid_np == 0) & (grid_convoluted ==3)] = 1
    grid_np_next[(grid_np == 1) & ((grid_convoluted <2) | (grid_convoluted >3))] = 0
    # Part 2
    grid_np_next = light_up_corners(grid_np_next)
    
    grid_np = grid_np_next
    
print(np.count_nonzero(grid_np ==1))