# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def compute_cycle(cycle, n, answer, X):
    if cycle in n:
        answer += X*cycle
        
    return answer
        
with open("input_10", 'r') as data:
    X = 1
    n = [20, 60, 100, 140, 180, 220]
    cycle = 0
    answer = 0
     
     
    for instruction in data.readlines():
        if 'addx' in instruction:
            
            cycle +=1
            answer = compute_cycle(cycle, n, answer, X)
            cycle +=1
            answer = compute_cycle(cycle, n, answer, X)
            
            X += int(instruction.split()[1])
            
        else:
           cycle +=1
           answer = compute_cycle(cycle, n, answer, X)
            
    print(answer)
             
         
     