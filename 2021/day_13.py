#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 23:17:58 2023

@author: setuhnjimaja
"""
import numpy as np

max_x = max_y = 0
holes = []
folds_instruction = []
a = []

with open('input_13') as data:
    for line in data.readlines():
        line = line.strip()
        
        if line:
        
            if not 'fold' in line:
                x, y = [int(pos) for pos in line.split(',')]
                holes += [[y, x]]
                a.extend([x, y])
                
                if x > max_x : max_x = x
                if y > max_y : max_y = y
                
            else:
                folds_instruction += [line.split()[-1].split('=')]
    
paper = np.zeros((max_y+1, max_x+1), dtype=bool)

for h in holes:
    paper[h[0], h[1]] = True

for idx, (axis, num)  in enumerate(folds_instruction):
    num = int(num)
        
    if axis == 'y':
        if 2*num > (paper.shape[0]-1):
            # np.pad(array, ((top, bottom), (left, right)), 'constant')
            paper = np.pad(paper, ((0, 2*num - (paper.shape[0]-1)), (0, 0)), mode = 'constant')
        
        elif 2*num < (paper.shape[0]-1):
            paper = np.pad(paper, ((2*num - (paper.shape[0]-1), 0), (0, 0)), mode = 'constant')

        paper = paper[:num, :] + np.flip(paper[num+1:, :], axis = 0)
        
    elif axis == 'x':
        if 2*num > (paper.shape[1]-1):
            # np.pad(array, ((top, bottom), (left, right)), 'constant')
            paper = np.pad(paper, ((0, 0), (0, 2*num - (paper.shape[1]-1))), mode = 'constant')
        
        elif 2*num < (paper.shape[1]-1):
            paper = np.pad(paper, ((0, 0), (2*num - (paper.shape[1]-1), 0)), mode = 'constant')
        
        paper = paper[:, :num] + np.flip(paper[:, num+1:], axis = 1)
    
    # Part 1
    if idx == 0:
        print('Answer part 1:', np.count_nonzero(paper == True))
        
# Part 2
print('Answer part 12:')
for row in paper:  
    for col in row:
        print('#' if col else ' ', end = '')
    print()
