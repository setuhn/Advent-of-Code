from itertools import combinations
import numpy as np

if __name__ == '__main__':

    with open(f'day_11.txt') as data:

        image = []

        for idx_line, line in enumerate(data.readlines()):
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

        # Calculate the distance between all the pairs of gaalxies combinations and sum them
        distance_total = 0
        for pair in combinations(coordinates_galaxies, 2):
            distance_total += sum([abs(coor1-coor2) for coor1, coor2 in zip(pair[0], pair[1])])

        print(f'Answer part 1: {distance_total}')


