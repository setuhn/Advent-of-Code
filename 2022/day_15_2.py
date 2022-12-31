# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 08:03:06 2022

@author: Setuhn
"""
import re
from shapely.geometry import Polygon, Point

def calc_dist(signal, beacon):
    return abs(signal[0]-beacon[0])+abs(signal[1]-beacon[1])


bound_cond = 4000000

area_interest_polygon = Polygon([
    (0, 0), 
    (0, bound_cond), 
    (bound_cond,bound_cond), 
    (bound_cond, 0), 
    (0, 0)
    ])

with open("input_15", 'r') as data:
    for idx, line in enumerate(data.readlines()):
        signal_x, beacon_x = re.findall(r'(?<=x=)-?\d+', line)
        signal_y, beacon_y = re.findall(r'(?<=y=)-?\d+', line)
        signal_x, beacon_x, signal_y, beacon_y = int(signal_x), int(beacon_x), int(signal_y), int(beacon_y)
        
        distance = abs(signal_x-beacon_x) + abs(signal_y-beacon_y)
        
        signal_v = [
            (signal_x-distance, signal_y), 
            (signal_x, signal_y-distance), 
            (signal_x+distance, signal_y), 
            (signal_x, signal_y+distance),
            (signal_x-distance, signal_y)
                    ]
        
        signal_polygon = Polygon(signal_v)
        
        area_interest_polygon = area_interest_polygon.difference(signal_polygon)

area = area_interest_polygon
# bounds -> minx, miny, maxx, maxy
minx, miny, maxx, maxy = area.bounds
minx, miny, maxx, maxy = int(minx), int(miny), int(maxx), int(maxy)

for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        if area.contains(Point(x, y)):
            beacon = (x, y)
            print(beacon)
           
          
print(beacon[0]*4000000+beacon[1])            
        
    
