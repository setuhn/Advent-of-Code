# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def cover_coord(coordinates):
    x = [int(coordinates[0][0]), int(coordinates[1][0])]
    y = [int(coordinates[0][1]), int(coordinates[1][1])]

    
    if x[0] == x[1] or y[0] == y[1]:
        
        return ((r_x, r_y) for r_x in range(min(x), max(x)+1) for r_y in range(min(y), max(y)+1))
    
    else:
        return ()
        
    
map_coord = {}
counter = 0

try:
    with open("input_5", 'r') as file_open:
        coordinates = [[coordinate.strip().split(',') for coordinate in entry.strip().split('->')] for entry in file_open.readlines()]
        
        for coord in coordinates:
            for c_coord in cover_coord(coord):
                
                if c_coord in map_coord.keys():
                    map_coord[c_coord] += 1 
                    if map_coord[c_coord ] == 2: counter +=1
                    
                else:
                    map_coord[c_coord] = 1
        
        print(counter)
        
except Exception as e:
    print(e)