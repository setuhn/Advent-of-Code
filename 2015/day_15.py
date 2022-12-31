# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 16:42:39 2022

@author: Setuhn
"""
import sympy as sym

ingredients = {}

with open('input_15_test.txt') as data:
    for line in data.readlines():
        name, capacity, durability, flavor, texture, calories = [int(word.strip(',')) if word.strip(',-').isdigit() else word.strip(':') for idx, word in enumerate(line.strip().split(' ')) if idx in [0, 2, 4, 6, 8, 10]]
        
        ingredients[name] = (capacity, durability, flavor, texture, calories)
        
teaspoons = 100
# sym = []

# TODO automatise the functon creation
# for name in ingredients:
#     ingredients[name] = ingredients[name] + tuple([sym.Symbol('x')])
    
x = sym.Symbol('x', real=True)
y = sym.Symbol('y', real=True)

f_capacity = -x + 2 * y
f_durability = -2 * x + 3 * y
f_flavor = 6 * x + -2 * y
f_texture = 3 * x -y

f_score = f_capacity * f_durability * f_flavor * f_texture
f_score_x = f_score.xreplace({y : 100-x})

fp_score_x = sym.diff(f_score_x, x)

scores = []

for result in sym.solve(fp_score_x, x):
    
    candidate = int(round(result.evalf()))
    
    scores.append(f_score_x.subs(x, candidate))
    
print(max(scores))
    
