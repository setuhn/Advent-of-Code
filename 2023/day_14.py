import numpy as np

ROCKS = {
    'O': 0,
    '#': 2,
    '.': 1
}

def invert_coordinates(coordinates_list):
    coordinates_list = [[col, row] for row, col in coordinates_list]
    coordinates_list.sort()

    return coordinates_list

# Part 1 could be solved by iterating over each line and col at the beginning and looking backward for each char 
# 'O' if there is space to fall -> one loop solving however, this would not be a very flexible solution
if __name__ == '__main__':
    plateform = []

    with open(f'day_14.txt') as data:
        for line in data.readlines():
            plateform.append([ROCKS[char] for char in line.strip()])

    plateform_array = np.array(plateform)

    # Find out where the square rocks are
    # Divide the columns at their idx 
    # Order the chunks
    for idx_col in range(plateform_array.shape[1]):
        delimiters = [d[0] for d in np.argwhere(plateform_array[:, idx_col] == 2)]

        if delimiters:
            plateform_array[:delimiters[0], idx_col] = np.sort(plateform_array[:delimiters[0], idx_col])
        
            for idx_del, delimiter in enumerate(delimiters):
                if delimiter != 0:
                    plateform_array[delimiters[idx_del - 1]+1:delimiter, idx_col] = np.sort(plateform_array[delimiters[idx_del - 1]+1:delimiter, idx_col])
            
            plateform_array[delimiters[-1] + 1:, idx_col] = np.sort(plateform_array[delimiters[-1] + 1:, idx_col])
        
        else:
            plateform_array[:, idx_col] = np.sort(plateform_array[:, idx_col])

    load = 0
    for idx_row in range(plateform_array.shape[1]):
        load += len(np.argwhere(plateform_array[idx_row, :] ==0)) * (plateform_array.shape[1] - idx_row)

    print(f'Answer to part 1: {load}')