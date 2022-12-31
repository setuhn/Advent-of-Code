# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 07:42:59 2022

@author: Setuhn
"""
from collections import deque

def execute_operation(operation, monkeys):
    x = monkeys[operation[0]]
    y = monkeys[operation[2]]
    if '+' in operation[1]:
        return  x + y
        
    elif '-' in operation[1]:
        return  x - y
        
    elif '*' in operation[1]:
        return  x * y
        
    elif '/' in operation[1]:
        return  x // y
        

monkeys_unknown = {}
monkeys_known = {}

todo = deque() # append(x), appendleft(x), pop(), popleft(), reverse(), rotate(n=1), remove(value)

with open('input_21') as data:
    for line in data.readlines():
        name, operation = line.split(': ')
        operation = operation.strip()
        
        if not any(x in ['+', '-', '*', '/'] for x in operation):
    
            number = int(operation)
            monkeys_known[name] = number
        
        else:
            monkeys_unknown[name] = operation.split(' ')
        
todo.append('root')
next_monkeys = [monkeys_unknown['root'][0], monkeys_unknown['root'][2]]

# Follows the monkey's need from 'root'
while next_monkeys:
    todo.extendleft(next_monkeys)
    current_monkeys = next_monkeys.copy()
    
    for monkey in current_monkeys:
        next_monkeys.remove(monkey)
        
        for i in [0, 2]:
            m = monkeys_unknown[monkey][i]
            if m not in todo and m in monkeys_unknown.keys():
                next_monkeys.append(m)
                

for name in todo:
    operation = monkeys_unknown[name]
    number = execute_operation(operation, monkeys_known)
    
    monkeys_known[name] = number

print(monkeys_known['root'])