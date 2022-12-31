# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:45:25 2022

@author: Setuhn
"""

try:
    with open("input_4", 'r') as file_open:
        assignments_list = [[assignment.strip().split('-') for assignment in line.strip().split(',')] for line in file_open.readlines()]
        
        counter = 0
        
        for assignment in assignments_list:
            i1, f1 = int(assignment[0][0]), int(assignment[0][1])
            i2, f2 = int(assignment[1][0]), int(assignment[1][1])
            
            if (i1 >= i2 and f1 <= f2) or (i2 >= i1 and f2 <= f1):
                counter += 1
        
        print(counter)

                 
except Exception as e:
    print(e)