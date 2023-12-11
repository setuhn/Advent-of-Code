# import pandas as pandas
import re
import numpy as np

def find_lowest_location(seeds_list):
    history = {'seed': seeds_list}
    for c in chunks[1:]:
        
        name_source, name_destination = regex_map.search(c).groups()

        current_values = history[name_source]
        history[name_destination] = current_values.copy()

        for line in c.split('\n')[1:]:
            start_destination, start_source, span = [int(x) for x in line.split(' ')]

            for idx, value in enumerate(current_values):
                if start_source <= value < start_source + span:
                    history[name_destination][idx] = start_destination + value - start_source
                    
    return min(history['location'])

if __name__ == '__main__':

    with open(f'day_5.txt') as data:

        # Follow the x-to-y map with a list of the seeds and connect the dots that way
        regex_map = re.compile(r'(\w+)-to-(\w+)\smap')

        chunks = data.read().strip().split('\n\n')
        seeds_planted = [int(x) for x in chunks[0].split(': ')[1].split(' ')]

        print(f'Answer to part 1: {find_lowest_location(seeds_planted)}')

        # Find out if range of seeds to be planted in overlapping the source_range. If yes, swap only the overlapping range 



        





