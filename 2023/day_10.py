from itertools import permutations

ROSETTA = { # (line, col)
    '|': ((-1, 0), (1, 0)), # is a vertical pipe connecting north and south.
    '-': ((0, 1), (0, -1)), # is a horizontal pipe connecting east and west.
    'L': ((-1, 0), (0, 1)), # is a 90-degree bend connecting north and east.
    'J': ((-1, 0), (0, -1)), # is a 90-degree bend connecting north and west.
    '7': ((1, 0), (0, -1)), # is a 90-degree bend connecting south and west.
    'F': ((1, 0), (0, 1)), # is a 90-degree bend connecting south and east
}

ADJACENT = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

def get_connecting_cells(coordinate, char, boundary):
    connections = {} # index = entry_cell_coordinate, value = connecting_cell_coordinate
    new_coordinates = [(coordinate[0] + movement[0], coordinate[1] + movement[1]) for movement in ROSETTA[char] if (0 <= coordinate[0] + movement[0] < boundary) and (0 <= coordinate[1] + movement[1] < boundary)]

    for p in permutations(new_coordinates):
        if len(p) == 2:
            connections[p[0]] = p[1]
        else:
            connections = None
            break
    
    return connections

def get_circuit(map_pipes, starting_cell, boundary):
    adjacent_cell = [(starting_cell[0] + movement[0], starting_cell[1] + movement[1]) for movement in ADJACENT if (0 <= starting_cell[0] + movement[0] < boundary) and (0 <= starting_cell[1] + movement[1] < boundary)]

    for cell in adjacent_cell:
        circuit = [starting_cell]
        current_cell = starting_cell
        next_cell = cell

        while next_cell != starting_cell:

            if map_pipes[next_cell] != None and current_cell in map_pipes[next_cell].keys():
                next_cell, current_cell = map_pipes[next_cell][current_cell], next_cell
                circuit.append(current_cell)
            else:
                break

        if next_cell == starting_cell:
            break

    return circuit

if __name__ == '__main__':


    map_pipes = {}
    coordinate_start = [0, 0]

    with open(f'day_10.txt') as data:

        for idx_line, line in enumerate(data.readlines()):
            line = line.strip()
            boundary = len(line)

            for idx_col, char in enumerate(list(line)):

                # If character is 'S', store the coordinate
                if char == 'S':
                    coordinate_start = (idx_line, idx_col)

                elif char != '.':
                    # Create dict with index = coordinate of the cell (line, column) and value = (dict with index = coordinate of entry and value = coordinate of exit)
                    map_pipes[(idx_line, idx_col)] = get_connecting_cells((idx_line, idx_col), char, boundary)

                else:
                    map_pipes[(idx_line, idx_col)] = None

    # Finds the path that comes back to the starting coordinates:
    circuit = get_circuit(map_pipes, coordinate_start, boundary)

    # Find the halfway point (firthest away from the starting point)
    print(f'Answer to part 1: {len(circuit)//2}')

    # Area = 1/2 * sum[ (x1*y2 + x2*y3 ... xn*y1) - (y1*x2 + y2*x3 ... yn*x1)]
    # Then, we need to remove all the area taken by the pipe: 
    circuit_backtrack = circuit + [coordinate_start]
    sum_1 = sum([circuit_backtrack[idx][0] * circuit_backtrack[idx+1][1] for idx, _ in enumerate(circuit_backtrack[:-1])])
    sum_2 = sum([circuit_backtrack[idx][1] * circuit_backtrack[idx+1][0] for idx, _ in enumerate(circuit_backtrack[:-1])])
    
    
    print(f'Answer to part 2: {abs(sum_2-sum_1)//2-len(circuit)//2+1}')

