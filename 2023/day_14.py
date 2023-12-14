import numpy as np

ROCKS = {
    'O': True,
    '#': False,
    '.': None
}

def invert_coordinates(coordinates_list):
    coordinates_list = [[col, row] for row, col in coordinates_list]
    coordinates_list.sort()

    return coordinates_list

# Part 1 could be solved by iterating over each line and col at the beginning and looking backward for each char 
# 'O' if there is space to fall -> one loop solving however, this would not be a very flexible solution
if __name__ == '__main__':
    plateform = []

    with open(f'day_14.1-test.txt') as data:
        for line in data.readlines():
            plateform.append([ROCKS[char] for char in line.strip()])

    plateform_array = np.array(plateform)

    coordinate_round = invert_coordinates(np.argwhere(plateform_array == True).tolist())
    coordinate_square = invert_coordinates(np.argwhere(plateform_array == False).tolist())

    # Find out where the square rocks are
    # Divide the columns at their idx 
    # Find the number of round boulder in each chunk of column 
    # Clump the round boulder together towards the north
