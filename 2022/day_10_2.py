# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 09:26:32 2022

@author: Setuhn
"""
import numpy as np


def draw_pixel(sprite_position, crt):

    if len(crt) in sprite:
        return ['#']
    else:
        return [' ']

def tick(crt, sprite, crt_np, line):
    crt += draw_pixel(sprite, crt)
    if len(crt) == crt_np.shape[1]:
        crt_np[line, :], crt, line = crt, [], line+1

    return crt, sprite, crt_np, line

with open("input_10", 'r') as data:
    crt = []
    sprite = [0, 1, 2]
    crt_np = np.full((6, 40), '')
    line = 0

    for instruction in data.readlines():
        crt, sprite, crt_np, line = tick(crt, sprite, crt_np, line)

        if 'addx' in instruction:
            crt, sprite, crt_np, line = tick(crt, sprite, crt_np, line)
            # Increment the sprite value
            sprite = [x+int(instruction.split()[1]) for x in sprite]
           

# Display answer
for i in crt_np:
    for n in i:
        print(n, sep='', end='')
    print('')
