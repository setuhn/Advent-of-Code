# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 15:43:08 2023

@author: Setuhn
"""

instructions = []
finished = False
instr_idx = 0

register = {
    'a' : 0,
    'b' : 0, 
    'c' : 1,
    'd' : 0
    }

# cpy x y - copies x (either an integer or the value of a register) into register y.
# inc x - increases the value of register x by one.
# dec x - decreases the value of register x by one.
# jnz x y - jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.

def execute_instruction(instr_idx:int, instructions:list):
    instruction = instructions[instr_idx]
    instr_idx += 1
    
    if 'cpy' in instruction:
        x, y = instruction.split()[1:]
        register[y] = register[x] if x in register.keys() else int(x) 
        
    elif 'inc' in instruction:
        x = instruction.split()[1]
        register[x] += 1
        
    elif 'dec' in instruction:
        x = instruction.split()[1]
        register[x] -= 1
        
    elif 'jnz' in instruction:
        x, y = instruction.split()[1:]
        if register[x] if x in register.keys() else int(x) != 0:
            instr_idx = (instr_idx-1) + int(y)
            
    return instr_idx
        
with open('input_12') as data:
    for line in data.readlines():
        instructions.append(line.strip())
        


while instr_idx < len(instructions):
    
    instr_idx = execute_instruction(instr_idx, instructions)

print(register['a'])