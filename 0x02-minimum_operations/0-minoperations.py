#!/usr/bin/python3
"""This module contains a minOperations Function"""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    Arguments: n - integer
    """
    no_of_operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            no_of_operations += min_operations
            n /= min_operations
        min_operations += 1
    return no_of_operations
