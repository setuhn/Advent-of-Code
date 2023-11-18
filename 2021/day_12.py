#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:37:16 2023

@author: setuhnjimaja
"""
import heapq

cave_system = {}

def get_neighbours(node, path):
    neighbours_possible = cave_system[node]
    neighbours_valid = []
    
    for neighbour in neighbours_possible:
        if neighbour.isupper():
            neighbours_valid += [neighbour]
            
        elif neighbour not in path:
            neighbours_valid += [neighbour]
            
            
    return neighbours_valid

def get_neighbours_v2(node, path):
    neighbours_possible = cave_system[node]
    neighbours_valid = []
    
    for neighbour in neighbours_possible:
        if neighbour != 'start':
            neighbours_valid += [neighbour]
            
    return neighbours_valid



with open('input_12') as data:
    for line in data.readlines():
        start, end = line.strip().split('-')
        
        if start not in cave_system.keys():
            cave_system[start] = []
            
        if end not in cave_system.keys():
            cave_system[end] = []
            
        cave_system[start] += [end]
        cave_system[end] += [start]
        
        
path_q = []

heapq.heappush(path_q, (0, ['start']))

paths_possible = []

while path_q:
    

    _, path_current = heapq.heappop(path_q)
    node_current = path_current[-1]
    
    if node_current == 'end':
        paths_possible += [path_current]
        continue
        
    nodes_next_list = get_neighbours(node_current, path_current)
    
    for node_next in nodes_next_list:
        path_next = path_current + [node_next]
        heapq.heappush(path_q, (0, path_next))
    
print(f'Answer part 1: {len(paths_possible)}')    

path_q = []
heapq.heappush(path_q, (0, (False, ['start'])))
paths_possible = []

while path_q:
    

    _, (double_small_cave, path_current) = heapq.heappop(path_q)
    node_current = path_current[-1]
    
    if node_current == 'end':
        paths_possible += [path_current]
        continue
        
    nodes_next_list = get_neighbours_v2(node_current, path_current)
    
    for node_next in nodes_next_list:
        token = double_small_cave
        
        if node_next.islower() and node_next in path_current:
            
            if token:
                continue
            
            else:
                token = True
            
        path_next = path_current + [node_next]
        heapq.heappush(path_q, (0, (token, path_next)))    
    
print(f'Answer part 2: {len(paths_possible)}')         
    