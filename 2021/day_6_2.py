# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 18:33:17 2022

@author: Setuhn
"""

def pop_growth(population):
    new_population = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    
    for days, number in population.items():
        
        if days > 0:
            new_population[days-1] += number
        
        else:
            new_population[6] += number
            new_population[8] += number
            
    
    
    return new_population
        
population = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

try:
    with open("input_6", 'r') as file_open:
        pop = [[int(p) for p in line.strip().split(',')] for line in file_open.readlines()][0]
        for p in pop:
                population[p] +=1
                
        for i in range(256):
            population = pop_growth(population)
            
        print(sum(population.values()))

    
except Exception as e:
    print(e)