import numpy as np

def find_symmetry_axe(pattern):
    num_rows, num_cols = pattern.shape

    # Vertical symmetry
    for idx_col in range(1, num_cols//2 + 1):

        original_pattern_left = pattern[:, : idx_col]
        original_pattern_right = pattern[:, num_cols - idx_col : num_cols]

        if idx_col > 1:
            reflected_pattern_left = np.fliplr(original_pattern_left)
            reflected_pattern_right = np.fliplr(original_pattern_right)

        else:
            reflected_pattern_left = original_pattern_left
            reflected_pattern_right = original_pattern_right

        size_reflexion_half = min(idx_col, num_cols - idx_col)

        comparison_pattern_left = pattern[:, idx_col : idx_col + size_reflexion_half]
        comparison_pattern_right = pattern[:, num_cols - idx_col - size_reflexion_half : num_cols - idx_col]

        if np.array_equal(reflected_pattern_left, comparison_pattern_left):
            return idx_col
        
        elif np.array_equal(reflected_pattern_right, comparison_pattern_right):
              return num_cols - idx_col
        
    # Horizontal symmetry
    for idx_row in range(1, num_rows//2 + 1):

        original_pattern_up = pattern[: idx_row, :]
        original_pattern_down = pattern[num_rows - idx_row : num_rows]

        if idx_row > 1:
            reflected_pattern_up = np.flipud(original_pattern_up)
            reflected_pattern_down = np.flipud(original_pattern_down)

        else:
            reflected_pattern_up = original_pattern_up
            reflected_pattern_down = original_pattern_down

        size_reflexion_half = min(idx_row, num_rows - idx_row)

        comparison_pattern_up = pattern[idx_row : idx_row + size_reflexion_half, :]
        comparison_pattern_down = pattern[num_rows - idx_row - size_reflexion_half : num_rows - idx_row, :]

        if np.array_equal(reflected_pattern_up, comparison_pattern_up):
            return 100 * idx_row
        
        elif np.array_equal(reflected_pattern_down, comparison_pattern_down):
              return 100 * (num_rows - idx_row)

if __name__ == '__main__':

    with open(f'day_13.txt') as data:
        patterns_pair = [np.array([[1 if char == '#' else 0 for char in list(line)] for line in pattern.split('\n')]) for pattern in data.read().strip().split('\n\n')]

        summary = sum([find_symmetry_axe(pattern) for pattern in patterns_pair])

        print(f'Answer part 1: {summary}')