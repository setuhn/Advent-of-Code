# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:06:49 2023

@author: Setuhn
"""


black_list_intervals = []

with open('input_20') as data:
    
    for idx, line in enumerate(data.readlines()):
        start_interval, end_interval = [int(char) for char in line.split('-')]
        
        black_list_intervals += [(start_interval, end_interval, range(start_interval, end_interval+1))]

IP_addresses_number = 4294967295
black_list_intervals = sorted(black_list_intervals)

# Part 1
IP_address = 0
found = False

while not found:
    found = True
    
    for idx, ( _, _, inter) in enumerate(black_list_intervals):
        
        if IP_address in inter:
            
            IP_address = inter[-1]+1
            found = False
            
            break
        
print('Answer part 1:', IP_address)


# Part 2
black_list_concanated_intervals = []
idx_interval = 0

size = 0

while idx_interval+1 < len(black_list_intervals):
    
    # if boundary of lower interval is inside or touching the higher interval
    if black_list_intervals[idx_interval][1]+1 in black_list_intervals[idx_interval+1][2]:
        start_interval, end_interval = black_list_intervals[idx_interval][0], black_list_intervals[idx_interval+1][1]
        
        black_list_intervals[idx_interval] = (start_interval, end_interval, range(start_interval, end_interval+1))
        
        del black_list_intervals[idx_interval+1]
    
    # if lower interval is inside higher interval
    elif black_list_intervals[idx_interval][0] in black_list_intervals[idx_interval+1][2] and black_list_intervals[idx_interval][1] in black_list_intervals[idx_interval+1][2]:
        del black_list_intervals[idx_interval]
        idx_interval += 1
        
    # if higher interval is inside lower interval
    elif black_list_intervals[idx_interval+1][0] in black_list_intervals[idx_interval][2] and black_list_intervals[idx_interval+1][1] in black_list_intervals[idx_interval][2]:
        del black_list_intervals[idx_interval+1]
        
    # if intervals not joint:
    else:
        size += black_list_intervals[idx_interval+1][0] - black_list_intervals[idx_interval][1] - 1
        idx_interval += 1

   
print('Answer part 2:', size)