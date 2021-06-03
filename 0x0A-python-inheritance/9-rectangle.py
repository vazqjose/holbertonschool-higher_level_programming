#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ create a rectangle class """

    def __init__(self, width, height):
        """ initiate objects and call parent method """

        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return(self.__width * self.__height)

    def __str__(self):
        return ("[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height))
