# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 23:37:32 2023

@author: Setuhn
"""
import re, string

def checksum_generator(room_name):
    letters_ordering = {}
    
    for letter in list(set(room_name)):
        letter_count = room_name.count(letter)
        
        if letter_count not in letters_ordering.keys():
            letters_ordering[letter_count] = []
            
        letters_ordering[letter_count].append(letter)
    
    checksum = []
    for idx in reversed(sorted(letters_ordering.keys())):
        
        checksum.extend(sorted(letters_ordering[idx]))
        
    return ''.join(checksum[:5])

def decrypt(room_name, shift):
    decrypted_name = []
    
    for letter in room_name:
        new_idx = string.ascii_lowercase.index(letter) + shift
        
        
        if new_idx > len(string.ascii_lowercase)-1: 
            new_idx -= len(string.ascii_lowercase)
            
        decrypted_name.append(string.ascii_lowercase[new_idx])
        
    return ''.join(decrypted_name)
            
        
answer = 0
with open('input_4') as data:
    
    for room in data.readlines():
        letters = re.findall(r'[a-z]+', room.strip())
        ID = int(re.findall(r'\d+', room.strip())[0])
        
        room_letters = ''.join(letters[:-1])
        checksum = letters[-1]
        
        if checksum_generator(room_letters) == checksum:
            answer += ID
            
            decrypted_room_name = decrypt(room_letters, ID%26)
            
            if 'northpole' in decrypted_room_name:
                
                print('Answer part 2:', ID)
            
        
print('Answer part 1:', answer)   
     