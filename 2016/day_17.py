# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 18:31:40 2023

@author: Setuhn
"""
import numpy as np
from itertools import zip_longest
import hashlib
from collections import deque

map_room = []
passcode = 'mmsxrhfx'
doors = ['U', 'D', 'L', 'R']
doors_direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_next_path(path, position):
    doors_info = hashlib.md5((passcode+''.join(path)).encode()).hexdigest()
    
    next_path = [((position[0] + 2*incr[0], position[1] + 2*incr[1]), d) for d, info, incr  in zip(doors, doors_info, doors_direction, ) if info in ['b', 'c', 'd', 'e', 'f'] and map_room_np[position[0] + incr[0], position[1] + incr[1]] == 1]
    
    return next_path

with open('map_17.txt') as data:
    for line in data.readlines():
        line = [int(char) for char in line.strip().replace('#', '2').replace('-', '1').replace('|', '1').replace(' ', '0').replace('V', '4').replace('S', '3')]
        
        map_room.append(line)

map_room_np = np.array(list(zip_longest(*map_room, fillvalue=0)))
map_room_np[7:, 7:] = 4

start_pos = [int(pos) for pos in np.where(map_room_np == 3)]

path_q = deque([[start_pos, []]])

# Part 1
while path_q:
    curr_pos, curr_path = path_q.popleft()
    
    # print(curr_pos)
    
    if map_room_np[curr_pos[0], curr_pos[1]] == 4:
        print('Answer part 1:', ''.join(curr_path))
        break
    
    next_path = get_next_path(curr_path, curr_pos)
    
    for path in next_path:
        
        if path not in path_q:
            
            pos, door = path
            path_q.append([pos, curr_path+[door]])
            
# Part 2
paths_max_size = 0

while path_q:
    curr_pos, curr_path = path_q.popleft()
    
    # print(curr_pos)
    
    if map_room_np[curr_pos[0], curr_pos[1]] == 4:
        if len(curr_path) > paths_max_size:  
            paths_max_size = len(curr_path)
        continue
    
    next_path = get_next_path(curr_path, curr_pos)
    
    for path in next_path:
        
        if path not in path_q:
            
            pos, door = path
            path_q.append([pos, curr_path+[door]])

print('Answer part 2:', paths_max_size)