# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 00:13:45 2023

@author: Setuhn
"""
import hashlib

ID = 'reyedfim'
num = 0

# # Part 1
# password = []
# print('.'*8, end='', sep='')

# while len(password) < 8:
    
#     digest = list(hashlib.md5((ID+str(num)).encode()).hexdigest())
    
#     if sum([int(i,base = 16) for i in digest[:5]]) == 0:
#         password.append(digest[5])
#         print('\b'*8, ''.join(password), '.'*(8-len(password)), end='', sep='')
        
#     num += 1

# Part 2s
password = [None] * 8
print('\b'*8, ''.join([(digit if (digit != None) else '.') for digit in password]), end='', sep='')

while None in password:
    
    digest = list(hashlib.md5((ID+str(num)).encode()).hexdigest())
    
    if sum([int(i,base = 16) for i in digest[:5]]) == 0:
        idx = int(digest[5],base = 16)
        
        if idx < len(password):
            if password[idx] == None:
            
                password[idx] = digest[6]
                
                print('\b'*8, ''.join([(digit if (digit != None) else '.') for digit in password]), end='', sep='')
        
    num += 1