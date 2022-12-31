# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 09:20:26 2022

@author: Setuhn
"""

import numpy as np

class Point:
    def __init__(self, coor: list):
        self.x = coor[0]
        self.y = coor[1]

def find_edges(paths):
    x_edges = [500, 0]
    y_edges = [0, 0]
    
    for line in paths:
        for point in line:
            if point.x < x_edges[0]: x_edges[0] = point.x
            elif point.x > x_edges[1]+1: x_edges[1] = point.x+1
            if point.y < y_edges[0]: y_edges[0] = point.y
            elif point.y > y_edges[1]+1: y_edges[1] = point.y+1
            
    return x_edges, y_edges
    
def paint_rock(paths, scan):
    
    for line_points in paths:
        start = line_points[0]    
        
        for point in line_points[1:]:
            if start.x == point.x:
                i, f = (start.y, point.y) if start.y < point.y else (point.y, start.y)
                scan[i:f+1, start.x] = '#'
                
            elif start.y == point.y:
                i, f = (start.x, point.x) if start.x < point.x else (point.x, start.x)
                scan[start.y, i:f+1] = '#'
            
            start = point
               
def cascade_sand(scan, start):
    active_sand = [Point([start.x, start.y])]
    rest_sand = []
    sand_blocked = False
    print(scan[:, 490:503])
    
    while not sand_blocked:
        
        for idx, sand in enumerate(active_sand):

            moved, scan = move_sand(sand, scan)
    
            if not moved:
                rest_sand.append(active_sand.pop(idx))
                
        print(moved, scan[:, 490:503])
        active_sand.append(Point([start.x, start.y]))
        moved, scan = move_sand(sand, scan)
        
        if not moved:
            sand_blocked = True
            rest_sand.append(start)
                
    return rest_sand, active_sand
                
        
def move_sand(sand_point, scan):
    scan[start.y, start.x] = 'o'
    
    if sand_point.y+1 < scan.shape[0]:
        
        if scan[sand_point.y+1, sand_point.x] == '.':
        
            if sand_point.y+1 < scan.shape[0]:
                
                scan[sand_point.y, sand_point.x] = '.'
                sand_point.y += 1
                scan[sand_point.y, sand_point.x] = 'o'
                return True, scan
      
        else:
            if sand_point.x-1 < 0:
                new_col = np.full((scan.shape[0],2), '.')
                new_col[-1] = '#'
                scan = np.hstack((new_col, scan))
                
            if scan[sand_point.y+1, sand_point.x-1] == '.':
                
                scan[sand_point.y, sand_point.x] = '.'
                sand_point.y += 1
                sand_point.x -= 1
                scan[sand_point.y, sand_point.x] = 'o'
                return True, scan
            
            else:
                
                if sand_point.x+1 >= scan.shape[1]:
                    new_col = np.full((scan.shape[0],2), '.')
                    new_col[-1] = '#'
                    scan = np.hstack((scan, new_col))
                    
                if scan[sand_point.y+1, sand_point.x+1] == '.':
                    
                    scan[sand_point.y, sand_point.x] = '.'
                    sand_point.y += 1
                    sand_point.x += 1
                    scan[sand_point.y, sand_point.x] = 'o'
                    return True, scan
                    
    return False, scan
            
        
paths = []
start = Point([500,0])

with open('input_14_test.txt') as data:
    paths.extend([[Point([int(coor.strip()) for coor in point.split(',')]) for point in line.strip().split('->')] for line in data.readlines()])

x_edges, y_edges = find_edges(paths)

scan = np.full((y_edges[1]+2, x_edges[1]), '.')
#Paint the floor
scan[-1, :] = '#'

#Paint the rock
paint_rock(paths, scan)

#Cascade the sand
rest_sand, active_sand = cascade_sand(scan, start)

print(len(rest_sand))

