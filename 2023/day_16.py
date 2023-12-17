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

    next_nodes_list['down'] = layout_array[idx_line+1:, idx_col][layout_array[idx_line+1:, idx_col] != None] #-> [0]
    next_nodes_list['up'] = layout_array[:idx_line, idx_col][layout_array[:idx_line, idx_col] != None] #-> [-1]
    next_nodes_list['right'] = layout_array[idx_line, idx_col+1:][layout_array[idx_line, idx_col+1:] != None] # -> [0]
    next_nodes_list['left'] = layout_array[idx_line, :idx_col][layout_array[idx_line, :idx_col] != None] # -> [-1]
    
    down_node = next_nodes_list['down'][0] if any(next_nodes_list['down']) else None
    up_node = next_nodes_list['up'][-1] if any(next_nodes_list['up']) else None
    right_node = next_nodes_list['right'][0] if any(next_nodes_list['right']) else None
    left_node = next_nodes_list['left'][-1] if any(next_nodes_list['left']) else None

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
    coordinates_mirrors_splitters = np.argwhere(layout_array)


    for coordinates in coordinates_mirrors_splitters.tolist():
        node = layout_array[coordinates[0],  coordinates[1]]
        next_nodes = get_next_nodes(node, layout_array)
        node.next = next_nodes
        for previous_node, next_node in next_nodes.items():
            if not isinstance(previous_node, Node):
                starting_node = node
    
    energised_tiles = set()
    beams = deque(starting_node)