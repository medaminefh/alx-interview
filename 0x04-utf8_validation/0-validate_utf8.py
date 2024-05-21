#!/usr/bin/python3
"""
UTF-8 Validation 
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant bit is set or not
    mask1 = 1 << 7

    # Mask to check if the second most significant bit is set or not
    mask2 = 1 << 6
    for num in data:

        # Get the bit pattern of the current byte
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios according to the rules of the problem
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:

            # If this byte is a part of an existing UTF-8 character,
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
