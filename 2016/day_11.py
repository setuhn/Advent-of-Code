# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 13:05:32 2023

@author: Setuhn
"""
import re, copy
import heapq

floors = [{}, {}, {}, {}]

# Determine if the new floor configuration is safe for all the microchips
def is_floor_safe(floor_num: int, supplem_material: dict) -> bool:
    new_floor = copy.deepcopy(floors[floor_num])
    
    new_floor['G'].extend(supplem_material['G'])
    new_floor['M'].extend(supplem_material['M'])
    
    for microchip in new_floor['M']:
        if microchip not in new_floor['G'] and len(new_floor['G']) > 0:
            return False
        
    return True

def gen_next_moves(current_floor_num, floors):
    pass

# floors is current configuration and current floor is the current level we're at
with open('input_11_test.txt') as data:
    for floor_num, line in enumerate(data.readlines()):
        line = line.strip()
        generators = [generator[0].upper() for generator in re.findall(r' (\w+) generator', line)]
        microchips = [microchip[0].upper() for microchip in re.findall(r' (\w+)-compatible', line)]
        
        floors[floor_num]['G'] = generators 
        floors[floor_num]['M'] = microchips
        


# the elevator capacity rating means it can carry at most yourself and two RTGs or microchips in any combination. 
# As a security measure, the elevator will only function if it contains at least one RTG or microchip
current_floor = 0
move_q = []

heapq.heappush(move_q, (0, (current_floor, floors, 0)))


# while not finished:
#     pass