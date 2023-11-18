#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 10:30:19 2023

@author: setuhnjimaja
"""

def hex_to_4bits_bin(num: str) -> str:
    
    four_bits_bin = ''
    
    for char in num:
        four_bits_bin += bin(int(char, base=16))[2:].zfill(4)
    
    return four_bits_bin


# Packets with type ID 4 represent a literal value. Literal value packets encode 
# a single binary number. To do this, the binary number is padded with leading 
# zeroes until its length is a multiple of four bits, and then it is broken into 
# groups of four bits. Each group is prefixed by a 1 bit except the last group, 
# which is prefixed by a 0 bit. These groups of five bits immediately follow the 
# packet header. For example, the hexadecimal string 


def get_literal_value(sub_packet: str) -> tuple:
    '''return the literal value along with the trailing characters'''
    literal_value_bin = ''
    i = 0
    
    while i < len(sub_packet) - 5:
        
        literal_value_bin += sub_packet[i+1:i+5]
        
        if sub_packet[i] == '0':
            return int(literal_value_bin, base = 2), sub_packet[i+5:]
            
        i +=5
        
    return None

# An operator packet contains one or more packets. To indicate which subsequent 
# binary data represents its sub-packets, an operator packet can use one of two 
# modes indicated by the bit immediately after the packet header; this is called 
# the length type ID:

#     If the length type ID is 0, then the next 15 bits are a number that represents the 
#     total length in bits of the sub-packets contained by this packet.
#     If the length type ID is 1, then the next 11 bits are a number that represents 
#     the number of sub-packets immediately contained by this packet.

# Finally, after the length type ID bit and the 15-bit or 11-bit field, 
# the sub-packets appear.    

def get_operation(sub_packet: str) -> list:
    length_ID = sub_packet[0]
    
    operation = []
    
    #  use trailing characters and size of return to stop when size achieved
    if length_ID == '0':
        total_length = int(sub_packet[1:16], base = 2)
        trailing = total_length
        
        operation += []
        
        
        
        return transcode_packet(sub_packet[16:total_length+16])
        
    elif length_ID == '1':
        packets_number = int(sub_packet[16:28], base = 2)
    
    
    
    
def transcode_packet(packet: str) -> list:
    version = int(packet[:3], base = 2)
    type_ID = int(packet[3:6], base = 2)
    
    if type_ID == 4:
        return (version, type_ID, get_literal_value(packet[6:])[0])
    
    else:
        return (version, type_ID, get_operation(packet[6:]))
    

transmission = '38006F45291200'
packet_source = hex_to_4bits_bin(transmission)

a = transcode_packet(packet_source)