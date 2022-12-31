#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 08:46:32 2022

@author: setuhnjimaja
"""
from itertools import permutations

def generate_arrangements(people):
    arrange = list(people.keys())
    arrangements = [arrange.copy()]
    
    same = False
    
    while not same:
        arrange.insert(1, arrange.pop())
        
        if arrange == arrangements[0]:
            same = True
            
        else:
            arrangements.append(arrange.copy())
            
    return arrangements
        
def calculate_happiness(arrange, people):
    happiness = 0
    
    for person_left, person, person_right in [(arrange[idx-1], name, arrange[idx+1 if idx+1 < len(arrange) else 0]) for idx, name in enumerate(arrange)]:
        happiness += people[person][person_left] + people[person][person_right]
        
    return happiness

def calculate_happiness_max(arrangements, people):
    happiness_max = 0
    
    for arrange in arrangements:
        happiness = calculate_happiness(arrange, people) 
        
        if happiness > happiness_max: 
            happiness_max = happiness

    return happiness_max
        
people = {}

with open('input_13') as data:
    for line in data.readlines():
        words = line.strip('.\n').split(' ')
        names = [name for idx, name in enumerate(words) if idx in [0, len(words)-1]]
        
        happiness = int(words[3]) if'gain' in words else -int(words[3])
        
        if names[0] not in people.keys():
            people[names[0]] = {}
            
        people[names[0]][names[1]] = happiness 

# Part 1:
arrangements = list(permutations(people.keys(), len(people))) 
happiness_max_1 = calculate_happiness_max(arrangements, people)     
print('Answer part 1:', happiness_max_1)

# Part 2:
people['me'] = {}
for name in [p for p in people.keys() if p != 'me']:
    people['me'][name] = 0
    people[name]['me'] = 0

arrangements = list(permutations(people.keys(), len(people)))     
happiness_max_2 = calculate_happiness_max(arrangements, people)  
   
print('Answer part 2:', happiness_max_2)


