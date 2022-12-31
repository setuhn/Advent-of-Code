#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 09:23:44 2022

@author: setuhnjimaja
"""

def distance_reindeer(reindeer_info, time):
    speed, time_speed, time_rest  = reindeer_info
    
    main_distance = time//(time_speed + time_rest) * speed * time_speed
    
    remain_time = time% (time_speed + time_rest)
    remain_distance = (time_speed * speed) if remain_time > time_speed else remain_time*speed
    
    return main_distance + remain_distance
    
reindeers = {}

with open('input_14') as data:
    for line in data.readlines():
        name, speed, time_speed, time_rest = [info for idx, info in enumerate(line.strip().split(' ')) if idx in [0, 3, 6, 13]]
        reindeers[name] = (int(speed), int(time_speed), int(time_rest))

# Part 1        
distances = []
time = 2503

for reindeer_info in reindeers.values():
    distances.append(distance_reindeer(reindeer_info, time))
    
print('Answer part 1:', max(distances))

# Part 2
distances = dict.fromkeys(reindeers.keys(), 0)
points = dict.fromkeys(reindeers.keys(), 0)

for tick in range(1, time+1):
    distance_max = 0
    
    for reindeer_name, reindeer_info in reindeers.items():
        
        distance =  distance_reindeer(reindeer_info, tick)
        
        if distance > distance_max: 
            distance_max = distance
        
        distances[reindeer_name] = distance
        
    for reindeer in reindeers.keys():
        
        if distances[reindeer] == distance_max:
            points[reindeer] +=1
        
print('Answer part 2:', max(points.values()))    