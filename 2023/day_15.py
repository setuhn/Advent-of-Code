
from collections import deque

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

    lense_to_box = {}
    box = {}

    for lense in entries:

        if '=' in lense:
            label, value = lense.split('=')

            # If label not use before -> initialise: hash, create label registry and box, and add label to box
            if label not in lense_to_box.keys():
                b = hash_fct(label)
                lense_to_box[label] = [b, True, int(value)]
                if b not in box.keys():
                    box[b] = deque()
                box[b].append(label)
            # If label exists and a lense with this label is already in the box -> update value
            elif lense_to_box[label][1]:
                lense_to_box[label][2] = int(value)

            # If label exists but a lense with this label is not in the box -> append the lense and update status and value
            else:
                box[lense_to_box[label][0]].append(label)
                lense_to_box[label][1] = True
                lense_to_box[label][2] = int(value)
        
        if '-' in lense:
            label = lense[:-1]
            # If label exists and a lense with this label is in the box -> remove the lense and upfate status
            if label in lense_to_box.keys() and lense_to_box[label][1]:
                box[lense_to_box[label][0]].remove(label)
                lense_to_box[label][1] = False
    
    focus_power = 0
    for idx_box, b in box.items():
        for position, lense in enumerate(b):
            focus_power += (idx_box + 1) * (position + 1) * lense_to_box[lense][2]
    
    print(f'Answer for part 2: {focus_power}')
                
