# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 08:27:38 2022

@author: Setuhn
"""

def game_points(input_game):
    
    game_rules_output = {
        'A': 'R',
        'X': 0,
        'B': 'P',
        'Y': 3,
        'C': 'S',
        'Z': 6
        }
    
    game_rules_input = {
        'R': {0: 3, 3: 1, 6: 2},
        'P': {0: 1, 3: 2, 6: 3},
        'S': {0: 2, 3: 3, 6: 1}
        }
    
    
    points = game_rules_output[input_game[1]]
    opponent_play = game_rules_output[input_game[0]]
    points += game_rules_input[opponent_play][points]
        
        
    

            
    return points


try:
    with open("input_2", 'r') as file_open:
        file_txt = sum([game_points(line.strip().split()) for line in file_open.readlines()])
        
        print(file_txt)
        

except Exception as e:
    print(e)