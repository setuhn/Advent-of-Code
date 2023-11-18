# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 20:42:19 2023

@author: Setuhn
"""
import numpy as np

elf_number = 3004953

# Part 1
elf_list = np.arange(1, elf_number+1)

while len(elf_list) > 1:
    
    if len(elf_list) % 2 == 0:
        elf_list = elf_list[::2]
    else:
        elf_list = np.roll(elf_list[::2], 1)
    
print('Answer part 1:', elf_list[0])

# Part 2
def alternator(n):
    for i in range(n):
        if i % 2 == 0:
            yield 1
        else:
            yield -1


elf_list = np.arange(1, elf_number+1)
start_idx = elf_number//2
i = 0

while len(elf_list) > 1:
        
    if len(elf_list) % 2 == 0:
        incr = 1
        
    else:
        incr = 2
        
    a = np.arange(start_idx, len(elf_list), 3) 
    b = np.arange(start_idx+incr, len(elf_list), 3)
        
    
    idx_delete = np.empty((a.size + b.size,), dtype=a.dtype)
    
    idx_delete[0::2] = a
    idx_delete[1::2] = b
    
    elf_list = np.delete(elf_list, idx_delete)
    
    elf_list = np.roll(elf_list, (len(elf_list)-len(idx_delete)))

    start_idx = len(elf_list)//2
        
    if len(elf_list) == 2:
        elf_list = [elf_list[0]]
    
        
print('Answer part 2:', elf_list[0])