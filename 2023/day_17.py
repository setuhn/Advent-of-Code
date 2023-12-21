
from collections import deque

ADJACENT = [
    (0+1j),
    (1+0j),
    (0-1j),
    (-1+0j)
]

def distance_coor(coor1, coor2):
    return abs(int(coor1.real - coor2.real)) + abs(int(coor1.imag - coor2.imag))

def get_next_coor_direct_from(path, boundary):
    _, _, coordinates, direction, countdown = path

    next_coordinates_directions = [(coordinates + direct, direct) for direct in ADJACENT 
                        if (direct != -1 * direction) 
                        and not (countdown == 0 and direct == direction) 
                        and not (coordinates + direct).real < 0 
                        and not (coordinates + direct).imag < 0
                        and not (coordinates + direct).real > boundary.real
                        and not (coordinates + direct).imag > boundary.imag]

    return next_coordinates_directions

### REVIEW this binary search or -> bisect.bisect_left
def insert_path_in(path, path_list: deque) -> None:
    print('insert')
    heat_loss = path[0]
    distance = path[1]

    if heat_loss < path_list[0][0] or heat_loss == path_list[0][0] and distance < path_list[0][1]:
        path_list.appendleft(path)
    
    elif heat_loss > path_list[-1][0] or heat_loss == path_list[-1][0] and distance < path_list[-1][1]:
        path_list.append(path)

    else:
        find = False
        idx_i = 0
        idx_f = len(path_list)

        while not find:
            if idx_i == idx_f:
                path_list.insert(idx_i, path)
            else:
                idx_new = (idx_f - idx_i) // 2

                if heat_loss == path_list[idx_new][0]:

                    if distance < path_list[idx_new][1]:
                        idx_f = idx_new-1
                
                    elif distance > path_list[idx_new][1]:
                        idx_i = idx_new+1

                elif heat_loss < path_list[idx_new][0]:
                    idx_f = idx_new-1
                
                elif heat_loss > path_list[idx_new][0]:
                    idx_i = idx_new+1



# Part 1: pathfinding (A*, breadth search with minimise the sum of heat loss and distance)
if __name__ == '__main__':

    map_heat_loss = {}

    with open(f'day_17.1-test.txt') as data:

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

        path_sorted_list.append((map_heat_loss[start_cell], distance_coor(start_cell, end_cell), start_cell, direction, countdown)) # heat_loss_tot, distance, coordinates, direction, countdown
        history.update([(start_cell, direction, map_heat_loss[start_cell])]) #coordinates, direction, heat_loss_tot

    # print(history)

    while path_sorted_list:

        current_path = path_sorted_list.popleft()

        next_countdown = current_path[4] -1 if current_path[4] > 0 else countdown_max

        for next_coordinates, next_direction in get_next_coor_direct_from(current_path, end_cell):

            next_heat_loss_tot = current_path[0] + map_heat_loss[next_coordinates]
            next_distance = distance_coor(end_cell, next_coordinates)

            if next_coordinates == end_cell:
                print(next_heat_loss_tot, next_distance, next_coordinates, next_direction, next_countdown)
                path_sorted_list = ()
                break

            if (next_coordinates, next_direction, next_heat_loss_tot) in history:
                continue

            else:
                # print(history)
                history.update([(next_coordinates, next_direction, next_heat_loss_tot)])
                next_path = (next_heat_loss_tot, next_distance, next_coordinates, next_direction, next_countdown)

                insert_path_in(next_path, path_sorted_list)

                # print(next_path)
            