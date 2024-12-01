#!/usr/bin/env python3
"""A module that does Minimum Operations"""


def minOperations(n):
    """a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file using
    Copy All and Paste"""

    if n <= 1:
        return 0
    operations = 0
    current_h = 1
    copied = 0

    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            copied = current_h
            n //= i
    return operations
