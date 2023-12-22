
from collections import deque
import bisect

ADJACENT = [
    (0+1j),
    (1+0j),
    (0-1j),
    (-1+0j)
]

def distance_coor(coor1, coor2):
    return abs(int(coor1.real - coor2.real)) + abs(int(coor1.imag - coor2.imag))

def get_next_coor_direct_from(path, boundary):
    _, _, _, coordinates, direction, countdown = path

    next_coordinates_directions = [(coordinates + direct, direct) for direct in ADJACENT 
                        if (direct != -1 * direction) 
                        and not (countdown == 0 and direct == direction) 
                        and not (coordinates + direct).real < 0 
                        and not (coordinates + direct).imag < 0
                        and not (coordinates + direct).real > boundary.real
                        and not (coordinates + direct).imag > boundary.imag]

    return next_coordinates_directions

def get_score(distance, heat_loss_tot):
    return distance + 0*heat_loss_tot

# Part 1: pathfinding (A*, breadth search with minimise the heat loss and distance)
# 1267, 1241
if __name__ == '__main__':

    map_heat_loss = {}

    with open(f'day_17.txt') as data:

        for idx_line, line in enumerate(data.readlines()):

            for idx_col, num in enumerate(line.strip()):

                map_heat_loss[idx_line + idx_col*1j] = int(num)

    start_cell = 0+0j
    end_cell = idx_line + idx_col*1j

    countdown_max = 3
    countdown = 3

    direction_list = [(0+1j),(1+0j)]

    path_sorted_list = deque()
    history = set()
    
    for direction in direction_list:

        path_sorted_list.append((0, distance_coor(start_cell, end_cell), map_heat_loss[start_cell], start_cell, direction, countdown)) # score, distance, heat_loss_tot, coordinates, direction, countdown
        history.update([(start_cell, direction, map_heat_loss[start_cell])]) # coordinates, direction, heat_loss_tot

    min_heat_loss = int(end_cell.real * 10 + end_cell.imag * 10)

    counter = 0
    while path_sorted_list:
        counter += 1
        # Get current path
        current_path = path_sorted_list.popleft()
        # Calculate next countdown
        next_countdown = current_path[-1] -1 if current_path[-1] > 0 else countdown_max
        # If min_heat_loss is lower than the current heat loss, prune this branch
        if min_heat_loss < current_path[2]:
            continue
        
        # Explore each different possible direction
        for next_coordinates, next_direction in get_next_coor_direct_from(current_path, end_cell):

            # Calculate next heat loss
            next_heat_loss_tot = current_path[2] + map_heat_loss[next_coordinates]

            # If heat loss is higher than min_heat_loss, prune this branch
            if min_heat_loss < next_heat_loss_tot:
                continue

            # If the coordinates are the end cell pass to the next branch
            if next_coordinates == end_cell:

                print(next_heat_loss_tot, len(path_sorted_list), counter)


                # Update the min_heat_loss if it is too high
                if min_heat_loss > next_heat_loss_tot:
                    min_heat_loss = next_heat_loss_tot

                continue

            # If the branch is already recorded, prune this branch
            if (next_coordinates, next_direction, next_heat_loss_tot) in history:
                continue

            else:
                # Update history
                history.update([(next_coordinates, next_direction, next_heat_loss_tot)])
                # Calculate next distance
                next_distance = distance_coor(end_cell, next_coordinates)
                # Construct the next path
                next_path = (get_score(next_distance, next_heat_loss_tot), next_distance, next_heat_loss_tot, next_coordinates, next_direction, next_countdown)
                # Find where to insert the new branch (1: distance, 2: heat loss)
                insert_idx = bisect.insort_left(path_sorted_list, next_path, key=lambda r: (r[0], r[2], r[1]))

    print()
    print(counter)