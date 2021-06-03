#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""


class Rectangle(BaseGeometry):
    """ create a rectangle class """

    def __init__(self, width, height):
        """ initiate objects and call parent method """

        self.__width = width
        self.__height = height

        super().integer_validator("width", width)
        super().integer_validator("height", height)
