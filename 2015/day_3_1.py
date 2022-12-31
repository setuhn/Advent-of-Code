# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 21:16:12 2022

@author: Setuhn
"""

try:
    with open("input_3", 'r') as data:
        
        position = {'x':0, 'y' :0}
        houses_delivered = list()
        houses_delivered.append(dict(position))
        
        for line in data:
            for character in line:
                if character == '^':
                    position['y'] += 1
                elif character == '>':
                    position['x'] += 1
                elif character == '<':
                    position['x'] -= 1
                elif character == 'v':
                    position['y'] -= 1
                
                if position not in houses_delivered:
                    houses_delivered.append(dict(position))
                
        print(len(houses_delivered))           

                 
except Exception as e:
    print(e)