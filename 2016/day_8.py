# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 12:26:59 2023

@author: Setuhn
"""
import numpy as np
import re

def rotate_row(row, shift):
    pass

def rotate_column(col, shift):
    pass


# The screen is 50 pixels wide and 6 pixels tall
screen = np.zeros((6, 50), dtype = np.intc)

with open('input_8') as data:
    for line in data.readlines():
        instruction = line.strip()
        
        if 'rect' in instruction:
            width, height = [int(num) for num in instruction.split()[-1].split('x')]
            screen[:height, :width] = 1
            
        elif 'rotate column' in instruction:
            col, shift = [int(num) for num in re.search(r'x=(\d+) by (\d+)', instruction).groups()]
            screen[:, col] = np.roll(screen[:, col], shift)
            
        elif 'rotate row' in instruction:
            row, shift = [int(num) for num in re.search(r'y=(\d+) by (\d+)', instruction).groups()]
            screen[row, :] = np.roll(screen[row, :], shift)
# Part 1           
print('Answer part 1:', np.count_nonzero(screen == 1))

# Part 2
print('Answer part 2:')
for line in screen:
    for char in line:
        if char == 1:
            print('o', end='')
        else:
            print(' ', end='')
    print()
