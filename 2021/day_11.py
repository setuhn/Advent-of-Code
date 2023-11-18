#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 07:39:16 2023

@author: setuhnjimaja
"""
from scipy import ndimage
import numpy as np

footprint = np.array([[1,1,1],
                      [1,1,1],
                      [1,1,1]])

def flash_values(values):
    centre_value = values[4]
    
    if centre_value > 0:
    
        flashes = len([num for idx, num in enumerate(values) if num >= 10 and idx != 4])
            
        return centre_value + flashes
    
    else:
        
        return centre_value
    
with open('input_11') as data:
    octopus_map = np.array([[int(num) for num in line] for line in data.read().strip().split('\n')])

goal_steps = 100
flashes = 0

step = 0
synchro_flash = False

while not synchro_flash or step <= goal_steps:
    step += 1
    octopus_map += 1
    
    while np.count_nonzero(octopus_map >= 10):
    
        new_map = ndimage.generic_filter(octopus_map, flash_values, footprint=footprint, mode = 'constant', cval = -1)
        
        if step <= goal_steps:
            flashes += np.count_nonzero(octopus_map >= 10)
        
        new_map[np.where(octopus_map >= 10)] = 0
        
        octopus_map = new_map
        
        if np.count_nonzero(octopus_map != 0) == 0:
            synchro_flash = True
            
print('Answer part 1:', flashes)    
print('Answer part 2:', step)
