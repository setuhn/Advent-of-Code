# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 20:28:13 2022

@author: Setuhn
"""

try:
    with open("input_7", 'r') as file_open:
        position = [int(pos) for pos in file_open.read().strip().split(',')]
        
        min_fuel = 1000000000
        pos_chosen = 0
        
        for pos_final in position:
            fuel = 0
            for pos_move in position:
                fuel += abs(pos_final-pos_move)
            
            if fuel < min_fuel:
                pos_chosen = pos_final
                min_fuel = fuel
                
        print(pos_chosen, min_fuel)
        
except Exception as e:
    print(e)