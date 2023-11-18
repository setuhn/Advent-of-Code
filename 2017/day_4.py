count_1 = 0
count_2 = 0

with open('2017/input_4') as data:
    for line in data.readlines():
        list_full = line.split()
        list_reduced = set(list_full)

        if len(list_full) == len(list_reduced):
            count_1 += 1

            list_reduce_2 = set( ''.join(sorted(s)) for s in list_full)

            if len(list_full) == len(list_reduce_2):
                count_2 += 1
                
print(f'Answer part 1: {count_1}')
print(f'Answer part 2: {count_2}')
