#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:23:31 2023

@author: setuhnjimaja
"""
from collections import deque

def calc_captcha_part_1(num: str):
    num_dq = deque(int(n) for n in num)
    double_int_sum = 0

    for _ in range(len(num_dq)):
        if num_dq[0] == num_dq[1]:
            double_int_sum += num_dq[0]
            
        num_dq.rotate(1)
    
    return double_int_sum

def calc_captcha_part_2(num: str)  :
    num_dq = deque(int(n) for n in num)
    double_int_sum = 0
    
    idx_half = len(num_dq)//2
    
    for _ in range(len(num_dq)):
        if num_dq[0] == num_dq[idx_half ]:
            double_int_sum += num_dq[0]
            
        num_dq.rotate(1)
    
    return double_int_sum
    
    
with open('input_1') as data:
    captcha = data.read().strip()    
    
# captcha = '12131415'
print('Answer part 1: ', calc_captcha_part_1(captcha))
print('Answer part 2: ', calc_captcha_part_2(captcha))