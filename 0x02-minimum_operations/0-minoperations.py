#!/usr/bin/python3
"""This module contains a function that returns a list of lists of integers representing the Pascal's triangle of n"""


def minOperations(n):
    """Returns a list of lists of integers representing the Pascal's triangle of n"""
    # If n is less than or equal to 0, return an empty list
    if n < 2:
        return 0

    # Initialize the number of operations to 0
    num_operations = 0

    # While n is greater than 1
    while n > 1:
        # If n is divisible by 2
        if n % 2 == 0:
            # Divide n by 2
            n = n / 2
        # If n is not divisible by 2
        else:
            # Add 1 to n
            n = n + 1
        # Add 1 to the number of operations
        num_operations += 1

    # Return the number of operations
    return num_operations
