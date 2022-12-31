# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 18:26:12 2022

@author: Setuhn
"""
import hashlib

key = 'iwrupvqb'
salt = 0
found = False
n = 6


while(not found):
    md5 = hashlib.md5(f'{key}{salt}'.encode()).hexdigest()
    
    if md5[:n] == '0'*n:
        found = True
    else:
        salt += 1

print(md5, salt)
