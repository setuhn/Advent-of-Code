# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 22:20:00 2023

@author: Setuhn
"""

import numpy as np
move_translator = {
    'U': (-1, 0), 
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1)
    }

def move_finger(position, numpad, movements):
    new_position = position
    for move in movements:
        new_position = [(axis + increment if (0 <= axis + increment < len(numpad)) else axis) for axis, increment in zip(position, move_translator[move])] 
        
        if numpad[new_position[0], new_position[1]] != '0':
            position = new_position
        
    return position

instructions = []
with open('input_2') as data:
    
    for line in data.readlines():
        
        instructions.append([move for move in line .strip()])

numpad = np.array([
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, 'A', 'B', 'C', 0],
    [0, 0, 'D', 0, 0]
    ])

position = [2, 0]
combination = []

for movements in instructions:
    position = move_finger(position, numpad, movements)
    combination.append(str(numpad[position[0], position[1]]))
    
print(''.join(combination))


    


