"""
Created on Fri Dec 30 16:42:39 2022

@author: Setuhn
"""

import numpy as np
import heapq

teaspoons_total = 100


def score_total(teaspoons: np.array, properties_values_np: np.array, ) -> int:

    return np.prod(np.matmul(teaspoons, properties_values_np).clip(0))

def get_next_tespoons_distrib(teaspoons):
    teaspoons_distrib = []
    
    for idx in range(len(teaspoons)):
        
        teaspoons_distrib += [[t+1 if i == idx else t for i, t in enumerate(teaspoons)]]
        
    return teaspoons_distrib
        


properties_values = []

with open('input_15') as data:
    for line in data.readlines():
        name = line.strip().split(' ')[0]
        properties = [int(word.strip(',')) for idx, word in enumerate(line.strip().split(' ')) if idx in [2, 4, 6, 8, 10]]
        
        properties_values.append(properties[:-1])

# Value for each property of each ingredient        
properties_values_np = np.array(properties_values)

# Quue for the A* algo
path_q = []
heapq.heappush(path_q, (0, [0]*properties_values_np.shape[0]))

# Answer to part 1
score_final = 0
teaspoons_final = []

visited = []

while path_q:
    _, teaspoons_current = heapq.heappop(path_q)
    
    score_current = score_total(teaspoons_current, properties_values_np)

    
    if score_final < score_current and sum(teaspoons_current) == teaspoons_total:
        score_final = score_current
        teaspoons_final = teaspoons_current
        continue
        

    teaspoons_next = get_next_tespoons_distrib(teaspoons_current)
    
    for teaspoons in teaspoons_next:
        if sum(teaspoons) > teaspoons_total:
            continue
        
        elif teaspoons not in visited:
            
            heapq.heappush(path_q, (-score_current, teaspoons))
            visited += [teaspoons]
        
        
print(score_final, teaspoons_final)    
    
        
    




