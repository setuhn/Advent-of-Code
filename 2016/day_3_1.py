# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 23:06:38 2023

@author: Setuhn
"""
impossible_counter = 0
triangles = []

with open('input_3') as data:
    
    for triangle in data.readlines():
        
        sides = [int(side) for side in triangle.strip().split()]
        sides.sort()
        triangles.append(sides)
        
        if sides[0] + sides[1] <= sides[2]:
            impossible_counter += 1
            
print(len(triangles) - impossible_counter)
            