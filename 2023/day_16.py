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
    
    # Find the next coordinates (up, down, right left) and if no nodes, returns the last cell's coordinates. then adds the directions after passing through the node
    next_down = [next_nodes_coor_list['down'][0].coordinates if any(next_nodes_coor_list['down']) else (boundary_line-1, idx_col), 1+0j]
    next_up = [next_nodes_coor_list['up'][-1].coordinates if any(next_nodes_coor_list['up']) else (0, idx_col), -1+0j]
    next_right = [next_nodes_coor_list['right'][0].coordinates if any(next_nodes_coor_list['right']) else (idx_line, boundary_col-1), 0+1j]
    next_left = [next_nodes_coor_list['left'][-1].coordinates if any(next_nodes_coor_list['left']) else (idx_line, 0), 0-1j]

    # Find the list of cells between the node and the next_node (or cell)
    next_down.append(tuple((y, idx_col) for y in range(idx_line, next_down[0][0] + 1)))
    next_up.append(tuple((y, idx_col, ) for y in range(next_up[0][0], idx_line)))
    next_right.append(tuple((idx_line, x) for x in range(idx_col, next_right[0][1] + 1)))
    next_left.append(tuple((idx_line, x) for x in range(next_left[0][1], idx_col)))

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

def part_1(starting_cell, direction):

    if all(layout_array[starting_cell[0], :] == None):
        return 0

    if direction.real == 0:
        first_node = layout_array[starting_cell[0], layout_array[starting_cell[0], :] != None][0 if direction.imag > 0 else -1]
    else:
        first_node = layout_array[layout_array[:, starting_cell[1]] != None, starting_cell[1]][0 if direction.real > 0 else -1]
        
    ## TODO fill in initial energised set
    energised_cells = set(find_cells_between_coordinates(starting_cell, first_node.coordinates))
    history = [(first_node.coordinates, direction)]

    beams_list = deque()
    beams_list.append((first_node.coordinates, direction))

    while beams_list:

        current_node_coordinates, direction = beams_list.pop()
        current_node = layout_array[current_node_coordinates[0]][current_node_coordinates[1]]

        for next_node_coordinates, next_direction, cell_E in current_node.next_node_coor_from[direction]:
            # print(f'{current_node_coordinates} -> {next_node_coordinates}')

            if cell_E:
                energised_cells.update(cell_E)
            
            if layout_array[next_node_coordinates[0]][next_node_coordinates[1]]:

                if (next_node_coordinates, next_direction) not in history:

                    history.append((next_node_coordinates, next_direction))
                    beams_list.append((next_node_coordinates, next_direction))

    return len(energised_cells)

def find_cells_between_coordinates(coor1, coor2):
    x1, y1 = coor1
    x2, y2 = coor2

    if x1 == x2:
        return [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    elif y1 == y2:
        return [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]

    else:
        print('ERROR')

# Part 1 could be done by coding the trajectory (coordinates and direction) of the beam(s) with complex numbers (x = real, y = img; *j = -90° *-j = 90°, *-1 = +180°)
# For flexibility a 'linked nodes', hashmap and complex numbers approach will be taken (useful for part 2? YES, this first approach was tried and is ok for part 1 but would take too long for part 2)
if __name__ == '__main__':

    layout_nodes = {}
    layout_array = []

    with open(f'day_16.txt') as data:
        
        for idx_line, line in enumerate(data.readlines()):
            layout_array.append([Node(char, (idx_line, idx_col)) if char != '.' else None for idx_col, char in enumerate(line.strip())])

            for idx_col, char in enumerate(line.strip()):

                if char != '.':
                    layout_nodes[idx_line + idx_col * 1j] = layout_array[idx_line][idx_col]

    layout_array = np.array(layout_array)

    for coordinates, node in layout_nodes.items():
        node.next_node_coor_from = get_next_nodes(node, layout_array)

    print(f'Answer to part 1: {part_1((0, 0), 0+1j)}')

    E = 0
    
    for direction in [(0+1j), (1+0j), (0-1j), (-1+0j)]:
        size = layout_array.shape[abs(int(direction.imag))]

        for idx in range(size):

            starting_cell = ({0: idx, 1: 0, -1: size - 1}[int(direction.real)], {0: idx, 1: 0, -1: size - 1}[int(direction.imag)])
            energy = part_1(starting_cell, direction)
            
            if energy > E:
                E = energy

    print(f'Answer to part 2: {E}')