import numpy as np

ROCKS = {
    'O': 0,
    '#': 2,
    '.': 1
}

def tilt_platform(plateform_array):
    # Find out where the square rocks are
    # Divide the columns at their idx 
    # Order the chunks
    for idx_col in range(plateform_array.shape[1]):
        delimiters = np.where(plateform_array[:, idx_col] == 2)[0].tolist()

        if delimiters:
            
            plateform_array[:delimiters[0], idx_col] = np.sort(plateform_array[:delimiters[0], idx_col])
        
            for idx_del, delimiter in enumerate(delimiters[1:], 1):
                plateform_array[delimiters[idx_del - 1]+1:delimiter, idx_col] = np.sort(plateform_array[delimiters[idx_del - 1]+1:delimiter, idx_col])
            
            plateform_array[delimiters[-1] + 1:, idx_col] = np.sort(plateform_array[delimiters[-1] + 1:, idx_col])
        
        else:
            plateform_array[:, idx_col] = np.sort(plateform_array[:, idx_col])

    return plateform_array

def cycle(plateform_array):

    for _ in range(4):
        plateform_array = np.rot90(tilt_platform(plateform_array), -1)

    return plateform_array

def calculate_load(plateform_array):
    load = 0
    for idx_row in range(plateform_array.shape[1]):
        load += np.count_nonzero(plateform_array[idx_row, :] == 0) * (plateform_array.shape[1] - idx_row)
    
    return load

# Part 1 could be solved by iterating over each line and col at the beginning and looking backward for each char 
# 'O' if there is space to fall -> one loop solving however, this would not be a very flexible solution
if __name__ == '__main__':
    plateform = []

    with open(f'day_14.txt') as data:
        for line in data.readlines():
            plateform.append([ROCKS[char] for char in line.strip()])

    plateform_array = np.array(plateform)

    plateform_array_tilted = tilt_platform(np.copy(plateform_array))
    
    print(f'Answer to part 1: {calculate_load(plateform_array_tilted)}')

    # Part 2: make part 1 as a function -> rotate 90° between each call to the function
    # 94941 and 95024 too low
    history = []
    number_cycles = 1000000000
    cyclic_idx = False
    for _ in range(number_cycles):
        
        plateform_array = cycle(plateform_array)

        for idx_h, plateform in enumerate(history):

            if np.array_equal(plateform, plateform_array):
                cyclic_idx = idx_h
                break

        if cyclic_idx != False:
            break
        
        else:
            history.append(np.copy(plateform_array))

    cyclic_history = history[cyclic_idx:]

    num = (number_cycles - cyclic_idx - 1) % len(cyclic_history)
    # print([calculate_load(h) for h in cyclic_history])

    print(f'Answer to part 2: {calculate_load(cyclic_history[num])}')