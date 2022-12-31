#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 22:55:35 2022

@author: setuhnjimaja
"""

# base 5
# translation: 2, 1, 0, minus (written -), and double-minus (written =). Minus is worth -1, and double-minus is worth -2.
SNAFU_dict = {
    '2': 2, 
    '1': 1, 
    '0': 0, 
    '-': -1, 
    '=': -2
    }

dec_dict = {
    0: '0',
    1: '1',
    2: '2',
    3: '=',
    4: '-',
    }

def SNAFU_to_dec(number_SNAFU: str):
    number_dec = 0
    
    for i, n in enumerate([SNAFU_dict[n] for n in number_SNAFU[::-1]]):
        number_dec+= 5**i*n
        
    return number_dec

# base 3?
def dec_to_SNAFU(number_dec: int):
    remainder = number_dec
    number_SNAFU = ''
    
    while remainder != 0:
        mod = remainder%5
        remainder //= 5
        
        if mod > 2:
            remainder +=1
            
        number_SNAFU = dec_dict[mod]+number_SNAFU

        
    return number_SNAFU
    
    

answer_dec = 0

with open('input_25') as data:
    for line in data.readlines():
        answer_dec += SNAFU_to_dec(line.strip())
        
print(dec_to_SNAFU(answer_dec))
        
