#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:24:23 2022

@author: setuhnjimaja
"""

import numpy as np
import string

class Point:
    def __init__(self,row: int, col: int):
        self.row = row
        self.col = col
        
class Node:
    def __init__(self,point: Point, dist: int):
        self.point = point  # The coordinates of the cell
        self.dist = dist  # Cell's distance from the source

def letter_to_height(letter):
    if letter.islower():
        return string.ascii_lowercase.index(letter)
    
    elif letter == 'S':
        return 0
    
    elif letter == 'E':
        return 26

def valid_move(value_start, value_end):
    if value_end-value_start <=1:
        return True
    
    return False

def get_valid_adjacent_cells(point_init, grid, visited):
    row_incr = [-1, 0, 0, 1]
    col_incr = [0, -1, 1, 0]
    coor_adj_valid = []
    
    for i in range(4):
        row_adj = point_init.row + row_incr[i]
        col_adj = point_init.col + col_incr[i]
        
        if 0 <= row_adj <= grid.shape[0]-1 and 0 <= col_adj <= grid.shape[1]-1:
            if not visited[row_adj, col_adj]:
                if valid_move(grid[point_init.row, point_init.col],  grid[row_adj, col_adj]):
                    coor_adj_valid.append(Point(row_adj, col_adj))
                
    return coor_adj_valid
                   
with open('input_12') as data:
    grid = []
    start_list = []
    end = Point(0,0)
    for row_n, line in enumerate(data.readlines()):
        row = []
        for col_n, letter in enumerate(line.strip()):
            height = letter_to_height(letter)
            
            
            if height == 0:
                start_list.append(Point(row_n, col_n))
                row.append(0)
                
            elif height == 26:
                end.row = row_n
                end.col = col_n
                row.append(25)
            else:
                row.append(height)
            
        grid.append(row)
        
grid_np = np.array(grid)
grid_shape = grid_np.shape

steps = grid_np.shape[0]*grid_np.shape[1]
i = 0

for start in start_list:
    
    # Create a queue for BFS
    q = []
    
    visited = np.full(grid_np.shape, False)
    # Add first coor into queue
    q.append(Node(start, 0))
    visited[start.row, start.col] = True
    while q:
        i+=1
        curr = q.pop(0) # Dequeue the front cell
        
        # If we have reached the destination cell,we are done
        if curr.point.row == end.row and curr.point.col == end.col:
            steps = curr.dist if curr.dist < steps else steps
            
        else:  
            # Otherwise enqueue its adjacent cells
            for point in get_valid_adjacent_cells(curr.point, grid_np, visited):
                q.append(Node(point, curr.dist+1))
                visited[point.row, point.col] = True
                
print(steps)