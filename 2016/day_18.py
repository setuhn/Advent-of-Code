# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:56:40 2023

@author: Setuhn
"""

# Then, a new tile is a trap only in one of the following situations:
# Its left and center tiles are traps, but its right tile is not.
# Its center and right tiles are traps, but its left tile is not.
# Only its left tile is a trap.
# Only its right tile is a trap.

trap_sequences = [
 [1, 1, 0],
 [0, 1, 1],
 [1, 0, 0],
 [0, 0, 1]
 ]

def gen_next_trap_col(map_line):
    imaginary_line = [0] + map_line + [0]
    new_line = []
    
    for tile_idx in range(len(imaginary_line)-2):
        
        if imaginary_line[tile_idx:tile_idx+3] in trap_sequences:
            new_line += [1]
            
        else:
            new_line += [0]
            
    return new_line

with open('input_18') as data:
    
    map_trap = [0 if char == '.' else 1 for char in data.read().strip()]

rows = 400000
safe_tiles = 0

for line_idx in range(rows):
    safe_tiles += map_trap.count(0)
    map_trap = gen_next_trap_col(map_trap)
    
print(safe_tiles)    


