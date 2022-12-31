#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:31:03 2022

@author: setuhnjimaja
"""
from itertools import permutations

class City:
    def __init__(self, name):
        self.name = name
        self.connections = {}

cities = {}

with open('input_9') as data:
    for line in data.readlines():
        cities_couple, distance = line.split(' = ')
        
        city_1, city_2 = cities_couple.split(' to ')
        
        if city_1 not in cities.keys():
            cities[city_1] = City(city_1)
            
        if city_2 not in cities.keys():
            cities[city_2] = City(city_2)
        
        cities[city_1].connections[city_2] = int(distance)
        cities[city_2].connections[city_1] = int(distance)
        
distance_min = len(cities)*1000
itinary_min = []
distance_max = 0
itinary_max = []

for itinary in permutations(cities.keys(), len(cities)):
    distance_i = 0
    
    for idx in range(len(itinary)-1):
        distance_i += cities[itinary[idx]].connections[itinary[idx+1]]
        
    if distance_i < distance_min: 
        distance_min = distance_i
        itinary_min = itinary
    if distance_i > distance_max: 
        distance_max = distance_i
        itinary_max = itinary

print('Distance_min:', distance_min, itinary_min)
print('Distance_max:', distance_max, itinary_max)