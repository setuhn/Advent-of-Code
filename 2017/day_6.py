import numpy as np

with open('2017/input_6') as data:
    banks = np.array([int(n) for n in data.read().strip().split('\t')])

memory = []

while tuple(banks) not in memory:
    memory.append(tuple(banks))

    blocks = banks.max()
    idx_max = banks.argmax()
    banks[idx_max] = 0

    for i in range(blocks):
        banks[(idx_max + i + 1) % len(banks)] += 1

print(f'Answer part 1: {len(memory)}')
print(f'Answer part 2: {len(memory) - memory.index(tuple(banks))}')