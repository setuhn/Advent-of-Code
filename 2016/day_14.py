# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:03:21 2023

@author: Setuhn
"""
import hashlib, re

salt = 'yjdafjpo'
index = 0

# A hash is a key only if:
# It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
# One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.
potential_keys = []
keys = []

while len(keys) < 64:
    salted_index = salt+str(index)

    hashed_salted_index = hashlib.md5(salted_index.encode()).hexdigest()
    
    # Part 2
    for _ in range(2016):
        hashed_salted_index = hashlib.md5(hashed_salted_index.encode()).hexdigest()
    
    removed_keys = []
    for pk in potential_keys:
        if index > pk[1]:
            removed_keys.append(pk)
            
        else:
            if re.search(rf'({pk[2]})\1\1\1\1', hashed_salted_index):
                keys.append(pk)
                removed_keys.append(pk)
                
    for k in removed_keys:
        potential_keys.remove(k)
    
    triplicate = re.search(r'(\w)\1\1', hashed_salted_index)
    
    if triplicate:
        potential_keys.append([index, 1000+index, triplicate.group(1), hashed_salted_index])
        
    index += 1

   
keys_id = [info[0] for info in keys]

# This is needed to get the id in the order they were drawn
print(sorted(keys_id)[63])