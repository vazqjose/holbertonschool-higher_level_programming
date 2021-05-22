#!/usr/bin/python3
"""
Print a square with #'s

Args:
    size: lenght of square
Return:
    nothing
"""


def print_square(size):
    """ function that prints a square with the character # """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for row in range(0, size):
        for col in range(0, size):
            print('#', end='')
        print()
