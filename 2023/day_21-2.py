from collections import deque
import timeit
start = timeit.default_timer()

def get_adjacent_cells(coordinates, map_garden, boundary):
    adjacent_cells = [[coordinates[0] + move[0], coordinates[1] + move[1]] for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]]

    for cell in adjacent_cells:
        for i, c in enumerate(cell):
            if c < 0:
                cell[i] = boundary[i] + c
            elif c > boundary[i] - 1:
                cell[i] = c - boundary[i]
    
    return [tuple(cell) for cell in adjacent_cells if map_garden[tuple(cell)] != 1]

if __name__ == '__main__':
    map_garden = {}

    with open(f'day_21.1-test.txt') as data:
        for idx_line, line in enumerate(data.readlines()):

            for idx_col, char in enumerate(line.strip()):

                map_garden[(idx_line, idx_col)] = 1 if char == '#' else 0

                if char == 'S':
                    starting_coordinates = (idx_line, idx_col)

        boundary = (idx_line, idx_col)

    steps = 0
    q = deque()
    history = deque()
    history.append(starting_coordinates)
    set_coordinates = set()
    set_coordinates.add(starting_coordinates)
    q.append((history, set_coordinates, steps))

    steps_max = 26501365

    finished_paths = []

    while q:
        current_history, current_set_coordinates, current_steps = q.popleft()
        current_coordinates = current_history[-1]

        for next_coordinates in get_adjacent_cells(current_coordinates, map_garden, boundary):

            # If cell has already been visited (-> loop completed) or step == step max (path finished)
            if next_coordinates in current_set_coordinates or current_steps == steps_max:
                finished_paths.append(current_history)
                continue
            
            # Otherwise, continue adding the coordinates to the history and set
            next_history = current_history.copy()
            next_history.append(next_coordinates)

            next_set_coordinates = current_set_coordinates.copy() 
            next_set_coordinates.add(next_coordinates)
            
            q.append((next_history, next_set_coordinates, current_steps + 1))

    print(f'Time :{timeit.default_timer() - start} s')
    print(f'Answer part 2: {len(q)}')


