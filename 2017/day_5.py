#bytes operation? Numpy?
instructions = []

with open('2017/input_5') as data:
    for line in data.readlines():
        instructions.append(int(line.strip()))

instructions_save = instructions.copy()

instructions = instructions

exit = len(instructions)
current_pos = 0
count_1 = 0

while current_pos < exit:
    # How much to move
    mv = instructions[current_pos]

    # Change instruction value
    instructions[current_pos] += 1

    # Change current position
    current_pos += mv

    # Increment count
    count_1 += 1

print(f'Answer part 1: {count_1}')

current_pos = 0
count_2 = 0
instructions = instructions_save

while current_pos < exit:
    # How much to move
    mv = instructions[current_pos]

    # Change instruction value
    if mv >= 3:
        instructions[current_pos] -= 1
    else:
        instructions[current_pos] += 1

    # Change current position
    current_pos += mv

    # Increment count
    count_2 += 1

print(f'Answer part 2: {count_2}')