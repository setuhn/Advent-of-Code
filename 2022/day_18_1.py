# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 14:11:48 2022

@author: Setuhn
"""
import numpy as np
import itertools

droplet = []

# Read input    
with open('input_18') as data:
    for cube in data.readlines():
        cube_coor = tuple((int(coor) for coor in cube.split(',')))
        droplet.append(np.array(cube_coor))            

outside_side = 6 * len(droplet)

for cube_1, cube_2 in itertools.combinations(droplet, 2):
    
    diff = abs(cube_1 - cube_2)
    
    if np.count_nonzero(diff == 0) == 2 and np.count_nonzero(diff == 1) == 1:
        outside_side -=2

print(outside_side)