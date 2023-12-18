import numpy as np
from collections import deque

# take all the non '.' characters and connect them with doubly linked list -> Node
class Node:
    def __init__(self, char, coordinates):
        self.char = char
        self.coordinates = coordinates
        # reference to next nodes as key = coordinates_entry, value = (node_next, distance)
        self.next_node_from = {}

# return the next dict for the given node
def get_next_nodes(node, layout_array):
    next_nodes = {}
    next_nodes_list = {}
    idx_line, idx_col = node.coordinates
    boundary_line, boundary_col = layout_array.shape

    next_nodes_list['down'] = layout_array[idx_line+1:, idx_col][layout_array[idx_line+1:, idx_col] != None] #-> [0]
    next_nodes_list['up'] = layout_array[:idx_line, idx_col][layout_array[:idx_line, idx_col] != None] #-> [-1]
    next_nodes_list['right'] = layout_array[idx_line, idx_col+1:][layout_array[idx_line, idx_col+1:] != None] # -> [0]
    next_nodes_list['left'] = layout_array[idx_line, :idx_col][layout_array[idx_line, :idx_col] != None] # -> [-1]
    
    down_node = next_nodes_list['down'][0] if any(next_nodes_list['down']) else (boundary_line-1, idx_col)
    up_node = next_nodes_list['up'][-1] if any(next_nodes_list['up']) else (0, idx_col)
    right_node = next_nodes_list['right'][0] if any(next_nodes_list['right']) else (idx_line, boundary_col-1)
    left_node = next_nodes_list['left'][-1] if any(next_nodes_list['left']) else (idx_line, 0)

    if node.char == '|':
        
        if down_node:
            next_nodes[down_node] = [up_node]

        if up_node:
            next_nodes[up_node] = [down_node]

        if right_node:
            next_nodes[right_node] = [up_node, down_node]

        if left_node:
            next_nodes[left_node] = [up_node, down_node]

        elif idx_line == 0:
            next_nodes['start'] = [down_node]

    elif node.char == '-':

        if down_node:
            next_nodes[down_node] = [left_node, right_node]

        if up_node:
            next_nodes[up_node] = [left_node, right_node]

        if right_node:
            next_nodes[right_node] = [left_node]

        if left_node:
            next_nodes[left_node] = [right_node]

        elif idx_line == 0:
            next_nodes['start'] = [right_node]

    elif node.char == '\\':

        if down_node:
            next_nodes[down_node] = [left_node]

        if up_node:
            next_nodes[up_node] = [right_node]

        if right_node:
            next_nodes[right_node] = [up_node]

        if left_node:
            next_nodes[left_node] = [down_node]

        elif idx_line == 0:
            next_nodes['start'] = [down_node]

    elif node.char == '/':

        if down_node:
            next_nodes[down_node] = [right_node]

        if up_node:
            next_nodes[up_node] = [left_node]

        if right_node:
            next_nodes[right_node] = [down_node]

        if left_node:
            next_nodes[left_node] = [up_node]

    return next_nodes

# Part 1 could be done by coding the trajectory (coordinates and direction) of the beam(s) with complex numbers (x = real, y = img; *j = -90° *-j = 90°, *-1 = +180°)
# For flexibility a 'linked nodes' approach will be taken (useful for part 2?)
if __name__ == '__main__':

    layout = []

    with open(f'day_16.1-test.txt') as data:
        
        for idx_line, line in enumerate(data.readlines()):
            layout.append([Node(char, (idx_line, idx_col)) if char != '.' else None for idx_col, char in enumerate(line.strip())])

    layout_array = np.array(layout)
    coordinates_mirrors_splitters = np.argwhere(layout_array != None)


    for coordinates in coordinates_mirrors_splitters.tolist():
        node = layout_array[coordinates[0],  coordinates[1]]
        next_nodes = get_next_nodes(node, layout_array)
        node.next_node_from = next_nodes
    
    first_node = layout_array[coordinates_mirrors_splitters[0][0], coordinates_mirrors_splitters[0][1]]
    print()
    print(first_node.next_node_from)
    print()
    energised_tiles = set()
    beams_list = deque()
    beams_list.append(['start', first_node])
    history = [['start', first_node]]

    while beams_list:
        previous_node, current_node = beams_list.popleft()

        # print(f'List of beams {beams_list}')

        while current_node != None:

            next_node, *other_nodes = current_node.next_node_from[previous_node]

            print(f'{current_node} leads to {next_node} and {other_nodes} from {previous_node}')

            if other_nodes:

                for node in other_nodes:

                    if [current_node, node] not in history:

                        beams_list.append([current_node, node])
                        history.append([current_node, node])
                                      
            if next_node:

                print(f'Next coordinates: {next_node.coordinates}')

                if [current_node.coordinates, next_node.coordinates] in history:
                    break
                
                else:

                    history.append([current_node, next_node])
                    previous_node, current_node = current_node, next_node

            else:
                break

    print(len(history))

            