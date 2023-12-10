import re

if __name__ == '__main__':  
    with open(f'day_3.1-test.txt') as data:
        schematic = [line.strip() for line in data.readlines()]

    len_col = len(schematic)
    len_line = len(schematic[0])

    symbol_list: list = []
    part_dict: dict = {}

    regex_part = re.compile(r'(\d+)')

    sum = 0

    for l, line in enumerate(schematic):

        # Find the coordinate (line, col) of every part and their span -> search each adjacent cell to find if a symbol is near
        for part in regex_part.finditer(line):
            i = part.start()
            f = part.end()

            # all coordinate around the part
            adjacent = [(l-1, y) for y in range(i-1, f+1)] + [(l+1, y) for y in range(i-1, f+1)] + [(l, i-1)] + [(l, f)]
            adjacent = [(x, y) for x, y in adjacent if 0 <= x < len_line and 0 <= y < len_col]

            # If any symbol next to it, add its value to sum and exit for loop
            for x, y in adjacent:
                cell = schematic[x][y]
                if not cell.isdigit() and cell != '.':
                    sum += int(part.group())
                    break

    print(f'Answer part 1: {sum}')

                # part_dict[(l, i)] = part.group()

        # # Find the coordinate (line, col) of every symbol -> search the adjacent cells and add the value to sum if a part is found
        # for symbol in regex_symbol.finditer(line):
        #     symbol_list.append((l, symbol.start()))


