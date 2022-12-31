# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
import numpy as np
import math

def production(inventory, robots_list):
    for idx, robot_n in enumerate(robots_list):
        inventory[idx] += robot_n

# verify if it is possible to buy the new robot
# if true: substract the cost of the new robot and return the new inventory along with the new robot int
# else: return the previous inventory along with -1 (no robot built)     
def construct_robot(robot_type, blueprint, inventory):
    new_inventory = inventory - blueprint[robot_type]
    
    if np.count_nonzero(new_inventory <0) == 0:
        return new_inventory, robot_type 
    
    else:
        return inventory, -1

# return the list of robot type that can be built with the current production line 
#TODO: add the time needed to build
def possible_robot_construction(blueprint, robots_list,inventory, time):
    possible = []
    
    for robot, cost in blueprint.items():
        bool_arr = cost > 0
        # keep only the robot that can be built from the current extracted resources
        c = cost[bool_arr]
        r = robots_list[bool_arr]
        i = inventory[bool_arr]
        # check that we have at least one robot of for each resources type that's needed
        if np.count_nonzero(r == 0) == 0:
            t = math.ceil(max((c-i)/r))
            building_time = t if t > 0 else 1
            
            if time - building_time > 0:
            
                possible.append((robot, building_time))
        
    return possible
        

blueprint = {}
inventory =  np.zeros(4, dtype=np.int64)
resources = ['ore', 'clay', 'obsidian', 'geode']

robots_list = np.array([1, 0, 0, 0], dtype=np.int64)

with open('input_19_test.txt')as data:
    for line in data.readlines():
        line = line.strip()
        name, line = line.split(':')
        name = int(name.split(' ')[1])
        blueprint[name] = {}
        
        robots = [b.strip() for b in line.strip().split('.')][:-1]
        
        for r in robots:
            robot_type , cost= r.split('Each')[1].split('costs')
            robot_type = resources.index(robot_type.strip().split(' ')[0])
            blueprint[name][robot_type] = []
            
            cost_str = [c.split(' ') for c in re.findall(r'\d+ [a-z]+', cost)]
            cost = np.zeros(4, dtype=np.int64)

            for idx, res in enumerate(resources):
                for cstr in cost_str:
                    if res in cstr[1]: 
                        cost[idx] = int(cstr[0])
                    
                
            blueprint[name][robot_type] = cost

time = 24
new_robot_type = None

# if robot cost R and we have X amount of robot, no more robots
# proritize how many are needed by ratio
# iterate over how much time is needed to make the next R_type of robot (check robots_cost against robots_list -> production)
# find more reasons to prune the branches

list_construction = []
q = []
start = (time, inventory, -1, robots_list)

q.append(start) 

i=0
inventory = np.array([0, 0, 0, 0])

# Pre-order traversal visit node, DFS, stack data, LIFO (Last In First Out)




# while(q):
#     i+=1
    
#     curr_time, curr_inventory, curr_new_robot_type, curr_robots_list = q.pop(0) # Dequeue the front cell
    
    
#     # update robot list
#     if curr_new_robot_type >= 0:
#         curr_robots_list[curr_new_robot_type] += 1
#         curr_new_robot_type = -1
        
#     # update inventory list
#     production(curr_inventory, curr_robots_list)
    
    
    
#     # check which robots can be built with the current production line:
#     possible_robots = possible_robot_construction(blueprint[1], curr_robots_list, inventory, time)
    
#     for next_robot_type, building_robot_time in possible_robots:
#             time = curr_time-building_robot_time
            
#             next_inventory = curr_inventory - blueprint[1][next_robot_type]

#             if (next_robot_type, building_robot_time) not in list_construction:
                
#                 q.append((time, next_inventory, next_robot_type, curr_robots_list.copy()))
#                 list_construction.append((next_robot_type, building_robot_time))

    