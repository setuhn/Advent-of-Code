# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def game_points(input_game):
    
    game_rules = {
        'A': ['R', 1],
        'X': ['R', 1],
        'B': ['P', 2],
        'Y': ['P', 2],
        'C': ['S', 3],
        'Z': ['S', 3]
        }

    rps = [None, None]
    points = 0
    
    for i, inp in enumerate(input_game):
        rps[i] = game_rules[inp][0]
        if i == 1:
            points += game_rules[inp][1]
            
    if rps[0] == rps[1]:
        points += 3
        
    elif rps in [['S', 'R'], ['P', 'S'], ['R', 'P']]:
       points += 6 
    
    
    return points


try:
    with open("input_2", 'r') as file_open:
        file_txt = sum([game_points(line.strip().split()) for line in file_open.readlines()])
        
        print(file_txt)
        

except Exception as e:
    print(e)