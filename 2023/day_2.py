import re 

def part_1_2(games_list: list) -> tuple:
    max_colour_num = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    sum_1 = sum_2 = 0

    for games in games_list:
        id = int(re.findall('Game\s(\d+)', games)[0])
        red_max = max([int(x) for x in re.findall('(\d+)\sred', games)])
        green_max = max([int(x) for x in re.findall('(\d+)\sgreen', games)])
        blue_max = max([int(x) for x in re.findall('(\d+)\sblue', games)])

        red = max_colour_num['red'] >= red_max
        green = max_colour_num['green'] >=  green_max
        blue = max_colour_num['blue'] >= blue_max

        if red and green and blue:
            sum_1 += id
        
        power = red_max * green_max * blue_max
        sum_2 += power
    
    return (sum_1, sum_2)

if __name__ == '__main__':  
    with open(f'day_2.txt') as data:
        games_list = data.readlines()

    part_1, part_2 = part_1_2(games_list)
    print(f'Answer part 1: {part_1}')
    print(f'Answer part 2: {part_2}')

    