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

def move(position, facing, steps_number):
    return [axis+increm*steps_number for axis, increm in zip(position, directions[facing])]

with open('input_1') as data:
    
    movements = [(unit[0], int(unit[1:])) for unit in data.read().strip().split(', ')]
    
    
    
position = [0, 0]
facing = 0

for rotation, steps in movements:
    facing = rotate(facing, rotation)
    position = move(position, facing, steps)

print(sum([abs(axis) for axis in position]))