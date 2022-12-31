#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 23:45:14 2022

@author: setuhnjimaja
"""
import string
import re

def increment_password(password):
    password = list(password)
    
    for idx, letter in reversed(list(enumerate(password))):
        
        if string.ascii_lowercase.index(letter) + 1 < len(string.ascii_lowercase):
            password[idx] = string.ascii_lowercase[string.ascii_lowercase.index(letter) + 1]
            break
        
        else:
            password[idx] = string.ascii_lowercase[0]
            
    return ''.join(password)

def verify_password(password):
    
    # Passwords may not contain the letters i, o, or l
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    
    # Passwords must contain at least two different, non-overlapping pairs of letters
    repeated_letters = re.findall(r'(.)\1{1,}', password)
    
    if len(repeated_letters) <= 1:
        return False
    
    # Passwords must include one increasing straight of at least three letters
    for i in range(len(password)-3):
        idx = string.ascii_lowercase.index(password[i])
        if idx > 23:
            continue
        
        if password[i+1] == string.ascii_lowercase[idx+1] and password[i+2] == string.ascii_lowercase[idx+2]:
            return True
    
    
    return False
# Part 1
# password = 'hepxcrrq'

# Part 2
password = 'hepxxyzz'
pass_verified = False

while not pass_verified:
    
    password = increment_password(password)
    pass_verified = verify_password(password)
    
print(password)