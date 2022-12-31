# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 12:58:18 2022

@author: Setuhn
"""
import re
import numpy as np

class Dice_face:
    def __init__(self, numpy_array, top, right, bottom, left):
        self.grid = numpy_array
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

# class Die:
#     def __init__(self, numpy_array, top, right, bottom, left):

# If a movement instruction would take you off of the map, you wrap around to the other side of the board
# Except if it is a wall
def advance(coor: tuple, facing: list, steps: int, dice: dict, current_side:int) -> tuple:
    y, x = coor
    x_d, y_d = facing
    path_coor = [(coor, current_side)] 
    hit_wall = False
    size_array = dice[current_side].array.shape[0]
    previous_side = None
    
    while(len(path_coor) <= steps and not hit_wall):
        x += x_d
        y += y_d
        
        # if end of side reached, go to next side
        if x < 0:  # go left
            previous_side, current_side = current_side, dice[current_side].left
            other_coor = y
        
        elif x >= size_array:  # right
            previous_side, current_side = current_side, dice[current_side].right
            other_coor = y
            
        elif y < 0:  # go top
            previous_side, current_side = current_side, dice[current_side].top
            other_coor = x
            
        elif y >= size_array:  # bottom
            previous_side, current_side = current_side, dice[current_side].bottom
            other_coor = x
            
        if previous_side:
            if previous_side == dice[current_side].top:
                new_facing = (0, 1)
                x, y = other_coor, 0
                
                if current_side in [dice[previous_side].right, dice[previous_side].top]:
                    x = size_array-1-other_coor
                
            elif previous_side == dice[current_side].bottom:
                new_facing = (0, -1)
                x, y = other_coor, size_array-1
                
                if current_side in [dice[previous_side].left, dice[previous_side].bottom]:
                    x = size_array-1-other_coor
                
            elif previous_side == dice[current_side].left:
                new_facing = (1, 0)
                x, y = 0, other_coor
                
                if current_side in [dice[previous_side].bottom, dice[previous_side].left]:
                    y = size_array-1-other_coor
                
            elif previous_side == dice[current_side].right:
                new_facing = (-1, 0)
                x, y = size_array-1, other_coor
                
                if current_side in [dice[previous_side].top, dice[previous_side].right]:
                    y = size_array-1-other_coor
            
        # check if the next step is a wall (==1)
        if dice[current_side].array[y, x] == 1:
           hit_wall = True
    
        # if the next step is free
        elif dice[current_side].array[y, x] == 0: 
            path_coor.append(((y, x), current_side))
            
            if previous_side:
                facing = new_facing
                x_d, y_d = facing
        
        previous_side = None

    return path_coor[-1], facing

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
map_q = [[c for c in line] for line in map_str]

for x, line in enumerate(map_q):
    
    for y, character in enumerate(line):
        if character=='.':
            map_q[x][y] = 0
        elif character=='#':
            map_q[x][y] = 1
        elif character==' ':
            map_q[x][y] = 2
            

# dimensions of the array
width = max([len(line) for line in map_q])
height = len(map_q)

# pad the right hand side with 2s to have all lines the same size for numpy array
map_q = [line+[2]*(width-len(line)) for line in map_q]

# TODO: automate this?
# test
# dice = {
#        1: Dice_face(None, 2, 6, 4, 3),
#        2: Dice_face(None, 1, 3, 5, 6),
#        3: Dice_face(None, 1, 4, 5, 2),
#        4: Dice_face(None, 1, 6, 5, 3),
#        5: Dice_face(None, 4, 6, 2, 5),
#        6: Dice_face(None, 4, 1, 2, 5),
#        }
# real input
dice = {
        1:Dice_face(None, 6, 2, 3, 4),
        2:Dice_face(None, 6, 5, 3, 1),
        3:Dice_face(None, 1, 2, 5, 4),
        4:Dice_face(None, 3, 5, 6, 1),
        5:Dice_face(None, 3, 2, 6, 4),
        6:Dice_face(None, 4, 5, 2, 1),
        }

map_np = np.array(map_q)

# slice the map array into equal shape squares
if map_np.shape[0] == max(map_np.shape):
    sliced_map_np = [np.split(array, 3, axis=1) for array in np.split(map_np, 4, axis=0)]
else:
    sliced_map_np = [np.split(array, 4, axis=1) for array in np.split(map_np, 3, axis=0)]
    
# only keep the squares that have no 2s in them (the dice faces)
list_sides = []
left_corner_sides = []

for idx_row, line in enumerate(sliced_map_np):
    for idx_col, array in enumerate(line):
        if np.count_nonzero(array ==2) == 0:
            list_sides.append(array)
            left_corner_sides.append((idx_row*array.shape[0], idx_col*array.shape[1]))

for name, side in zip(dice.keys(), list_sides):
    dice[name].array = side

current_side = 1

# You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing to the right
coor = (0, 0)
facing = (1, 0) # facing = rotate(facing, 'R')

for d in directions:
    if isinstance(d, tuple):
        (coor, current_side), facing = advance(coor, facing, int(d[0]), dice, current_side)
        facing = rotate(facing, d[1])
        
    else:
        (coor, current_side), facing = advance(coor, facing, int(d), dice, current_side)

coor_final = [0, 0]
coor_final[0] = coor[0] + left_corner_sides[current_side-1][0] +1 
coor_final[1] = coor[1] + left_corner_sides[current_side-1][1] +1

if facing == (1, 0):
    f = 0
elif facing == (-1, 0):
    f = 2
elif facing == (0, 1):
    f = 1
elif facing == (0, -1):
    f = 3
    
print(coor_final)    
print(1000*coor_final[0] + 4 * coor_final[1] + f)