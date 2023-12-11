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

def find_lowest_location_2(seeds_ranges):

    for c in chunks[1:]:
        
        name_source, name_destination = regex_map.search(c).groups()

        for line in c.split('\n')[1:]:
            start_destination, start_source, span = [int(x) for x in line.split(' ')]

            for idx, (seeds_range_start, seeds_range_end) in enumerate(seeds_ranges):
                if start_source <= seeds_range_start < start_source + span:
                    print(seeds_range_start - (start_source + span))
                
                elif start_source <= seeds_range_end < start_source + span:
                    print(start_source - seeds_range_end)
                    
                    

if __name__ == '__main__':

    with open(f'day_5.txt') as data:

        # Follow the x-to-y map with a list of the seeds and connect the dots that way
        regex_map = re.compile(r'(\w+)-to-(\w+)\smap')

        chunks = data.read().strip().split('\n\n')
        seeds_planted = [int(x) for x in chunks[0].split(': ')[1].split(' ')]

        print(f'Answer to part 1: {find_lowest_location(seeds_planted)}')

        # Find if range of seeds to be planted is overlapping the source_range. If yes, swap only the overlapping range -> data struct using only ranges?
        seeds_ranges = [(seeds_planted[idx], seeds_planted[idx]+seeds_planted[idx+1]) for idx in range(0, len(seeds_planted), 2)]
        print(seeds_ranges)

        find_lowest_location_2(seeds_ranges)





