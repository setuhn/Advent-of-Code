# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:19:05 2023

@author: Setuhn
"""
import numpy as np
import re 

input_str = 'abcdefgh'
string_np = np.array([char for char in input_str])


# swap position X with position Y 
# swap letter X with letter Y 
# rotate left/right X steps 
# rotate based on position of letter X 
# reverse positions X through Y 
# move position X to position Y 

def swap_pos(x, y):
    string_np[x], string_np[y] = string_np[y], string_np[x]
    return string_np

def swap_char(x, y):
    pos_x, pos_y = int(np.where(string_np == x)[0]), int(np.where(string_np == y)[0])
    string_np[pos_x], string_np[pos_y] = string_np[pos_y], string_np[pos_x]
    
    return string_np
    
def rotate_right(x):
    return np.roll(string_np, x)

def rotate_left(x):
    return np.roll(string_np, -x)

def rotate_based_on_pos(x):
    pos_x = int(np.where(string_np == x)[0])
    
    return np.roll(string_np, pos_x+(1 if pos_x < 4 else 2))

def reverse_position(x, y):
    string_np[x:y+1] = np.flip(string_np[x:y+1])
    
    return string_np
    
def move_position(x, y):
    char = string_np[x]
    return np.insert(np.delete(string_np, x), y, char)

def rotate_based_on_pos_reversed(x):
    pos_x = int(np.where(string_np == x)[0])
    
    if pos_x % 2 != 0:
        incr = (pos_x+1)//2
    
    elif pos_x == 0:
        incr = (((pos_x+len(string_np)) % (len(string_np)+1)) + len(string_np) -2) // 2 + 2
    
    else:
        incr = (pos_x + len(string_np) - 2)//2 + 2
    
    return np.roll(string_np, -incr)


with open('input_21') as data:
    
    instructions_list = data.readlines()

passwd_history = [np.copy(string_np)]    
# Part 1
for instruction in instructions_list:
    if 'swap position' in instruction:
        x, y = [int(num) for num in re.search(r'(\d+) with position (\d+)', instruction).groups()]
        string_np = swap_pos(x, y)
        
    elif 'swap letter' in instruction:
        x, y = [char for char in re.search(r'(\w+) with letter (\w+)', instruction).groups()]
        string_np = swap_char(x, y)
        
    elif 'rotate right' in instruction:
        x = int(re.search(r'(\d+) steps?', instruction).group(1))
        string_np = rotate_right(x)
        
    elif 'rotate left' in instruction:
        x = int(re.search(r'(\d+) steps?', instruction).group(1))
        string_np = rotate_left(x)
        
    elif 'rotate based' in instruction:
        x = re.search(r'letter (\w+)', instruction).group(1)
        string_np = rotate_based_on_pos(x)
        
    elif 'reverse' in instruction:
        x, y = [int(num) for num in re.search(r'(\d+) through (\d+)', instruction).groups()]
        string_np = reverse_position(x, y)
        
    elif 'move' in instruction:
        x, y = [int(num) for num in re.search(r'(\d+) to position (\d+)', instruction).groups()]
        string_np = move_position(x, y)

    else:
        print('ERROR: ', instruction)
        
    passwd_history += [np.copy(string_np)]
        
print(''.join(string_np))
prev_instruction = None
    
# Part 2
input_str = 'fbgdceah'
string_np = np.array([char for char in input_str])

for idx, (instruction, old_passwd) in enumerate(zip(reversed(instructions_list), reversed(passwd_history))):
    
    if 'swap position' in instruction:
        y, x = [int(num) for num in re.search(r'(\d+) with position (\d+)', instruction).groups()]
        string_np = swap_pos(x, y)
        
    elif 'swap letter' in instruction:
        y, x = [char for char in re.search(r'(\w+) with letter (\w+)', instruction).groups()]
        string_np = swap_char(x, y)
        
    elif 'rotate right' in instruction:
        x = -int(re.search(r'(\d+) steps?', instruction).group(1))
        string_np = rotate_right(x)
        
    elif 'rotate left' in instruction:
        x = -int(re.search(r'(\d+) steps?', instruction).group(1))
        string_np = rotate_left(x)
        
    elif 'rotate based' in instruction:
        x = re.search(r'letter (\w+)', instruction).group(1)
        string_np = rotate_based_on_pos_reversed(x)
        
    elif 'reverse' in instruction:
        x, y = [int(num) for num in re.search(r'(\d+) through (\d+)', instruction).groups()]
        string_np = reverse_position(x, y)
        
    elif 'move' in instruction:
        y, x = [int(num) for num in re.search(r'(\d+) to position (\d+)', instruction).groups()]
        string_np = move_position(x, y)

    else:
        print('ERROR: ', instruction)
        
    prev_instruction = instruction
        

        
print(''.join(string_np))
            
