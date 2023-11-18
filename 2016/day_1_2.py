# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 21:45:00 2023

@author: Setuhn
"""

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def rotate(facing, rotation_letter):
    
    if rotation_letter == 'R':
        facing = facing+1 if facing+1 < len(directions) else 0
    
    else:
        facing = facing-1 if facing-1 >= 0 else len(directions)-1
    
    return facing

def move(position, facing, steps_number, position_history):
    crossed = False
    
    for i in range(1, steps_number+1):
        new_position = [axis+increm*i for axis, increm in zip(position, directions[facing])]
        
        if new_position in position_history:
            crossed = True
            print(sum([abs(axis) for axis in new_position]))
            
        else:
            position_history.append(new_position)
    
    return (new_position, position_history, crossed)

with open('input_1') as data:
    
    movements = [(unit[0], int(unit[1:])) for unit in data.read().strip().split(', ')]
    
position = [0, 0]
facing = 0
position_history = [position]


for rotation, steps in movements:
    facing = rotate(facing, rotation)
    position, position_history, crossed = move(position, facing, steps, position_history)
    
    if crossed:
        break
