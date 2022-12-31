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
        
def reverse_operation(operation, name, number, monkeys_known, monkeys_unknown):
    name_1 = operation[0]
    name_2 = operation[2]
    
    z = number
    i, name_y = [(idx, n) for idx, n in enumerate([name_1, name_2]) if n not in monkeys_unknown and n != 'humn'][0]
    
    y = monkeys_known[name_y]
    
    if '+' in operation[1]:
            return  z - y
        
    elif '-' in operation[1]:
        if i == 1:
            return  z + y
        else:
            return y - z
        
    elif '*' in operation[1]:
            return  z // y
        
    elif '/' in operation[1]:
        if i == 1:
            return  z * y
        else:
            return y // z
    
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
        

next_monkeys = [monkeys_unknown['root'][0], monkeys_unknown['root'][2]]
operation_list = []

# Follows the monkey's need from 'root'
while next_monkeys:
    todo.extendleft(next_monkeys)
    current_monkeys = next_monkeys.copy()
    
    for monkey in current_monkeys:
        if 'humn' in monkeys_unknown[monkey]:
            operation_list.insert(0, monkey)
        
        next_monkeys.remove(monkey)
        
        for i in [0, 2]:
            m = monkeys_unknown[monkey][i]
            if m not in todo and m in monkeys_unknown.keys():
                next_monkeys.append(m)
                
for name in todo:
    operation = monkeys_unknown[name]
    number = execute_operation(operation, monkeys_known)
    monkeys_known[name] = number
    
    if any(n in operation_list for n in operation):
        operation_list.insert(0, name)

good_branch = [monkey for monkey in [monkeys_unknown['root'][0],  monkeys_unknown['root'][2]] if monkey not in operation_list][0]

n = monkeys_known[good_branch]

for name in operation_list:
    n = reverse_operation(monkeys_unknown[name], name, n, monkeys_known, operation_list)

monkeys_known['humn'] = n

for name in todo:
    operation = monkeys_unknown[name]
    number = execute_operation(operation, monkeys_known)
    monkeys_known[name] = number

if monkeys_known[good_branch]:
    n_1 = monkeys_known[monkeys_unknown['root'][0]]
    n_2 = monkeys_known[monkeys_unknown['root'][2]]
    print(n_1, n_2, n_1==n_2)
    
print('Answer: ', n)