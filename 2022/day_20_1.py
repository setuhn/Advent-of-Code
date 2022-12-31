# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:31:46 2022

@author: Setuhn
"""
from collections import deque


# use data class to keep track of the values if there are repeating values one can't just use list.index()
class Data:
    def __init__(self, value):
        self.value = value
        self.moved = False

encrypted_file = []
with open('input_20')as data:
    for n in data.readlines():
        number = int(n.strip())
        encrypted_file.append(Data(number))
        
        if number == 0:
            data_zero = encrypted_file[-1]

     
decrypted_file = encrypted_file.copy()

for data in encrypted_file:
    n = data.value
    
    idx = decrypted_file.index(data)
    

    new_idx = idx + n
    
    new_idx = new_idx % (len(decrypted_file)-1)
    
    if n < 0 and new_idx == 0:
        new_idx = len(decrypted_file)-1
    
    elif n > 0 and new_idx == len(decrypted_file)-1:
        new_idx = 0
    
    decrypted_file.insert(new_idx, decrypted_file.pop(idx))
       
idx_zero = decrypted_file.index(data_zero)

# create a double-ended queue from the decrpted file
decrypted_file_band = deque(decrypted_file)
# rotate the values until 0 is at index 0
decrypted_file_band.rotate(-idx_zero)

coordinate = [1000, 2000, 3000]
answer = []

for c in coordinate:
    
    answer.append(decrypted_file_band[c-(c//len(decrypted_file_band))*len(decrypted_file_band)].value)

print(sum(answer))
    