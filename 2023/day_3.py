import re

if __name__ == '__main__':  
    with open(f'day_3.txt') as data:
        schematic: list = [line.strip() for line in data.readlines()]

    len_col: int = len(schematic)
    len_line: int  = len(schematic[0])

    symbol_star_dict: dict = {}

    regex_part: re.Pattern = re.compile(r'(\d+)')

    part_sum: int  = 0

    for l, line in enumerate(schematic):

        # Find the coordinate (line, col) of every part and their span -> search each adjacent cell to find if a symbol is near
        for part in regex_part.finditer(line):
            i = part.start()
            f = part.end()

            # Get all the coordinates around the part
            adjacent = [(l-1, y) for y in range(i-1, f+1)] + [(l+1, y) for y in range(i-1, f+1)] + [(l, i-1)] + [(l, f)]
            adjacent = [(x, y) for x, y in adjacent if 0 <= x < len_line and 0 <= y < len_col]

            # If any symbol next to it, add its value to sum then check if there are any stars around and if yes, adds the part's value to the symbol_star_dict
            for x, y in adjacent:
                cell = schematic[x][y]
                
                if not cell.isdigit() and cell != '.':
                    part_sum += int(part.group())

                    if cell == '*':
                        if (x, y) not in symbol_star_dict.keys():
                            symbol_star_dict[(x, y)] = []

                        symbol_star_dict[(x, y)].append(int(part.group()))


    print(f'Answer part 1: {part_sum}')
    print(f'Answer part 2: {sum([star[0]*star[1] for star in symbol_star_dict.values() if len(star) == 2])}') # Calculates the sum of all of the gear ratios