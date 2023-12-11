import re
from itertools import cycle
import math

def part_1(map, instructions):
    current_node = 'AAA'

    for counter, instr in enumerate(cycle(list(instructions))):
        counter += 1

        current_node = map[current_node][0 if instr == 'L' else 1]

        if current_node == 'ZZZ':
            break
    
    return counter

# Find if at some point the patterns reaches an ending node (ends with Z) then calculate when they align
def part_2(map, instructions):
    current_nodes = [node for node in map if node[-1] == 'A']

    steps = 1

    for idx_for, instr in enumerate(cycle(list(instructions))):

        current_nodes = [map[node][0 if instr == 'L' else 1] for node in current_nodes]

        for node in current_nodes:
            if node[-1] == 'Z':
                current_nodes.pop(current_nodes.index(node))
                steps = math.lcm(steps, idx_for + 1)

        if len(current_nodes) == 0:
            break

    return steps

if __name__ == '__main__':

    with open(f'day_8.txt') as data:
        instructions, network = data.read().strip().split('\n\n')

        regex = re.compile(r'(\w+)\s=\s\((\w+),\s(\w+)\)')

        map = {}
        for node in network.split('\n'):
            name, left, right = regex.search(node).groups()
            map[name] = (left, right)

    print(f'Answer part 1: {part_1(map, instructions)}')
    print(f'Answer part 2: {part_2(map, instructions)}')
