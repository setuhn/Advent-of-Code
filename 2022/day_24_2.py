#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 10:17:46 2022

@author: setuhnjimaja
"""
import numpy as np

NSEW = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def move_blizz(list_blizzards, map_np):
    for idx, blizzard in enumerate(list_blizzards):
        y, x = blizzard[0]
        dy, dx = blizzard[1]
        map_np[y, x] -= 1
        
        y, x = y+dy, x+dx
        
        if map_np[y, x] == -1 and dy < 0:
            y = map_np.shape[0]-2
        elif map_np[y, x] == -1 and dy > 0:
            y = 1
        elif map_np[y, x] == -1 and dx < 0:
            x = map_np.shape[1]-2
        elif map_np[y, x] == -1 and dx > 0:
            x = 1
            
        map_np[y, x] += 1
        list_blizzards[idx][0] = (y, x)

def next_positions(curr_pos, next_map_np):
    positions = []
    y, x = curr_pos
    
    for dy, dx in NSEW+[(0,0)]:
        if y + dy < len(next_map_np):
            if next_map_np[y+dy, x+dx] == 0:
                positions.append((y+dy, x+dx))
    
    return positions
    
map_str =[]

dict_transl = {
    '.': 0,
    '#': -1,
    '<': 1,
    '>': 1,
    'v': 1,
    '^': 1
    }

direct_transl = {
    '<': (0, -1),
    '>': (0, 1),
    'v': (1, 0),
    '^': (-1, 0)
    }

list_blizz = []
   
with open('input_24') as data:

    for row, line in enumerate(data):
        map_str.append([dict_transl.get(c) for c in line.strip()])
        
        for col, char in enumerate(line):

            if char in direct_transl.keys():
                list_blizz.append([[row, col], direct_transl.get(char)])

map_np = np.array(map_str)

start_pos = (0, np.where(map_np[0, :] == 0)[0][0])
end_pos = (map_np .shape[0]-1, np.where(map_np[-1, :] == 0)[0][0])
goal = [end_pos, start_pos, end_pos]

pos_q = [(start_pos, 0)]
list_map_np = [map_np.copy()]
visited = []

while(True):
    
    curr_pos, time = pos_q.pop(0)
    
    if time+1 > len(list_map_np)-1:
        move_blizz(list_blizz, map_np)
        list_map_np.append(map_np.copy())
        
    curr_map_np = list_map_np[time+1]
    
    if curr_pos == goal[0]:
        print(time)
        goal.pop(0)
        pos_q = [(curr_pos, time)]
        
        if goal:
            continue
        
        else:
            break
    
    next_pos = next_positions(curr_pos, curr_map_np)
    
    time +=1
    
    for pos in next_pos:
        if (pos, time) not in pos_q:
            pos_q.append((pos, time))
            visited.append((pos, time))