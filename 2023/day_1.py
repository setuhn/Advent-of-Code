def part_1(coordinates_list: list) -> int:
    sum = 0

    for coordinate in coordinates_list:

        numbers = [x for x in coordinate.strip() if x.isdigit()]
        sum += int(numbers[0] + numbers[-1])

    return sum

def part_2(coordinates_list: list) -> int:
    digit_name = {'one': 'o1e',
                  'two': 't2o', 
                  'three': 't3e', 
                  'four': 'f4r',
                  'five': 'f5e',
                  'six': 's6x',
                  'seven': 's7n',
                  'eight': 'e8t',
                  'nine': 'n9e'
                  }
    sum = 0

    for coordinate in coordinates_list:
        
        for word, replace in digit_name.items():
            coordinate = coordinate.replace(word, replace)

        numbers = [x for x in coordinate.strip() if x.isdigit()]
        sum += int(numbers[0] + numbers[-1])
    
    return sum


if __name__ == '__main__':  
    with open(f'day_1.txt') as data:
        coordinates_list = data.readlines()

    print(f'Answer part 1: {part_1(coordinates_list)}')
    print(f'Answer part 2: {part_2(coordinates_list)}')