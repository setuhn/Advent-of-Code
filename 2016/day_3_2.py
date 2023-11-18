# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 23:06:38 2023

@author: Setuhn
"""
import numpy as np


triangles = []

with open('input_3') as data:
    
    for triangle in data.readlines():
        
        sides = [int(side) for side in triangle.strip().split()]
        triangles.append(sides)
            
triangles_np = np.array(triangles)    

triangles_np_cut_h = np.hsplit(triangles_np, triangles_np.shape[1])
triangles_np_cut_hv = [np.vsplit(col, col.shape[0]//3) for col in triangles_np_cut_h]

impossible_counter = 0

for col in triangles_np_cut_hv:
    
    for row in col:
        
        sides = np.sort(row, axis = 0)
        
        if sides[0] + sides[1] <= sides[2]:
            impossible_counter += 1
            
print(len(triangles) - impossible_counter)