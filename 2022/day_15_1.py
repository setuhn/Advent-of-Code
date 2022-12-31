# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 08:03:06 2022

@author: Setuhn
"""
import re

def calc_dist(signal, beacon):
    return abs(signal[0]-beacon[0])+abs(signal[1]-beacon[1])



y = 2000000
cover = set()
beacon_at_y = set()

with open("input_15", 'r') as data:
    for line in data.readlines():
        signal_x, beacon_x = re.findall(r'(?<=x=)-?\d+', line)
        signal_y, beacon_y = re.findall(r'(?<=y=)-?\d+', line)
        signal_x, beacon_x, signal_y, beacon_y = int(signal_x), int(beacon_x), int(signal_y), int(beacon_y)
        
        distance = abs(signal_x-beacon_x)+abs(signal_y-beacon_y)

        # calculate cover only if the y-line of interest is in its signal range
        if signal_y - distance <= y <= signal_y + distance: 
            # the signal cover is proportional to the distance between the siang and the line of interest
            cover.add(signal_x)
            for i in range(1, distance - abs(signal_y - y)+1) :
                cover.add(signal_x+i)
                cover.add(signal_x-i)
            
        # remove one cover unit of beacon in on the line of interest
        if beacon_y == y:
            beacon_at_y.add(beacon_x)

print(len(cover-beacon_at_y))            
            
        
    
