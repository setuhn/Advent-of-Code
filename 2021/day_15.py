#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 08:22:36 2023

@author: setuhnjimaja
"""
import numpy as np
import heapq

def get_next_positions(pos_current: tuple, risk_map_limit: int) -> tuple:
    
    x = pos_current[0]
    y = pos_current[1]
    pos_next_valid = []

    pos_next  = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    for pos in pos_next :
        if (0 <= pos[0] <= risk_map_limit - 1) and (0 <= pos[1] <= risk_map_limit - 1):
            pos_next_valid += [pos]
    
    return pos_next_valid
       
def get_lowest_risk(risk_map: np.array):
    pos_start = (0, 0)
    risk_start = 0

    pos_end = tuple([pos-1 for pos in risk_map.shape])
    path_q = []
    

    heapq.heappush(path_q, (0, (pos_start, risk_start)))
    
    # calculate the starting lowest risk by summing an easy path (down the first column and along the last row or opposite)
    risk_min_val = min([np.sum(risk_map[:, 0]) + np.sum(risk_map[-1, 1:]), np.sum(risk_map[0, :]) + np.sum(risk_map[1:, -1])])
    visited = {}
    risk_map_limit = risk_map.shape[0]
    
    while path_q:
        _, (pos_current, risk_current) = heapq.heappop(path_q)
        
        # If this path leads to the end: 
        if pos_current == pos_end:
    
            # check if it is a new min: replace the risk_min
            risk_min_val = min([risk_min_val, risk_current])
            
            continue
        
        # Get the list of the possible positions
        pos_next_list = get_next_positions(pos_current, risk_map_limit)
        
        for pos_next in pos_next_list:
            
            risk_next = risk_current + risk_map[pos_next]
            
            #If we encounter the same cell as before and the risk that was associated with it is lower than the one we currently have, we prune this branch
            if pos_next in visited.keys():
                
                if risk_next >= visited[pos_next]:
                    continue
                
            
            visited[pos_next] = risk_next
            
            #  If the new risk is bigger than the current min risk: prune the branch
            if not risk_next >= risk_min_val:
                heapq.heappush(path_q, (risk_next+get_distance_to(pos_next, pos_end), (pos_next, risk_next)))
    
    return risk_min_val

def get_distance_to(pos_start: tuple, pos_end: tuple) -> int:
    return abs(pos_start[0] - pos_end[0]) + abs(pos_start[1] - pos_end[1])
                
with open('input_15') as data:
    
    risk_map = np.array([[int(num) for num in line] for line in data.read().strip().split('\n')])

# Part 1
risk_min = get_lowest_risk(risk_map)
print(f'Answer part 1: {risk_min}')

# Part 2
neighbours = {}
risk_map_new_list = [np.copy(risk_map)]
n = 5

for _ in range(2*(n-1)):
    risk_map += 1
    risk_map[np.where(risk_map == 10)] = 1
    risk_map_new_list.append(np.copy(risk_map))

risk_map_new = np.concatenate(risk_map_new_list[:n])

for i in range(1, n):
    risk_map_new = np.concatenate((risk_map_new, np.concatenate(risk_map_new_list[i:n+i])), axis = 1)

risk_min_new = get_lowest_risk(risk_map_new)
print(f'Answer part 2: {risk_min_new}')
            