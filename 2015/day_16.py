#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 08:29:14 2023

@author: setuhnjimaja
"""
import re
aunts_dict = {}

with open('input_16') as data:
    for aunt_info in data.readlines():
        number = [word.strip(':') for idx, word in enumerate(aunt_info.strip().split(' ')) if idx == 1][0]
        categories = re.findall(r'\s([a-z]+): (\d+)', aunt_info)
        aunts_dict[number] = {}
        
        for name, num in categories:
            aunts_dict[number][name] = int(num)
            
ticker_tape = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1    
    }


# Part 1
for idx, aunt in aunts_dict.items():
    selected = True
    
    for item, number in aunt.items():
        
        if item in ticker_tape.keys() and number != ticker_tape[item]:
            selected = False
            break
        
    if selected:
        print('Answer to part 1:', idx)

# Part 2
for idx, aunt in aunts_dict.items():
    selected = True
    
    for item, number in aunt.items():
        
        if item in ticker_tape.keys():
            
            if item in ['cats', 'trees']:
                
                if number <= ticker_tape[item]:
                    selected = False
                    break
            
            elif item in ['pomeranians', 'goldfish']:
                
                if number >= ticker_tape[item]:
                    selected = False
                    break
            
            elif number != ticker_tape[item]:
                selected = False
                break
        
    if selected:
        print('Answer to part 2:', idx)
    