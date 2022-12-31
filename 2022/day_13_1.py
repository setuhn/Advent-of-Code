#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 08:34:45 2022

@author: setuhnjimaja
"""
import itertools

def are_pairs_right_order(left, right):
    
    for l, r in itertools.zip_longest(left, right):
        
        if l is None and r is not None:
            return True
        
        elif l is not None and r is None:
            return False
        
        elif type(l) == int and type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
            
        else:
            if type(l) == list and type(r) == int:
                result = are_pairs_right_order(l, [r])
                if result is not None: return result
            
            if type(l) == int and type(r) == list:
                result = are_pairs_right_order([l], r)
                if result is not None: return result
            
            if type(l) == list and type(r) == list:
                result = are_pairs_right_order(l, r)
                if result is not None: return result
                
    return None
            

with open('input_13') as data:
    packet_pairs = [[eval(pair_str.strip()) for pair_str in block.split('\n')] for block in data.read().strip('\n').split('\n\n')]
    
    
answer = 0
for idx, pp in enumerate(packet_pairs, 1):
    packet_left = pp[0]
    packet_right = pp[1]
    
    if are_pairs_right_order(packet_left, packet_right):
        answer += idx
        
print(answer)