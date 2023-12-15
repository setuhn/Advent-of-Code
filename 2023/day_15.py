
def hash_fct(entry):
    current_value = 0

    for char in entry:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    return current_value

if __name__ == '__main__':
    with open(f'day_15.txt') as data:
        entries = data.read().strip().split(',')

    
    print(f'Answer for part 1: {sum([hash_fct(e) for e in entries])}')
