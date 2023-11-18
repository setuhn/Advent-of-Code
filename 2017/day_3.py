#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 13:20:05 2023

@author: setuhnjimaja
"""
def find_shell_idx(linear_pos):
    
    idx = 0
    
    start = 1
    end = 2
    
    while True:
        
        if linear_pos in range(start, end):
            return (idx, range(start, end))
        
        idx += 1
        
        start = end
        end += idx*8
def get_distance_from_origin(position):
    
    # distance from centre shell and range of number in the shell
    shell_idx, shell_range = find_shell_idx(position)

    # size of each side of the shell
    shell_side_size = shell_idx*2

    # idx of the centre number
    shell_half = shell_side_size // 2

    # idx of the linear_number in the shell
    idx_num_line = (shell_range.index(linear_pos)) % shell_side_size +1

    shift = abs(shell_half - idx_num_line)

    return shift + shell_idx

def get_adjacent_idx(idx):
    
        
linear_pos = 368078

print('Answer part 1:', get_distance_from_origin(linear_pos))