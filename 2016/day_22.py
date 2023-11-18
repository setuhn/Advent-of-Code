# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 09:15:40 2023

@author: Setuhn
"""
import re
import heapq
 # Size  Used  Avail  Use%
# /dev/grid/node-x0-y0     91T   66T    25T   72%

class Node:
    def __init__(self, size: int, used_mem: int, avail_mem: int, used_mem_perc: int):
        self.size = size
        self.used_mem = used_mem
        self.avail_mem = avail_mem
        self.used_mem_perc = used_mem_perc

# return a list of tuple of Node where the first item has less used_mem than 
# the avail_mem of the second item i.e. the content of the first item can be 
# transferred into the second item
def get_viable_pairs(nodes: dict) -> list:
    pairs = []

    for n_1 in nodes.values():
        
        if n_1.used_mem != 0:
        
            for n_2 in nodes.values():
                
                if n_1 is not n_2 and n_1.used_mem <= n_2.avail_mem:
                    
                    pairs += [(n_1, n_2)]
                    
    return pairs

# Return a list of the adjacent nodes' position if the neighbours memory use is smaller than the available memory in the current position
def get_viable_neighbours(pos_current: tuple, pos_list: list, nodes: dict) -> list:
    
    row, col = pos_current
        
    return [pos_n for pos_n in [(row+1, col), (row, col+1), (row-1, col), (row, col-1)] if pos_n in pos_list and nodes[pos_n].used_mem <= nodes[pos_current].avail_mem]

# Return the Manhattan distance of 2 positions               
def distance_from(pos_i: tuple, pos_f: tuple) -> int:
    return abs(pos_i[0]-pos_f[0]) + abs(pos_i[1]-pos_f[1])

nodes_init = {}
pos_limits_array = [0, 0]

with open('input_22') as data:
    for node in data.readlines():
        if 'node' in node:
            col, row, size, use, avail, use_pc = [int(num) for num in re.search(r'x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%', node).groups()]
            
            node = Node(size, use, avail, use_pc)
            
            nodes_init[(row, col)] = node
            
            if row > pos_limits_array[0]: pos_limits_array[0] = row
            if col > pos_limits_array[1]: pos_limits_array[1] = col
            
            if use == 0:
                pos_zero = (row, col)
                
del col, row, node, size, use, avail, use_pc, data

# Part 1
pairs = get_viable_pairs(nodes_init)
print('Answer part 1:', len(pairs))

# Part 2: after analysis there is only one celle that can exchange data and it's empty. Check necighbours only for this one

# Save the list of keys as they won't change and they will be used a lot
pos_list = list(nodes_init.keys())

# Empty queue for the A*
path_q = []

# starting conditions
pos_start = data_pos  = (0, pos_limits_array[1])
pos_end = (0,0)

data_node = nodes_init[data_pos]
data_size = data_node.used_mem

#  Push in the heap queue: (-distance, score, (pos_start, pos_zero, steps_current, nodes_current, history))
heapq.heappush(path_q, ( 0, 0, (pos_start, pos_zero,  0, nodes_init.copy(), [])))

visited = []
found = False
steps_min = pos_limits_array[0] * pos_limits_array[1]


while path_q:
    
    distance, _, (pos_data, pos_zero, steps_current, nodes_current, history) = heapq.heappop(path_q)
    
    if pos_data == pos_end:
        print('Answer part 2:', steps_current)
        found = True
        break
    
    # get the neighbours of the zero node and send data there
    for pos_node_send in get_viable_neighbours(pos_zero, pos_list, nodes_current):
        
        nodes_next = nodes_current.copy()
        
        nodes_next[pos_node_send], nodes_next[pos_zero] = nodes_next[pos_zero], nodes_next[pos_node_send]
        
        pos_data_next = pos_data
        pos_zero_next = pos_node_send
        distance_next = distance
        steps_next = steps_current+1
        
        if pos_data == pos_node_send:
            pos_data_next = pos_zero
            distance_next -= 1
            
            if (distance_from(pos_data_next, pos_end) > distance_from(pos_data, pos_end)):
                continue
            
        score = distance_from(pos_data_next, pos_end) + distance_from(pos_zero_next, pos_data_next)
        
        history_next = history + [(pos_zero_next, pos_data_next, steps_next)]
        
        if (pos_data_next, pos_zero_next) not in visited:
            
            heapq.heappush(path_q, (distance_next, score, (pos_data_next, pos_zero_next, steps_next, nodes_next, history_next)))
            
            visited += [(pos_data_next, pos_zero_next)]
                    
if not found:
    print('ERROR queue empty')
    print(pos_data, pos_zero)
    
    
    