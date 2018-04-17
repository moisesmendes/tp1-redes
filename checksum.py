#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        checksum.py
#
# Author:      Grant Curell
#
# Created:     16 Sept 2012
#
# Description: Calculates the checksum for an IP header
#-------------------------------------------------------------------------------
    
    
def ip_checksum(ip_header, size):
    
    cksum = 0
    pointer = 0
    
    #The main loop adds up each set of 2 bytes. They are first converted to strings and then concatenated
    #together, converted to integers, and then added to the sum.
    while size > 1:
        cksum += int((str("%02x" % (ip_header[pointer],)) + 
                      str("%02x" % (ip_header[pointer+1],))), 16)
        size -= 2
        pointer += 2
    if size: #This accounts for a situation where the header is odd
        cksum += ip_header[pointer]
        
    cksum = (cksum >> 16) + (cksum & 0xffff)
    cksum += (cksum >>16)
    
    return (~cksum) & 0xFFFF
    
# -----------------------------
# USING THE CODE 

import checksum

header = {}

header[0] = 0x45
header[1] = 0x00
header[2] = 0x00
header[3] = 0xe8
header[4] = 0x00
header[5] = 0x00
header[6] = 0x40
header[7] = 0x00
header[8] = 0x40
header[9] = 0x11
header[10] = 0x0
header[11] = 0x0
header[12] = 0x0a
header[13] = 0x86
header[14] = 0x33
header[15] = 0xf1
header[16] = 0x0a
header[17] = 0x86
header[18] = 0x33
header[19] = 0x76

print("Checksum is: %x" % (checksum.ip_checksum(header, len(header)),))
print("Should be BD92")


