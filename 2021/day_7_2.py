# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 20:35:11 2022

@author: Setuhn
"""

def fuel_consumption(pos_start, pos_end):
    
    return sum(range(1, abs(pos_start-pos_end)+1))
    

try:
    with open("input_7", 'r') as file_open:
        position = [int(pos) for pos in file_open.read().strip().split(',')]
        
        fuel = []
        for pos_final in range(1, max(position)+1):
            
            fuel += [sum([fuel_consumption(pos_move, pos_final) for pos_move in position])]
                
        min_fuel = min(fuel)
        
        print(fuel.index(min_fuel)+1, min_fuel)
        
except Exception as e:
    print(e)