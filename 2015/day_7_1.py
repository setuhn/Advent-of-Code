#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 16:01:25 2022

@author: setuhnjimaja
"""
# use DFS to get all the wires value


# return a tuple of the variables and the operation name
def deconstruct_instruction(instruction):
    out = None
    
    if 'AND' in instruction:
        out = (instruction.strip().split(' AND '), 'AND')
        
    elif 'OR' in inst[0]:
        out = (instruction.strip().split(' OR '), 'OR')
        
    elif 'LSHIFT' in inst[0]:
        out = (instruction.strip().split(' LSHIFT '), 'LSHIFT')
        
    elif 'RSHIFT' in inst[0]:
        out = (instruction.strip().split(' RSHIFT '), 'RSHIFT')
        
    elif 'NOT' in inst[0]:
        out = ([instruction.strip().strip('NOT ')], 'NOT')
        
    else:
        out = ([instruction.strip()], None)
        
    return out

def calculate_instruction(variables, operation):
    out = None
    left = int(variables[0]) if variables[0].isdigit() else wires_known[variables[0]]
    
    if len(variables) > 1:
        right = int(variables[1]) if variables[1].isdigit() else wires_known[variables[1]]
    
        if operation == 'AND': 
            out = left & right
            
        elif operation == 'OR':
            out = left | right
            
        elif operation == 'LSHIFT':
            out = left << right
            
        elif operation == 'RSHIFT':
            out = left >>  right
            
        else:
            print('ERROR operation 1: ', operation)
    
    else:
        
        if operation == 'NOT':
            out = 65535 - left
            
        elif operation == None:
            out = left
            
        else:
            print('ERROR operation 1: ', operation)
            
    return out
   
wires_known = {}
wires_unknown = {}

with open('input_7') as data:
    booklet = data.readlines()

for instruction in booklet:
    
    inst = instruction.split('->')
    wire_label = inst[1].strip()
    
    if inst[0].strip().isdigit():
        wires_known[wire_label] = int(inst[0])
        
    else:
        wires_unknown[wire_label] = deconstruct_instruction(inst[0])

start_wire = 'a'
wire_q = [start_wire]

while wire_q:
    current_wire = wire_q[-1]
    
    variables, operation = wires_unknown[current_wire]
    variables_known = True
    
    for v in [var for var in variables if not var.isdigit()]:

        if v not in wires_known.keys():
            variables_known = False
            
            if v not in wire_q:
                wire_q.append(v)
                
            else:
                wire_q.insert(wire_q.index(v), wire_q.pop())
                
    if variables_known:
        wires_known[current_wire] = calculate_instruction(variables, operation)
        wire_q.pop()
        
print(wires_known[start_wire])