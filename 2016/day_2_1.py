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
    
    for move in movements:
        position = [(axis + increment if (0 <= axis + increment < len(numpad)) else axis) for axis, increment in zip(position, move_translator[move])] 
        
    return position

instructions = []
with open('input_2') as data:
    
    for line in data.readlines():
        
        instructions.append([move for move in line .strip()])

numpad = np.arange(1, 10).reshape((3, 3))
position = [axis//2 for axis in numpad.shape]
combination = []

for movements in instructions:
    position = move_finger(position, numpad, movements)
    combination.append(str(numpad[position[0], position[1]]))
    
print(''.join(combination))


    


