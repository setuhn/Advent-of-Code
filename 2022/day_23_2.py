#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 12:49:43 2022

@author: setuhnjimaja
"""

import numpy as np

NSWE_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
NSWE_8 = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
NSWE_choice = [
    [(-1, 0), (-1, 1), (-1, -1)], #N
    [(1, 0), (1, -1), (1, 1)], #S
    [(-1, -1), (0, -1), (1, -1)],#W
    [(-1, 1), (0, 1), (1, 1)] #E
    ]

class Elf:
    def __init__(self, position: tuple):
        self.position = position
        self.checklist = NSWE_choice
        self.direction_list = NSWE_4
        self.path = [position]
# TODO: remove the surrounded list from the checklist to drcrease the check number (speedup program)
def surrounded(elf, map_np):
    y, x = elf.position
    surrounded_by = []
    
    for dx, dy in NSWE_8:
        if map_np[y + dy , x + dx] != 0:
            surrounded_by.append(map_np[y, x])
        
    return surrounded_by

# TODO
def choose_next_position(elf, map_np):
    y, x = elf.position

    empty_direction = True
    
    for i, direct_list in enumerate(elf.checklist):
        direction_i = i
        empty_direction = True
        
        for dy, dx in direct_list:
            
            if map_np[y + dy , x + dx] != 0:

                empty_direction = False
                break
            
        if empty_direction:
        
            return (y + elf.direction_list[direction_i][0], x + elf.direction_list[direction_i][1])
    
    return ()
            
    
# remove empty row and col on each sides
def trim_map(map_np):
    height, width = map_np.shape
    
    # top
    for row in range(height):
        if np.count_nonzero(map_np[0, :] != 0) > 0:
            break
        map_np = np.delete(map_np, 0, axis=0)
        
    # bottom
    for row in range(height):
        if np.count_nonzero(map_np[-1, :] != 0) > 0:
            break
        map_np = np.delete(map_np, -1, axis=0)
        
    # left
    for col in range(width):
        if np.count_nonzero(map_np[:, 0] != 0) > 0:
            break
        map_np = np.delete(map_np, 0, axis=1)
        
    # right
    for col in range(width):
        if np.count_nonzero(map_np[:, -1] != 0) > 0:
            break
        map_np = np.delete(map_np, -1, axis=1)
        
    return map_np
        

with open('input_23') as data:

    map_str = [[1 if char == '#' else 0 for char in line] for line in data.readlines()]

map_np = np.array(map_str, dtype=object) 

# create an arbitrary big array. Enlarge if reach the end during runtime
n_map = 1000
# pad map with 15 empty row/column on each side to avoid hitting the end of the map:
map_np = np.vstack((np.zeros((n_map, map_np.shape[1])), map_np, np.zeros((n_map, map_np.shape[1]))))
map_np = np.hstack((np.zeros((map_np.shape[0], n_map)), map_np, np.zeros((map_np.shape[0], n_map))))

elfs_positions = np.transpose((map_np == 1).nonzero())
elfs_list = []

for position in elfs_positions:
    y, x = position
    new_elf = Elf((y, x))
    elfs_list.append(new_elf)
    map_np[y, x] = new_elf
    
rounds = 0
next_moves = {}
elf_moving = True

while elf_moving:
    # print(rounds, elf_moving)
    rounds +=1
    
    # calculate the next positions for all the elfs that can move
    for elf in elfs_list :
        if surrounded(elf, map_np):
            new_pos = choose_next_position(elf, map_np)
            
            if new_pos in next_moves.keys():
                next_moves[new_pos].append(elf)
            else:
                next_moves[new_pos] = [elf]
                          
    # move the elfs if only one has pre-selected the position otherwise, change the NSEW order:
    for new_pos, elf  in next_moves.items():
        if len(elf) == 1 and new_pos:
            # erase elf at current location
            y, x = elf[0].position 
            map_np[y, x] = 0
            # write elf at new location
            y, x = new_pos
            if map_np[y, x] != 0:
                print( 'ERROR_1: ', y, x)
            else:
                map_np[y, x] = new_elf
                elf[0].position = (y, x)
            
    if next_moves == {}:
        elf_moving = False
        
    # end of round
    next_moves = {}
    NSWE_4.append(NSWE_4.pop(0))
    NSWE_choice.append(NSWE_choice.pop(0))    

print(rounds)