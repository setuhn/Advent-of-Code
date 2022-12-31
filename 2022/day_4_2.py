# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:56:08 2022

@author: Setuhn
"""

try:
    with open("input_4", 'r') as file_open:
        assignments_list = [[assignment.strip().split('-') for assignment in line.strip().split(',')] for line in file_open.readlines()]
        
        counter = 0
        
        for assignment in assignments_list:
            a1 = range(int(assignment[0][0]), int(assignment[0][1])+1)
            a2 = range(int(assignment[1][0]), int(assignment[1][1])+1)
            
            if set(a1).intersection(a2):
                counter += 1
                                    
        print(counter)

                 
except Exception as e:
    print(e)