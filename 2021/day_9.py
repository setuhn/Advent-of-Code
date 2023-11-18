#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 14:35:53 2023

@author: setuhnjimaja
"""
import scipy.ndimage as ndimage
import numpy as np

def find_lowpoints_values(values):
    centre_value = values[2]
    
    useful_values = [num for num in values if num > centre_value]
    
    if len(useful_values) == len([num for num in values if num >= 0])-1:
        
        return centre_value + 1
    
    else:
        return 0

with open('input_9') as data:
    floor_map = np.array([[int(num) for num in line] for line in data.read().strip().split('\n')])


# Part 1
footprint = np.array([[0,1,0],
                      [1,1,1],
                      [0,1,0]])

lowpoints = ndimage.generic_filter(floor_map, find_lowpoints_values, footprint=footprint, mode = 'constant', cval = -1)
print('Answer part 1:', lowpoints.sum())

# Part 2
from scipy.ndimage import label

floor_map_basin = np.ones(floor_map.shape, dtype = int)
floor_map_basin[np.where(floor_map == 9)] = 0

basins = label(floor_map_basin, footprint)
basins_size = []

for b in range(1, basins[1]+1):
    basins_size += [np.count_nonzero(basins[0] == b)]

product = 1

for s in sorted(basins_size)[-3:]:
    product *= s
    
print('Answer part 2:', product)


