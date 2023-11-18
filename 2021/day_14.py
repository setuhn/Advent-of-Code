#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 20:40:21 2023

@author: setuhnjimaja
"""

insertion_instruction = {}
polymer_template = None

def chop_polymer_template(polymer_template):
    
    polymer = {}
    keys = []
    for i in range(len(polymer_template)-1):
        keys += [polymer_template[i:i+2]]


    for k in keys:
        if k not in polymer.keys():
            polymer[k] = 0
            
        polymer[k] += 1
        
    return polymer
    

with open('input_14') as data:
    
    for line in data.readlines():
        line = line.strip()
        
        if '->' in line:
            pair, insertion = line.split(' -> ')
            
            if pair not in insertion_instruction.keys():
                insertion_instruction[pair] = []
                
            insertion_instruction[pair] = insertion
            
        elif line:
            polymer_template = line
            
 
# Chop the polymer_tmeplate into list of pairs:
polymer = chop_polymer_template(polymer_template)
step = 40

for _ in range(step):
    # Creat a new polymer dictionary to write the modifications
    polymer_new = polymer.copy()
    
    for key in insertion_instruction.keys():
        
        # if an insetion keyy is found in the polymer, substract the number of key and create the new keys from the insertion (AB -> Y becomes AY and YB) 
        if key in polymer.keys():
            
            polymer_new[key] -= polymer[key]
            
            new_keys = (key[0]+insertion_instruction[key], insertion_instruction[key]+key[1])
            
            if new_keys[0] not in polymer_new.keys():
                polymer_new[new_keys[0]] = 0
                
            if new_keys[1] not in polymer_new.keys():
                polymer_new[new_keys[1]] = 0
                
            polymer_new[new_keys[0]] += polymer[key]
            polymer_new[new_keys[1]] += polymer[key]
    
    # The new polymer becomes the current one
    polymer = polymer_new.copy()

# Find all the different individual letters (elements)and creat a counter
elements = set(''.join(polymer.keys()))
counter = {elem: 0 for elem in elements}

# count the number of time the elements are found in the polymer key and uoltiply by the number of key (value)
for key in polymer.keys():

    for elem in counter.keys():
        counter[elem] += key.count(elem) * polymer[key]

# Add the first an last element       
counter[polymer_template[0]] += 1   
counter[polymer_template[-1]] += 1  

# As each element is part of 2 key, divide the final counter by 2

for elem in counter.keys():
    counter[elem] //= 2

elem_max = max(counter.values())
elem_min = min(counter.values())

print(f'Answer: {elem_max - elem_min}')