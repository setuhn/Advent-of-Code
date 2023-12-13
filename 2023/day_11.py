from itertools import combinations
import numpy as np

# Calculate the distance between all the pairs of galaxies combinations and sum them
def calculate_distance(coordinates):
    distance_total = 0
    for pair in combinations(coordinates, 2):
        distance_total += sum([abs(coor1-coor2) for coor1, coor2 in zip(pair[0], pair[1])])

    return distance_total

if __name__ == '__main__':
    
    with open(f'day_11.txt') as data:
        lines = data.readlines()

    image = []

    for idx_line, line in enumerate(lines):
        # Translate '.' to 0 and '#' to 1
        line_num = [0 if char == '.' else 1 for char in list(line.strip())]
        image.append(line_num)

        # Add the new zero-filled rows
        if not any(line_num):
            image.append(line_num)

    image_array = np.array(image)

    # Find where the all-zero columns are
    zero_column_idx = np.argwhere(~image_array.any(axis=0))

    # Adjust the idx to account for the change in idx after the previous columns will have been added
    zero_column_idx_adjusted = [col + idx for idx, col in enumerate(zero_column_idx)]

    # Insert the new zero-filled columns
    for idx_col in zero_column_idx_adjusted:
        image_array = np.insert(image_array, idx_col, 0, axis=1)

    # Find the coordinates of the galaxies
    coordinates_galaxies = np.argwhere(image_array == 1).tolist()

    print(f'Answer part 1: {calculate_distance(coordinates_galaxies)}')

    ### PART 2 -> only use the coordinates of the galaxy and the empty space columns and rows to avoid filling up memory with the array (smart way)
    image = []
    extension_empty_column = 999999

    for idx_line, line in enumerate(lines):
        line_num = [0 if char == '.' else 1 for char in list(line.strip())]
        image.append(line_num)

    image_array = np.array(image)

    # Find where the all-zero columns and rows are
    zero_rows_idx = np.where(~image_array.any(axis=1))[0].tolist()
    zero_columns_idx = np.where(~image_array.any(axis=0))[0].tolist()


    # Find the coordinates of the galaxies
    coordinates_galaxies = np.argwhere(image_array == 1).tolist()

    # Adust the galaxies coordinates according to the all-zero columns positions: loop over every galaxy and when found the right interval add idx * extension_empty_column and break
    for galaxy in coordinates_galaxies:

        # row
        for rank, idx_row in enumerate(reversed(zero_rows_idx)):
            if galaxy[0] > idx_row:
                galaxy[0] += (len(zero_rows_idx) - rank) * extension_empty_column
                break
        # col
        for rank, idx_col in enumerate(reversed(zero_columns_idx)):
            if galaxy[1] > idx_col:
                galaxy[1] += (len(zero_columns_idx) - rank) * extension_empty_column
                break

    print(f'Answer part 2: {calculate_distance(coordinates_galaxies)}')
