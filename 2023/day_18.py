import re
import timeit
start = timeit.default_timer()

ROSETTA = {
    'R': 1j,
    'L': -1j,
    'D': 1,
    'U': -1
}

COLOUR2DIR = {
    '0': 1j,
    '1': 1,
    '2': -1j,
    '3': -1
}

# Area = 1/2 * sum[ (x1*y2 + x2*y3 ... xn*y1) - (y1*x2 + y2*x3 ... yn*x1)]
# Add the perimeter
def area_from_coordinates(coordinates_list):
    sum_1 = sum([coordinates_list[idx].real * coordinates_list[idx+1].imag for idx, _ in enumerate(coordinates_list[:-1])])
    sum_2 = sum([coordinates_list[idx].imag * coordinates_list[idx+1].real for idx, _ in enumerate(coordinates_list[:-1])])
    sum_3 = sum([abs(coordinates_list[idx].real - coordinates_list[idx+1].real) + abs(coordinates_list[idx].imag - coordinates_list[idx+1].imag) for idx, _ in enumerate(coordinates_list[:-1])])
    return int(abs(sum_1- sum_2) + sum_3 )//2 + 1

# The first five hexadecimal digits encode the distance in meters as a five-digit hexadecimal number
# The direction to dig: 0 means R, 1 means D, 2 means L, and 3 means U.
def convert_colour_to_instructions(colour):
    return (COLOUR2DIR[colour[-1]], int(colour[:-1], 16))

# Inspiration from day 10 for the area calculation
if __name__ == '__main__':

    coordinates_list = [0*1j]
    coordinates_list_swapped = [0*1j]

    regex = re.compile(r'(\w)\s(\d+)\s\(#(\w+)\)')

    with open(f'day_18.txt') as data:
        for line in data.readlines():
            direction, distance, colour = regex.match(line.strip()).groups()
            coordinates_list.append(coordinates_list[-1] + int(distance) * ROSETTA[direction])

            direction, distance = convert_colour_to_instructions(colour)
            coordinates_list_swapped.append(coordinates_list_swapped[-1] + int(distance) * direction)

    print(f'Answer part 1: {area_from_coordinates(coordinates_list)}')
    print(f'Answer part 2: {area_from_coordinates(coordinates_list_swapped)}')
    print(f'Time :{timeit.default_timer() - start} s')