# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 21:03:58 2022

@author: Setuhn
"""


try:
    with open("input_5", 'r') as data:
        
        stacks = {}
        
        for line in data:
            
            line = line.strip('\n')
            n = 4
            
            if 'move' not in line and '[' in line:
                crates = [line[i:i+n].rstrip() for i in range(0, len(line), n)]
                
                for i,c in enumerate(crates):
                    
                    if c != '':
                    
                        if i+1 in stacks.keys():
                            stacks[i+1].insert(0, c)
                        else:
                            stacks[i+1] = [c]

            elif 'move' in line:
                move = [int(n) for n in line.split() if n.isdigit()]
                
                for _ in range(move[0]):
                    stacks[move[2]].append(stacks[move[1]].pop())
                    

        print(''.join([pile[-1].strip('[]') for pile in dict(sorted(stacks.items())).values()]))

        
except Exception as e:
    print(e)