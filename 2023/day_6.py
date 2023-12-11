import re
from math import sqrt, ceil, floor

def calculate_ways(time, distance):
    # This problem can be simplified by solveing a second degree polynomial: -t_waited**2 + time * t_waited - distance = 0
    # a = -1, b = time, c = -distance
    ways_total = 1
    for t, d in zip(time, distance):
        delta = t**2 - 4 * d # b**2 - 4 * a * c
        x1 = (t + sqrt(delta)) / 2 # (-b + sqrt(delta))/ (2 * a) as a = -1 -> (b + sqrt(delta)) / 2
        x2 = (t - sqrt(delta)) / 2 # (b - sqrt(delta)) / 2

        if x1.is_integer():
            x1 -= 1
        if x2.is_integer():
            x2 +=1
        ways_total *= floor(x1) - ceil(x2) + 1

    return ways_total

if __name__ == '__main__':

    with open(f'day_6.txt') as data:
        lines_list = data.readlines()
        time_1, distance_1 = [[int(n) for n in re.findall(r'(\d+)', line.strip())] for line in lines_list]
        time_2, distance_2 = [int(''.join(re.findall(r'(\d+)', line.strip()))) for line in lines_list]

        print(f'Answer to part 1: {calculate_ways(time_1, distance_1)}')
        print(f'Answer to part 2: {calculate_ways([time_2], [distance_2])}')






