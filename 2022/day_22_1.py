# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 08:34:48 2022

@author: Setuhn
"""
import re
import numpy as np

# 197092 -> too low

# If a movement instruction would take you off of the map, you wrap around to the other side of the board
# Except if it is a wall
def advance(coor: tuple, facing: list, steps: int, map_np) -> tuple:
    y, x = coor
    x_d, y_d = facing
    path_coor = [coor] 
    hit_wall = False
    
    while(len(path_coor) <= steps and not hit_wall):
        x += x_d
        y += y_d
        
        # if end of grid reached, wrap around
        if map_np[y, x] == 2:
            
            if x_d < 0: 
                x = np.where(map_np[y, :] != 2)[0][-1]
            
            elif x_d > 0:
                x = np.where(map_np[y, :] != 2)[0][0]
                
            elif y_d < 0: 
                y = np.where(map_np[:, x] != 2)[0][-1]
        
                
            elif y_d > 0:
                y = np.where(map_np[:, x] != 2)[0][0]
                 
        # check if the next step is a wall (==1)
        if map_np[y, x] == 1:
           hit_wall = True
    
        # if the next step is free
        elif map_np[y, x] == 0: 
            path_coor.append((y, x))
        
        # print(y, x)
    # print(path_coor)
    return path_coor[-1]

# turn 90 degrees clockwise (R) or counterclockwise (L). 
def rotate(facing: list, rotation_letter: str) -> tuple:
    x_d = facing[0]
    y_d = facing[1]
    
    if rotation_letter == 'R':
        x_d, y_d = -y_d if y_d != 0 else 0, x_d
    
    elif rotation_letter == 'L':
        x_d, y_d = y_d, -x_d if x_d != 0 else 0
        
    return (x_d, y_d)

# a path like 10R5 means "go forward 10 tiles, then turn clockwise 90 degrees, then go forward 5 tiles"

with open('input_22') as data:

    map_str, directions_str = data.read().split('\n\n')
    

directions = [(match[:-1], match[-1]) if not match[-1].isdigit() else match for match in re.findall(r'\d+[RL]*', directions_str)]

map_str = map_str.split('\n')

# decompose map into components and pad the end with 2s (represent the end of the map)
map_q = [[2]+[c for c in line]+[2] for line in map_str]

for x, line in enumerate(map_q):
    
    for y, character in enumerate(line):
        if character=='.':
            map_q[x][y] = 0
        elif character=='#':
            map_q[x][y] = 1
        elif character==' ':
            map_q[x][y] = 2
            
# Pad the top and bottom with None list            
map_q.insert(0, [2]*len(map_q[0]))
map_q.append([2]*len(map_q[-1]))

# dimensions of the array
width = max([len(line) for line in map_q])
height = len(map_q)

# pad the right hand side with 2s to have all lines the same size for numpy array
map_q = [line+[2]*(width-len(line)) for line in map_q]

map_np = np.array(map_q)

# You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing to the right
coor = [0, 0]
for y in range(height):
    if np.count_nonzero(map_np[y, :] < 2) > 0:
        for x in range(width):
            if map_np[y, x] < 2:
                coor = [y, x]
                break
        break
   
             
facing = [1, 0] # facing = rotate(facing, 'R')

# print(advance([9, 13], [0, -1], 20, map_np))

for d in directions:
    # print(coor,facing, d, end='')
    if isinstance(d, tuple):
        coor = advance(coor, facing, int(d[0]), map_np)
        facing = rotate(facing, d[1])
        
    else:
        coor = advance(coor, facing, int(d), map_np)
        
    # print(coor)

if facing == (1, 0):
    f = 0
elif facing == (-1, 0):
    f = 2
elif facing == (0, 1):
    f = 1
elif facing == (0, -1):
    f = 3
    
print(coor)    
print(1000*coor[0] + 4 * coor[1] + f)

