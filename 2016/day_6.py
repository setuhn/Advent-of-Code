# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 00:48:06 2023

@author: Setuhn
"""

def most_frequent_letter(word):
    highest = ('', 0)
    
    for letter in word:
        count = word.count(letter)
        
        if count > highest[1]:
            highest = (letter, count)
            
    return highest[0]

def least_frequent_letter(word):
    lowest = ('', len(word))
    
    for letter in word:
        count = word.count(letter)
        
        if count < lowest[1]:
            lowest = (letter, count)
            
    return lowest[0]


answer_1 = []
answer_2 = []
signal = []

with open('input_6') as data:
    for line in data.readlines():
        signal.append([char for char in line.strip()])
        
for row_idx in range(len(signal[0])):
    answer_1.append(most_frequent_letter([row[row_idx] for row in signal]))
    answer_2.append(least_frequent_letter([row[row_idx] for row in signal]))

print('Answer part 1:', ''.join(answer_1))   
print('Answer part 2:', ''.join(answer_2))  