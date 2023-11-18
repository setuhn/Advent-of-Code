# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:46:34 2023

@author: Setuhn
"""

bots = {}
output_bin = {}

class Bot:
    def __init__(self, bot_ID:int,  lower:list, upper:list) -> None:
        self.ID = bot_ID
        self._chips = []
        self.lower_output = lower
        self.upper_output = upper
        
    def add_chip(self, chip_ID:int) -> None:
        
        if len(self._chips) >= 2:
            print('ERROR chips number')
            
        else:
            self._chips.append(chip_ID)
            
            if len(self._chips) == 2:
                
                # Part 1
                if sorted(self._chips) == [17, 61]:
                    print('Answer part 1 :', self.ID)
                
                lower_chip_ID, upper_chip_ID = sorted(self._chips)
                    
                if self.lower_output[0] == 'b':
                    bots[self.lower_output[1]].add_chip(lower_chip_ID)
                    
                else:
                    
                    if self.lower_output[1] not in output_bin.keys():
                        output_bin[self.lower_output[1]] = []
                        
                    output_bin[self.lower_output[1]].append(lower_chip_ID)
                    
                if self.upper_output[0] == 'b':
                    bots[self.upper_output[1]].add_chip(upper_chip_ID)
                    
                else:
                    
                    if self.upper_output[1] not in output_bin.keys():
                        output_bin[self.upper_output[1]] = []
                        
                    output_bin[self.upper_output[1]].append(upper_chip_ID)
                
                self._chips = []
                
initiation = []

with open('input_10') as data:
    for line in data.readlines():
        if 'value' in line:
            chip_value, bot_ID = int(line.strip().split()[1]), int(line.strip().split()[-1])
            initiation.append((bot_ID, chip_value))
            
        else:
            bot_ID, lower_ID, upper_ID = int(line.strip().split()[1]), ['b' if line.strip().split()[5] == 'bot' else 'o', int(line.strip().split()[6])] , ['b' if line.strip().split()[-2] == 'bot' else 'o', int(line.strip().split()[-1])]
            
            bots[bot_ID] = Bot(bot_ID, lower_ID, upper_ID)
            

for bot_ID, chip_ID in initiation:
    bots[bot_ID].add_chip(chip_ID)
    
print('Answer part 2 :', output_bin[0][0] * output_bin[1][0] * output_bin[2][0])