#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:17:04 2023

@author: setuhnjimaja
"""
# 1048320 too high
from numba import jit

@jit(nopython = True) 
def dividers_list(number):
    dividers = []
    
    for div in range(2, number//2+1):

            if number % div == 0:
                
                dividers.append(div)

    return dividers

@jit(nopython = True) 
def find_house_number(present_limit):
    house_number = 0
    presents = 0

    while presents < present_limit:
        house_number += 1
        dividers = dividers_list(house_number)
        presents = sum([div * 10 for div in dividers])
        
    return house_number, presents

print(find_house_number(34000000))
    