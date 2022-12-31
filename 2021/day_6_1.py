# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 17:19:16 2022

@author: Setuhn
"""

def pop_growth(population):
    new_pop = 0
    
    for i, fish in enumerate(population):
        if fish > 0:
            population[i] -= 1
        
        else:
            population[i] = 6
            new_pop += 1
            
    population.extend([8]*new_pop)
    
    return population
        

try:
    with open("input_6", 'r') as file_open:
        population = [[int(p) for p in line.strip().split(',')] for line in file_open.readlines()][0]
    
    for i in range(80):
        population = pop_growth(population)
    
    print(len(population))
    
except Exception as e:
    print(e)