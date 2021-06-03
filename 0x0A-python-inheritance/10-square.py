#!/usr/bin/python3
"""
Write a class square that inherits from Rectangle (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ create a Square class """

    def __init__(self, size):
        """ initiate objects and call parent method """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
