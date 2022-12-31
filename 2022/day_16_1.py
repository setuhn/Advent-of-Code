# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 07:41:57 2022

@author: Setuhn
"""
import re

class Node:
    def __init__(self, connection: dict={}, flow: int=0):
        self.connections = connection # {name: min_hop}
        self.flow = flow
        
class Element_BFS:
    def __init__(self, node, distance = 0):
        self.node = node
        self.distance = distance

# Can be optimised by looking at past visited list for the Element_BFS with same node_goal to append the end of the path 
def shortest_path(node_start, node_goal, network, max_distance):
    i = 0
    # Create a queue for BFS
    q = []
    visited = []
    
    # Add first node into queue
    q.append(Element_BFS(node_start))
    visited.append(node_start)
    
    while q:
        i+=1
        element_curr = q.pop(0) # Dequeue the front cell
        
        # If we have reached the destination cell,we are done
        if element_curr.node == node_goal or element_curr.distance >= max_distance:
            return element_curr.distance
            
        else:  
            # Otherwise enqueue its adjacent cells
            for n in [node for node, value in network[element_curr.node].connections.items() if value == 1]:
                q.append(Element_BFS(n, element_curr.distance+1))
                visited.append(element_curr.node)
    
    return None

def create_generator(valves):
    for v in valves:
        yield v


def released_pressure_path(current_valve, remaining_valves, network, time, path, max_p):
    released_pressure = path[-1][1]
    
    if released_pressure > max_p: max_p = released_pressure
    
    for next_valve in remaining_valves:
        
        if next_valve not in network[current_valve].connections.keys():
            network[current_valve].connections[next_valve] = shortest_path(current_valve, next_valve, network, 30) 
        
        if time - network[current_valve].connections[next_valve] - 1 > 1:
            next_time = time - network[current_valve].connections[next_valve] - 1
            updated_released_pressure = released_pressure + network[next_valve].flow * next_time
            p = released_pressure_path(next_valve, [v for v in remaining_valves if v != next_valve], network, next_time, path+[[next_valve, updated_released_pressure]], max_p)

            if p > max_p: max_p = p
            
    return max_p

network = {}
valves = []

with open('input_16_test.txt') as data:
    for line in data.readlines():
        name = re.findall(r'(?<=^Valve\s)[A-Z]{2}', line)[0]
        flow = int(re.findall(r'(?<=rate=)\d+', line)[0])
        connections = {name:1 for name in re.findall(r'((?:[A-Z]{2})(?#,\s))+', line.split(';')[1])}
        
        network[name] = Node(connections, flow)
        
        if flow > 0:
            valves.append(name)

time = 30
released_pressure = 0
current_node = 'AA'

max_p = released_pressure_path(current_node, valves, network, time, [['AA', 0]], 0)
print(max_p)

# permutation of n elements without repetition = n!
# calculate the weighed value for each node (possible released pressure when moved with shortest path) 
# divide the set of nodes by x where x * y = n and keep 

# Calculate the hop values for each start/goal pair
# for node_start in valves + [current_node]:
    
#     for node_goal in valves:
        
#         if node_start != node_goal and node_goal not in network[node_start].connections.keys():
#             network[node_start].connections[node_goal] = shortest_path(node_start, node_goal, network, time)

# Creat permuation list
# perm = list(itertools.permutations(valves))
                
# Reopen pickled data
# with open('16.pickle', 'rb') as handle:
#     network = pickle.load(handle)