#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 00:38:01 2022

@author: setuhnjimaja
"""

import re
import json

def extract_numbers(string):
    numbers_list = [int(number) for number in re.findall(r'-?\d+', string)]
    
    return numbers_list

def extract_numbers_no_red(string):
    value = 0
    
    if isinstance(string, dict):
        
        if not ('red' in string.keys() or 'red' in string.values()):
            
            for val in string.values():
                value += extract_numbers_no_red(val)

    elif isinstance(string, list):
        for item in string:
            value += extract_numbers_no_red(item)
            
    elif isinstance(string, int):
        value += string
        
    return value

def parser(string):
    
    content = json.loads(string)
    
    return content

with open('input_12') as data:
    string = data.read()
    answer_1 = sum(extract_numbers(string))
    
    answer_2 = extract_numbers_no_red(parser(string))
    
print('Answer part 1:', answer_1)
print('Answer part 2:', answer_2)
