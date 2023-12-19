import numpy as np
from collections import deque

# take all the non '.' characters and connect them with doubly linked list -> Node
class Node:
    def __init__(self, char, coordinates):
        self.char = char
        self.coordinates = coordinates
        # reference to next nodes as key = direction_entry, value = (node_next, [linking cells])
        self.next_node_coor_from = {}

# return the next dict for the given node as 
def get_next_nodes(node, layout_array):
    next_nodes_coor = {}
    next_nodes_coor_list = {}
    idx_line, idx_col = node.coordinates
    boundary_line, boundary_col = layout_array.shape

    next_nodes_coor_list['down'] = layout_array[idx_line+1:, idx_col][(layout_array[idx_line+1:, idx_col] != None)] #-> [0]
    next_nodes_coor_list['up'] = layout_array[:idx_line, idx_col][(layout_array[:idx_line, idx_col] != None)] #-> [-1]
    next_nodes_coor_list['right'] = layout_array[idx_line, idx_col+1:][(layout_array[idx_line, idx_col+1:] != None)] # -> [0]
    next_nodes_coor_list['left'] = layout_array[idx_line, :idx_col][(layout_array[idx_line, :idx_col] != None)] # -> [-1]
    
    next_down = (next_nodes_coor_list['down'][0].coordinates if any(next_nodes_coor_list['down']) else (boundary_line-1, idx_col), 1+0j)
    next_up = (next_nodes_coor_list['up'][-1].coordinates if any(next_nodes_coor_list['up']) else (0, idx_col), -1+0j)
    next_right = (next_nodes_coor_list['right'][0].coordinates if any(next_nodes_coor_list['right']) else (idx_line, boundary_col-1), 0+1j)
    next_left = (next_nodes_coor_list['left'][-1].coordinates if any(next_nodes_coor_list['left']) else (idx_line, 0), 0-1j)

    if node.char == '|':
        
        next_nodes_coor[-1+0j] = [next_up]
        next_nodes_coor[1+0j] = [next_down]
        next_nodes_coor[0-1j] = [next_up, next_down]
        next_nodes_coor[0+1j] = [next_up, next_down]

    elif node.char == '-':

        next_nodes_coor[-1+0j] = [next_left, next_right]
        next_nodes_coor[1+0j] = [next_left, next_right]
        next_nodes_coor[0-1j] = [next_left]
        next_nodes_coor[0+1j] = [next_right]

    elif node.char == '\\':
            
        next_nodes_coor[-1+0j] = [next_left]
        next_nodes_coor[1+0j] = [next_right]
        next_nodes_coor[0-1j] = [next_up]
        next_nodes_coor[0+1j] = [next_down]

    elif node.char == '/':

        next_nodes_coor[-1+0j] = [next_right]
        next_nodes_coor[1+0j] = [next_left]
        next_nodes_coor[0-1j] = [next_down]
        next_nodes_coor[0+1j] = [next_up]

    return next_nodes_coor

# Part 1 could be done by coding the trajectory (coordinates and direction) of the beam(s) with complex numbers (x = real, y = img; *j = -90° *-j = 90°, *-1 = +180°)
# For flexibility a 'linked nodes', hashmap and complex numbers approach will be taken (useful for part 2? YES, this first approach was tried and is ok for part 1 but would take too long for part 2)
if __name__ == '__main__':

    layout_nodes = {}
    layout_array = []

    with open(f'day_16.1-test.txt') as data:
        
        for idx_line, line in enumerate(data.readlines()):
            layout_array.append([Node(char, (idx_line, idx_col)) if char != '.' else None for idx_col, char in enumerate(line.strip())])

            for idx_col, char in enumerate(line.strip()):
                if char != '.':
                    layout_nodes[idx_line + idx_col * 1j] = layout_array[idx_line][idx_col]

    layout_array = np.array(layout_array)

    for coordinates, node in layout_nodes.items():
        node.next_node_coor_from = get_next_nodes(node, layout_array)
    
    first_node = layout_array[0, layout_array[0, :] != None][0]
    direction = 0+1j
    print()
    print(first_node.next_node_coor_from[direction])
    print()
    # energised_tiles = set()
    # beams_list = deque()
    # beams_list.append(['start', first_node])
    # history = [['start', first_node]]

    # while beams_list:
    #     previous_node, current_node = beams_list.popleft()

    #     # print(f'List of beams {beams_list}')

    #     while current_node != None:

    #         next_node, *other_nodes = current_node.next_node_from[previous_node]

    #         print(f'{current_node} leads to {next_node} and {other_nodes} from {previous_node}')

    #         if other_nodes:

    #             for node in other_nodes:

    #                 if [current_node, node] not in history:

    #                     beams_list.append([current_node, node])
    #                     history.append([current_node, node])
                                      
    #         if next_node:

    #             print(f'Next coordinates: {next_node.coordinates}')

    #             if [current_node.coordinates, next_node.coordinates] in history:
    #                 break
                
    #             else:

    #                 history.append([current_node, next_node])
    #                 previous_node, current_node = current_node, next_node

    #         else:
    #             break

    # print(len(history))

            