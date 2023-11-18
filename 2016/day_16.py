# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 09:01:17 2023

@author: Setuhn
"""
from collections import deque

def gen_new_data(initial_state, disk_length):
    initial_state = [int(char) for char in str(initial_state)]
    
    while len(initial_state) < disk_length:
        next_state = [0 if num == 1 else 1 for num in reversed(initial_state)]
        initial_state = initial_state + [0] + next_state
        
        
    return initial_state[:disk_length]

# The checksum for some given data is created by considering each non-overlapping pair of characters in 
# the input data. If the two characters match (00 or 11), the next checksum character is a 1. If the characters 
# do not match (01 or 10), the next checksum character is a 0. This should produce a new string which is exactly 
# half as long as the original. If the length of the checksum is even, repeat the process until you end up with a 
# checksum with an odd length.

def checksum(data):
    
    checksum = deque(data)
    
    
    while len(checksum)%2 == 0:
        
        next_checksum = deque()
        
        while checksum:
            chunk = [checksum.popleft(), checksum.popleft()]
            
            if sum(map(lambda x : x == 0, chunk)) % 2 == 0:
                next_checksum.append(1)
                
            else:
                next_checksum.append(0)
                
        checksum = next_checksum
              
    else:
        return checksum

initial_state = 10111011111001111
disk_length = 35651584

data = gen_new_data(initial_state, disk_length)

checksum = checksum(data)


for num in checksum:
    print(num, end='')