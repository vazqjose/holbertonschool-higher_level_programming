#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """
    class MyList that inherits from list
    """

    def print_sorted(self):
        """ return sorted list """

        print(sorted(self))
