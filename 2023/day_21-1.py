def get_adjacent_cells(coordinates, map_garden, boundary):
    return [(coordinates[0] + move[0], coordinates[1] + move[1]) for move in [(0, 1), (0, -1), (1, 0), (-1, 0)] 
            if (0 <= coordinates[0] + move[0] < boundary[0]) 
            and (0 <= coordinates[1]+move[1] < boundary[1])
            and (map_garden[(coordinates[0] + move[0], coordinates[1] + move[1])] != 1)
            ]

if __name__ == '__main__':
    map_garden = {}

    with open(f'day_21.txt') as data:
        for idx_line, line in enumerate(data.readlines()):
            for idx_col, char in enumerate(line.strip()):
                map_garden[(idx_line, idx_col)] = 1 if char == '#' else 0

                if char == 'S':
                    starting_coordinates = (idx_line, idx_col)
        boundary = (idx_line, idx_col)

    steps = 0
    q = set()
    q.add(starting_coordinates)
    next_q = set()

    while steps < 64:

        while q:

            current_coordinates = q.pop()

            for next_coordinates in get_adjacent_cells(current_coordinates, map_garden, boundary):
                next_q.add((next_coordinates))

        
        q = next_q.copy()
        next_q.clear()
        steps +=1

    print(f'Answer part 1: {len(q)}')
