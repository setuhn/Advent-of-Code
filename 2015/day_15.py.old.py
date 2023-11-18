# sym = []

# TODO automatise the functon creation
# for name in ingredients:
#     ingredients[name] = ingredients[name] + tuple([sym.Symbol('x')])
    
# x = sym.Symbol('x', real=True)
# y = sym.Symbol('y', real=True)

# f_capacity = -x + 2 * y
# f_durability = -2 * x + 3 * y
# f_flavor = 6 * x + -2 * y
# f_texture = 3 * x -y

# f_score = f_capacity * f_durability * f_flavor * f_texture
# f_score_x = f_score.xreplace({y : 100-x})

# fp_score_x = sym.diff(f_score_x, x)

# scores = []

# for result in sym.solve(fp_score_x, x):
    
#     candidate = int(round(result.evalf()))
    
#     scores.append(f_score_x.subs(x, candidate))
    
# print(max(scores))

# Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
# PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
# Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
# Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 16:42:39 2022

@author: Setuhn
"""
import sympy as sym
from scipy.optimize import fmin, minimize
import numpy as np


def score_total(teaspoons: np.array, properties_values_np: np.array, ) -> int:
    return np.prod(np.matmul(teaspoons, properties_values_np))
    
    # for i in range(properties_n):
        
        
    
    # return np.prod(property_scores)

properties_values = []

with open('input_15_test.txt') as data:
    for line in data.readlines():
        name = line.strip().split(' ')[0]
        properties = [int(word.strip(',')) for idx, word in enumerate(line.strip().split(' ')) if idx in [2, 4, 6, 8, 10]]
        
        properties_values.append(properties[:-1])
        
properties_values_np = np.array(properties_values)

# boundary: tespoons between 0 and 100, sum of teaspoons must be 100    
teaspoons_total = 100
teaspoons = np.array((44, 56))#np.zeros((len(properties_values), ), dtype=int)

# a = score_total(properties_values_np, [44, 56] or teaspoons)

fmin(score_total, teaspoons, properties_values_np)

# A maximization is the minimization of the -1*function: scipy.optimize.minimize



