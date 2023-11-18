# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 08:36:27 2023

@author: Setuhn
"""
import re

discs = []
with open('input_15') as data:
    
    for line in data.readlines():
        discs.append([int(position) for position in re.search(r' (\d+) positions.* position (\d+)', line.strip()).groups()])


# Part 2
discs.append([11, 0])


t = 0
positions = [1]*len(discs)

while True:
    
    
    for idx, d in enumerate(discs):
        positions[idx] = (d[1] + t + idx + 1)%d[0]
        
    if positions.count(0) == len(discs):
        break
    
    else:
        t += 1

print(t)
        