import numpy as np
from collections import deque

def next_beams(beam, layout):
    new_position = beam[0] + beam[1]

    if new_position not in layout.keys():
        return None
    
    char = layout[new_position]
    new_directions = [beam[1]]

    # Logic for rotating the beam depending on the real/img and char
    if char == '\\':
        if new_directions[0].real == 0:
            new_directions[0] *= -1j
        else:
            new_directions[0] *= 1j

    if char == '/':
        if new_directions[0].img == 0:
            new_directions[0] *= 1j
        else:
            new_directions[0] *= -1j

    if char == '|':
        if new_directions[0].real == 0:
            new_directions = [new_directions[0] * modif for modif in [1j, -1j]]

    if char == '-':
        if new_directions[0].img == 0:
            new_directions = [new_directions[0] * modif for modif in [1j, -1j]]

    return [[new_position, direction] for direction in new_directions]



    

# Part 1 could be done by coding the trajectory (coordinates and direction) of the beam(s) with complex numbers (x = real, y = img; *j = -90° *-j = 90°, *-1 = +180°)
if __name__ == '__main__':

    layout = {}

    with open(f'day_16.1-test.txt') as data:
        
        for idx_line, line in enumerate(data.readlines()):
            for idx_col, char in enumerate(list(line.strip())):
                layout[idx_line+idx_col*1j] = char

    energised_tiles = set()
    beams_list = deque()
    beam = [0-1j, 0+1j]
    beams_list.append(beam)
    history = []

    

    while beams_list:
        beam = beams_list.popleft()

        for next_beam in next_beams(beam, layout):

            if next_beam[0] not in layout.keys():
                break

            elif next_beam in history:
                break

            else;
                

