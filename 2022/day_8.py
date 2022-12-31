# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 08:36:51 2022

@author: Setuhn
"""
import numpy as np

def check_visibility(tree, tree_line):
    for t in tree_line:
        if tree <= t:
            return False

    return True

def is_visible(row, col, grid):
    tree = grid[row, col]
    
    # check top
    if check_visibility(tree, grid[:row, col]):
        return True

    # check bottom
    if check_visibility(tree, grid[row+1:, col]):
        return True
    
    # check left:
    if check_visibility(tree, grid[row, :col]):
        return True
        
    # check right:
    if check_visibility(tree, grid[row, col+1:]):
        return True
    
    return False

def line_tree_visible(tree, tree_line):
    number = 0
    
    for t in tree_line:
        
        if t >= tree:
            return number + 1
        else:
            number +=1

    return number

def number_visible_trees(row, col, grid):
    tree = grid[row, col]
    # check top
    n_top = line_tree_visible(tree, np.flip(grid[:row, col]))

    # check bottom
    n_bottom =  line_tree_visible(tree, grid[row+1:, col])
 
    # check left:
    n_left =  line_tree_visible(tree, np.flip(grid[row, :col]))
        
    # check right:
    n_right =  line_tree_visible(tree, grid[row, col+1:])
    
    return n_top*n_bottom*n_left*n_right

with open("input_8", 'r') as data:
    
    grid = np.array([[int(tree) for tree in line if tree.isdigit()] for line in data.readlines() ]) 
    
    # # PART 1
    # visible = 0
    # #  Count the edges
    # visible = 2*(grid.shape[0]+grid.shape[1]-2)
    
    # # Count the interior
    # for row in range(1, grid.shape[0]-1):
    #     for col in range(1, grid.shape[1]-1):
            
    #         if is_visible(row, col, grid):
    #             visible += 1
            
    # print(visible)
    
    # PART 2
    view_tree = 0
    for row in range(1, grid.shape[0]-1):
        for col in range(1, grid.shape[1]-1):
            new_view_tree = number_visible_trees(row, col, grid)
            if new_view_tree > view_tree:
                view_tree = new_view_tree 
    print(view_tree)