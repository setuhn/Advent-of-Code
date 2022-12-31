# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:54:07 2022

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
    for jet in cycle(jet_pattern):
        yield jet
        
def gen_rock_cycle(rock_pattern):
    for rock in cycle(rock_pattern):
        yield rock

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
with open('input_17_test.txt') as data:
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

# Main loop
# stop after n rocks have stopped (but before the n+1 rock begins falling)
while(rocks_fallen < 2022):
    # cycle through the diferent rock shapes
    for rock in rock_cycle:
        
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
                for jet in jet_cycle:
                    if jet == '>': falling_rock.move_right()
                    elif jet == '<': falling_rock.move_left()
                    break
            
            # else, check if move possible
            else:
                
                # move the rock left or right while checking if possible on current_row
                for jet in jet_cycle:
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
            
        rocks_fallen += 1
        
        break

        
# remove all empty row at the top
for row in screen:
    if np.count_nonzero(row > 0):
        break
    screen = np.delete(screen, 0, axis=0)

print(screen.shape[0])