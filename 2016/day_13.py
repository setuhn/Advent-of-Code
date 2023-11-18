# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 16:05:28 2023

@author: Setuhn
"""
import numpy as np

favorite_number = 1350
movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
office = np.zeros((100, 100))

# Find x*x + 3*x + 2*x*y + y + y*y.
# Add the office designer's favorite number (your puzzle input).
# Find the binary representation of that sum; count the number of bits that are 1.
#     If the number of bits that are 1 is even, it's an open space.
#     If the number of bits that are 1 is odd, it's a wall.
def is_wall(x: int, y: int):
    if bin((x*x + 3*x + 2*x*y + y + y*y) + favorite_number).count('1') % 2 == 0:
        return False
    
    else:
        return True

def get_next_steps(current_pos: list) -> list:
    next_positions = []
    
    for move in movements:
        x, y = [axis+incr for axis, incr in zip(current_pos, move)]

        if 0 <= x < len(office) and 0 <=  y < len(office):
            
            if office[y,  x] == 0:
                next_positions.append([x, y])
                
    return next_positions
        
for x in range(office.shape[1]):
    for y in range(office.shape[0]):
        office[y, x] = 1 if is_wall(x, y) else 0
        
start_pos = [1, 1]
end_pos = [31,39]
positions_q = [(start_pos, 0)]
visited_pos = []

while positions_q:
    current_pos, steps = positions_q.pop(0)
    
    # Part 1
    # if current_pos == end_pos:
    #     print(steps)
    #     break

    # Part 2
    if steps == 50:
        print(len(visited_pos))
        break
    
    next_positions = get_next_steps(current_pos)
    
    for next_pos in next_positions:
        if next_pos not in visited_pos:
            positions_q.append((next_pos, steps+1))
            visited_pos.append(next_pos)
        