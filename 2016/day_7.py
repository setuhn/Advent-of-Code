# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 01:02:44 2023

@author: Setuhn
"""
import regex as re
#https://regexr.com/

counter_1 = 0
counter_2 = 0
IP_addresses = []

with open('input_7') as data:
    for line in data.readlines():
        line = line.strip()
        
        supernet = re.findall(r'(\w+(?![^\[]*\]))', line)
        hypernet = re.findall(r'\[([a-z]+)\]', line)
        IP_addresses.append([line, supernet, hypernet])
        
        #Part 1
        # test for all ABBA sequences # test for ABBA sequences in the brackets
        if re.findall(r'(\w)(?!\1)(\w)\2\1', line) and not re.findall(r'\[[^]]*?(\w)(?!\1)(\w)\2\1[^[]*?\]', line):
            counter_1 += 1
            
        #Part 2    
        ABA_list = []
        for sn in supernet:
            ABA_list.extend(re.findall(r'(\w)(?!\1)(\w)\1', sn, overlapped=True))
        
        found = False
        # print(ABA_list)
        
        if ABA_list:
        
            for hn in hypernet:
                
                for ABA_i in ABA_list:
                    BAB_i = ABA_i[1]+ABA_i[0]+ABA_i[1]
                    
                    if BAB_i in hn:
                        counter_2 += 1
                        found = True
                        break
                    
                if found:
                    break

print('Answer part 1:', counter_1) 
print('Answer part 2:', counter_2)