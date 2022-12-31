# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 09:59:28 2022

@author: Setuhn
"""
from itertools import cycle
import numpy as np

# Classes
class FallingRock:
    
    def __init__(self, rock_pattern, screen_size):
        self.pattern = np.array(rock_pattern)
        
        self.height, self.width = self.pattern.shape

        # add the 2 spaces from the left wall
        self.pattern = np.hstack((np.zeros((self.height, 2)), self.pattern))
        
        # pad to the right wall
        self.pattern = np.hstack((self.pattern, np.zeros((self.height, (screen_size-2)-self.width))))
        
    def move_left(self):
        # check if left column is empty
        if np.sum(self.pattern[:, 0]) == 0:
            # remove one empty stack on the left
            self.pattern = np.delete(self.pattern, 0, axis=1)
            
            # add one empty stack to the right
            self.pattern = np.hstack((self.pattern, np.zeros((self.height, 1))))
            
    def move_right(self):
        # check if right column is empty
        if np.sum(self.pattern[:, -1]) == 0:
            # remove one empty stack on the left
            self.pattern = np.delete(self.pattern, -1, axis=1)
            
            # add one empty stack to the right
            self.pattern = np.hstack((np.zeros((self.height, 1)), self.pattern, ))


# Functions
def gen_jet_cycle(jet_pattern):
    for idx, jet in cycle(zip(range(len(jet_pattern)), jet_pattern)):
        yield idx, jet
        
def gen_rock_cycle(rock_pattern):
    for idx, rock in cycle(zip(range(len(rock_pattern)), rock_pattern)):
        yield idx, rock

# take the part of the screen that overlaps with the falling rock, sum them and 
# check that there are no cell with a number > 1
def has_rock_landed(falling_rock, row, screen):
    
    overlap_size = row-falling_rock.height
    
    if  overlap_size < 0:
        stack_overlap = screen[:row, :] + falling_rock.pattern[-(row):, :]
        
    else:
        stack_overlap = screen[row-falling_rock.height:row, :] + falling_rock.pattern

    if np.count_nonzero(stack_overlap > 1):
        return True
        
    return False
    

# add the landed rock to the screen by adding its pattern to the overlaping screen part
def add_landed_rock_screen(falling_rock, screen, row, screen_size):

    screen[row-falling_rock.height:row, :] = screen[row-falling_rock.height:row, :] + falling_rock.pattern
    
# Check if the rock can move right by changing its pattern and adding it to the part of the screen that overlaps with the pattern
def move_if_rock_free_right(falling_rock, screen, row):
    falling_rock.move_right()
    overlap_size = row-falling_rock.height
    
    if  overlap_size < 0:
        stack_overlap = screen[:row, :] + falling_rock.pattern[-(row):, :]
        
    else:
        stack_overlap = screen[row-falling_rock.height:row, :] + falling_rock.pattern

    if np.count_nonzero(stack_overlap > 1):
        falling_rock.move_left()
        
# Check if the rock can move left by changing its pattern and adding it to the part of the screen that overlaps with the pattern
def move_if_rock_free_left(falling_rock, screen, row):
    falling_rock.move_left()
    overlap_size = row-falling_rock.height
    
    if  overlap_size < 0:
        stack_overlap = screen[:row, :] + falling_rock.pattern[-(row):, :]
        
    else:
        stack_overlap = screen[row-falling_rock.height:row, :] + falling_rock.pattern

    if np.count_nonzero(stack_overlap > 1):
        falling_rock.move_right()
        
# Read input    
with open('input_17') as data:
    jet_pattern =  data.read().strip()

   
screen_size = 7 # The tall, vertical chamber is exactly seven units wide
# Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one)
screen = np.zeros((1, screen_size))

rock_pattern = [
    [[1]*4], 
    [[0, 1, 0], [1, 1, 1], [0, 1, 0]], 
    [[0, 0, 1], [0, 0, 1], [1, 1, 1]], 
    [[1], [1], [1], [1]],
    [[1, 1], [1, 1]]
    ]

jet_cycle = gen_jet_cycle(jet_pattern)
rock_cycle = gen_rock_cycle(rock_pattern)
rocks_fallen = 0
# keep the idx_rock_cycle, idx_jet_cycle and screen last 4 height to compare if it comes back
track_cycles = []
track_pattern = []
pattern_found = False
size_check_pattern = 1000
indicator = None

# Main loop
# stop after n rocks have stopped (but before the n+1 rock begins falling)
while(rocks_fallen < 10000 and not pattern_found):
    # cycle through the diferent rock shapes
    for idx_rock_cycle, rock in rock_cycle:
        
        # initiate falling rock
        falling_rock = FallingRock(rock, screen_size)
        
        # pad with 3 empty lines
        screen = np.vstack((np.zeros((3, screen_size)), screen))
        
        # pad with height of rock empty lines
        screen = np.vstack((np.zeros((falling_rock.height, screen_size)), screen))
        
        rock_landed = False
        
        # cycle through the screen rows, starts the row below the rock, until it either landed or reached the bottom
        for row in range(falling_rock.height, screen.shape[0]):
            
            #check if the row is empty if yes, move freely
            if np.count_nonzero(screen[row, :] > 0) == 0:
            
                # move the rock left or right
                for idx_jet_cycle, jet in jet_cycle:
                    if jet == '>': falling_rock.move_right()
                    elif jet == '<': falling_rock.move_left()
                    break
            
            # else, check if move possible
            else:
                
                # move the rock left or right while checking if possible on current_row
                for idx_jet_cycle, jet in jet_cycle:
                    if jet == '>': 
                        move_if_rock_free_right(falling_rock, screen, row)
                    elif jet == '<': 
                        move_if_rock_free_left(falling_rock, screen, row)
                    break
            
                #check if the rock can fall to the next_row
                if has_rock_landed(falling_rock, row+1, screen):
                    rock_landed = True
                    add_landed_rock_screen(falling_rock, screen,row, screen_size)
                    
                    break
        
        # if rock not landed, draw at the bottom of the screen
        if not rock_landed:
            add_landed_rock_screen(falling_rock, screen, screen.shape[0],screen_size)
        
        # remove all empty row at the top
        for row in screen:
            if np.count_nonzero(row > 0):
                break
            screen = np.delete(screen, 0, axis=0)
            
        
        
        
        # if rocks_fallen >= size_check_pattern:
        current_cycle = (idx_rock_cycle, idx_jet_cycle)
        current_screen_pattern = np.copy(screen[0:size_check_pattern, :])
        
    
        if current_cycle in track_cycles:
            for i, c in [(idx, c) for idx, c in enumerate(track_cycles) if c == current_cycle]:
                if np.array_equal(track_pattern[i][0], current_screen_pattern):
                    pattern_found = True
                    indicator = i
                    break
            
        track_cycles.append((idx_rock_cycle, idx_jet_cycle, ))
        track_pattern.append([current_screen_pattern, screen.shape[0]])
        
        rocks_fallen += 1
        
        break

        
# remove all empty row at the top
for row in screen:
    if np.count_nonzero(row > 0):
        break
    screen = np.delete(screen, 0, axis=0)

aimed_rocks = 1000000000000

n_rocks_repeat = rocks_fallen-1-indicator
base_lines = track_pattern[indicator][1]
n_lines_repeat = track_pattern[rocks_fallen-1][1] - base_lines

n = (aimed_rocks - indicator)//n_rocks_repeat

remain_rocks = (aimed_rocks - indicator)%n_rocks_repeat
remain_lines = track_pattern[indicator+remain_rocks-1][1] - base_lines

height = base_lines + n*n_lines_repeat + remain_lines

print(height)
        
    
    