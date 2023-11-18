#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 10:00:22 2023

@author: setuhnjimaja
"""
import re
import heapq

def replace_str(substr_new, string, idx, length_old_substr):
    
    return string[:idx] + substr_new + string[idx + length_old_substr:]

def score_calculator(molecule_current, molecule):
    score = 0
    
    for idx, char in enumerate(molecule_current):
        if char == molecule[idx]:
            score += 1
            
        if molecule_current[-idx] == molecule[-idx]:
            score += 1
            
    return score

def get_new_molecules(molecule_current, dead_ends_list_current, replacements):
    
    molecules_new_list = []
    
    for origin_frag, new_frag in replacements:
        len_og = len(origin_frag)
        
        dead_ends_list_new = dead_ends_list_current.copy()
        
        if new_frag in dead_end_fragments:
            dead_ends_list_new[new_frag] +=1
                     
        for iter_i in regex_origin_fragments[origin_frag].finditer(molecule_current):
            
            idx = iter_i.start()

            
            molecules_new_list += [(replace_str(new_frag, molecule_current, idx, len_og), dead_ends_list_new)]
            
    return molecules_new_list


    
def get_dead_end_frag(molecule):
    molecule_dead_ends = {}
    
    for frag in dead_end_fragments:
        if len(frag) > 1:
            molecule_dead_ends[frag] = molecule.count(frag)
        
        else:
            molecule_dead_ends[frag] = len(regex_dead_end_fragments[frag].findall(molecule))
        
    return molecule_dead_ends

replacements = {}
replacements_2 = []

# TODO: rewrite to work with list instead of string
with open('input_19') as data:
    for line in data.readlines():
        line = line.strip()
        
        if '=>' in line:
            frag_origin, frag_new = line.split(' => ')
            
            frag_new = re.findall(r'[A-Z][a-z]?', frag_new)
            
            if frag_origin not in replacements.keys():
                replacements[frag_origin] = []
            
            replacements[frag_origin] += [frag_new]
            
            replacements_2 += [(frag_origin, frag_new)]
        
        elif line:
            molecule_target = re.findall(r'[A-Z][a-z]?', line)

# Part 1
new_molecules_list = []
new_molecules = set()

for origin_frag, new_frag in replacements_2:
    
    for idx in [i.start() for i in re.finditer(origin_frag,  ''.join(molecule_target))]:
        
        new_molecules.add(replace_str(''.join(new_frag),  ''.join(molecule_target), idx, len(origin_frag)))
        

for idx, elem in enumerate(molecule_target):
    
    if elem in replacements.keys():
        
        for frag_new in replacements[elem]:
            
            new_molecule = replace_str(frag_new,  molecule_target, idx, len(elem))
            
            if ''.join(new_molecule) not in new_molecules:
                print(''.join(new_molecule[:10]))
            
            if new_molecule not in new_molecules_list:
            
                new_molecules_list += [new_molecule]
                


print('Answer part 1:', len(new_molecules_list))

# Part 2
# A* on the possible transformations
# Prune the branches with more 'unreduceable' (dead-end) elements than the target molecule

# A list of the elements that can be changed
elements = []

for origin_frag, _ in replacements:
    if origin_frag not in elements:
        elements.append(origin_frag)

# A list of the unmutable ('unreduceable', dead-end) elements which can't be removed after being introduced'   
dead_end_fragments = []    
# Precompile the regex for the different origin_frag as they will used a lot        
regex_origin_fragments = {}    
# Precompile the regex for the different dead ends as they will used a lot        
regex_dead_end_fragments = {}

for origin_frag, new_frag in replacements:
    frags = re.findall(r'[A-Z][a-z]?', new_frag)
    regex_origin_fragments[origin_frag] = re.compile(f'{origin_frag}([A-Z]|$)')
    
    for f in frags:
        if f not in elements and f not in dead_end_fragments :
            dead_end_fragments.append(f)
            regex_dead_end_fragments[f] = re.compile(f'{f}([A-Z]|$)')

           
    
            
# A dicitionary of the dead-end fragments and their number in the target molecule
molecule_dead_ends = get_dead_end_frag(molecule_target)

frag_start = 'e'

molecule_q = []
heapq.heappush(molecule_q, (0, (0, frag_start, get_dead_end_frag(frag_start))))

visited = []

len_target = len(molecule_target)

a = 0
while molecule_q:
    a+=1
    
    _, (steps_current, molecule_current, dead_ends_list_current) = heapq.heappop(molecule_q)
    
    if molecule_current == molecule_target:
        print('Answer part 2:', steps_current)
        break
    
    molecules_new_list = get_new_molecules(molecule_current, dead_ends_list_current, replacements)
    
    for molecule_new, molecule_new_dead_ends in molecules_new_list:
    
        steps_new = steps_current + 1
        
        
        # check if the current molecule hasn't been analysed before and that its length is lower or equal to the target molecul and that the deadend fragments are not too numerous
        if (molecule_new, steps_new) not in visited and len(molecule_new) <= len_target:
            
            over = False
            
            for frag_de in dead_end_fragments:
                
                if molecule_new_dead_ends[frag_de] > molecule_dead_ends[frag_de]:
                    over = True
                    break
                
            if over:
                continue
            
            # score to measure how close to the final molecule it is 
            score = - score_calculator(molecule_new, molecule_target)
                
            heapq.heappush(molecule_q, (score, (steps_new, molecule_new, molecule_new_dead_ends)))
            visited += [(molecule_new, steps_new)]
                