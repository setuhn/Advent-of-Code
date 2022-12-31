# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:31:36 2022

@author: Setuhn
"""

import numpy as np

def crawler_3D(start, cube):
    # Create a queue 
    q = []
    visited = []
    counter = 0
    
    # Add first node into queue
    q.append(start)
    visited.append(start)
    
    # If the queue is empty we are done
    while q:
        
        element_curr = q.pop(0) # Dequeue the front cell
        
        mvm_map = [
            [1, 0, 0],
            [0, 0, 1],
            [0, 1, 0],
            [-1, 0, 0],
            [0, 0, -1],
            [0, -1, 0]
            ]
        # iterate through the adjacent cells (if ==1, increase counter, if not visited: add to queue)
        for x, y, z in [(element_curr[0] + mvm[0], element_curr[1] + mvm[1], element_curr[2] + mvm[2]) for mvm in mvm_map if 0 <= element_curr[0] + mvm[0] < cube.shape[0] and 0 <= element_curr[1] + mvm[1] < cube.shape[1] and 0 <= element_curr[2] + mvm[2] < cube.shape[2]]:

                if cube[x, y, z] == 1:
                    counter +=1
                
                elif cube[x, y, z] == 0:
                    q.append((x, y, z))
                
                    cube[x, y, z] = 2 # droplet won't be visited again
                    
        
    print(counter)
    
    return visited
    
droplet_coor = []
max_coor = [0, 0, 0]

# Read input    
with open('input_18') as data:
    for cube in data.readlines():
        cube_coor = tuple((int(coor)+1 for coor in cube.split(','))) # shift the coordinate by one to pad the volume with an empty plane
        droplet_coor.append(cube_coor)
        
        for idx in range(len(max_coor)):
            if cube_coor[idx]+2 > max_coor[idx]:
                max_coor[idx] = cube_coor[idx]+2

droplet_np = np.full((max_coor), 0)      
  
for cube_coor in droplet_coor:
    droplet_np[cube_coor] = 1
    
# 3D crawler that can't go through 1s and increments everytime is touches a 1
start = (0,0,0)
visited = crawler_3D(start, droplet_np)
