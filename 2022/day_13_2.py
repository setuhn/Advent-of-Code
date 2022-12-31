#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 09:27:33 2022

@author: setuhnjimaja
"""

import itertools

def is_lower(left, right):
    
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
                result = is_lower(l, [r])
                if result is not None: return result
            
            if type(l) == int and type(r) == list:
                result = is_lower([l], r)
                if result is not None: return result
            
            if type(l) == list and type(r) == list:
                result = is_lower(l, r)
                if result is not None: return result
                
    return None
            
# Function to find the partition position
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if is_lower(array[j], pivot):
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
            

with open('input_13') as data:
    list_packet = [eval(line.strip()) for line in data.readlines() if line.strip() != '' ]
    item_list = [ [[2]], [[6]] ]
    
    for item in item_list:
        list_packet.append(item)
    
quickSort(list_packet, 0, len(list_packet)-1)
indexes = [list_packet.index(item)+1 for item in item_list]

answer = 1

for idx in indexes:
    answer *= idx
    
print(answer)
