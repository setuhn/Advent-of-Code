# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 06:50:38 2022

@author: Setuhn
"""



try:
    with open("input_6", 'r') as data:
        
        characters = data.read()
        
        # input the number of consecutive characters that needs to be different
        n = 14 #  part 1: n = 4

        
        for i in range(len(characters)):
            
            if len([c for c in characters[i:i+n] if characters[i:i+n].count(c) > 1]) == 0:
        
                print(i+n) 
                
                break

except Exception as e:
    print(e)