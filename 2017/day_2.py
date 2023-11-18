#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:51:41 2023

@author: setuhnjimaja
"""
checksum = 0
evenly_divisible_sum  = 0

with open('input_2') as data:
    for line in data.readlines():
        line_numbers = [int(num) for num in line.split()]
        
        checksum += (max(line_numbers) - min(line_numbers))
        
        idx_start = 0
        
        
        for num in line_numbers:
            idx_start += 1
            
            for idx in range(idx_start, len(line_numbers)):
                
                divider = sorted([num, line_numbers[idx]])
                
                if divider[1] % divider[0] == 0:
                    evenly_divisible_sum += divider[1]//divider[0]

                    break
        
print('Answer part 1:', checksum)
print('Answer part 2:', evenly_divisible_sum)