# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 16:54:20 2023

@author: Setuhn
"""
import re

regex_v2 = re.compile(r'\((\d+)x(\d+)\)')

def get_compression_markers(compressed_string):
    compression_info = re.finditer(r'(?<!\))\((\d+)x(\d+)\)', compressed_string)
    
    return compression_info

# TODO write a function to find it without regex by iterating through the string
def get_next_compression_marker_v2(compressed_string):
    compression_info = regex_v2.search(compressed_string)
    
    return compression_info

#  Whitespace is ignored
decompressed_data = ''
idx_current = 0

with open('input_9') as data:
    compressed_data = data.read().replace(' ', '').strip()
    
# Part 1
# for marker in get_compression_markers(compressed_data):
#     idx_start, idx_end = marker.span()
    
#     # Don't take into account the markers that are part of another markers decompression
#     if idx_start >= idx_current:
#         size, n = [int(num) for num in marker.groups()]
        
#         chunk = compressed_data[idx_end:idx_end+size]
#         decompressed_data = decompressed_data + compressed_data[idx_current:idx_start] + chunk * n
        
#         # Change the current index to after the marker's decompression's length
#         idx_current = idx_end + size 
        
# decompressed_data = decompressed_data + compressed_data[idx_current:-1]
# decompressed_data = decompressed_data

# print(len(decompressed_data))

# Part 2
# recursion is too deep -> replace with loop

size_dd = 0
marker = get_next_compression_marker_v2(compressed_data)


while marker:
    
    idx_start, idx_end = marker.span()
    
    size, n = int(marker.groups()[0]), int(marker.groups()[1])
    
    chunk = compressed_data[idx_end:idx_end+size]
    
    size_dd += idx_start
    
    decompressed_data = chunk * n + compressed_data[idx_end + size:]
    
    compressed_data = decompressed_data
    
    marker = get_next_compression_marker_v2(compressed_data)

size_dd += len(compressed_data)
print(size_dd)