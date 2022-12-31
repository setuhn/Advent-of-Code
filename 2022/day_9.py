# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 08:13:15 2022

@author: Setuhn
"""

def move_head(position_head, direction):
    position = list(position_head)
    if direction == 'R':
        position[0] += 1
    
    elif direction == 'L':
        position[0] -= 1
    
    elif direction == 'U':
        position[1] += 1
    
    elif direction == 'D':
        position[1] -= 1
        
    return position

def is_adjacent(position_head, position_tail):
    
    if position_head == position_tail:
        return True
    
    elif (position_tail[0]-1 <= position_head[0] <= position_tail[0]+1) and (position_tail[1]-1 <= position_head[1] <= position_tail[1]+1):
        return True
    
    else:
        return False
    
def move_tail(position_1, position_2):
    position_head = list(position_1)
    position_tail = list(position_2)
    
    if not is_adjacent(position_head, position_tail):
        
        # If head and tail on same row/column, tail moves in a straight line
        if position_tail[0] == position_head[0]:
            if position_tail[1] < position_head[1]:
                position_tail[1] += 1
            
            else:
                position_tail[1] -= 1
                
        elif position_tail[1] == position_head[1]:
            if position_tail[0] < position_head[0]:
                position_tail[0] += 1
            
            else:
                position_tail[0] -= 1
        
        # Otherwise tail moves diagonally
        elif position_head[0] > position_tail[0]+1:
            
            position_tail[0] += 1 
            if position_head[1] > position_tail[1]:
                position_tail[1] +=1
            else:
                position_tail[1] -= 1 
                
        elif position_head[0] < position_tail[0]-1:
            position_tail[0] -= 1 
            if position_head[1] > position_tail[1]:
                position_tail[1] +=1
            else:
                position_tail[1] -= 1
                
        elif position_head[1] > position_tail[1]+1:
            
            position_tail[1] += 1 
            if position_head[0] > position_tail[0]:
                position_tail[0] +=1
            else:
                position_tail[0] -= 1 
                
        elif position_head[1] < position_tail[1]-1:
            position_tail[1] -= 1 
            if position_head[0] > position_tail[0]:
                position_tail[0] +=1
            else:
                position_tail[0] -= 1
        
    return position_tail
    
def update_list_position_tail(list_position_tail, position_tail):
    position = (position_tail[0], position_tail[1])
    
    if position in list_position_tail.keys():
        list_position_tail[position] += 1
    
    else:
        list_position_tail[position] = 1
    
with open("input_9", 'r') as data:
    n = 2 # number of nodes
    positions = [[0, 0]] * n # x(R, L), y(U, D)
    list_position_tail = {}
    update_list_position_tail(list_position_tail, positions[-1])
    
    for move in data.readlines():
        direction, number = move.split()
        
        for _ in range(int(number)):
            positions[0] = move_head(positions[0], direction)
            
            for i in range(1, len(positions)):
                positions[i] = move_tail(positions[i-1], positions[i])
                
            update_list_position_tail(list_position_tail, positions[-1])

    print(len(list_position_tail))