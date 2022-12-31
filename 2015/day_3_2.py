# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:44:36 2022

@author: Setuhn
"""

try:
    with open("input_3", 'r') as data:
        
        position = {True: {'x':0, 'y' :0}, False:{'x':0, 'y' :0}}
        who = True
        
        houses_delivered = list()
        houses_delivered.append(dict(position[who]))
        
        for line in data:
            for character in line:
                if character == '^':
                    position[who]['y'] += 1
                elif character == '>':
                    position[who]['x'] += 1
                elif character == '<':
                    position[who]['x'] -= 1
                elif character == 'v':
                    position[who]['y'] -= 1
                
                if position[who] not in houses_delivered:
                    houses_delivered.append(dict(position[who]))
                
                who = not who
                
        print(len(houses_delivered))           

                 
except Exception as e:
    print(e)