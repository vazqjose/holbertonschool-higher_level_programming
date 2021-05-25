#!/usr/bin/python3
""" Write a class Rectangle that defines a rectangle """


class Rectangle:

    """ create a rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        rectangle = ''
        for i in range(self.height):
            rectangle = rectangle + ('#' * self.width) + '\n'
        return rectangle

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width is not an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height is not an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):

        """ validate the size variable received from calling program """

        return (self.width * self.height)

    def perimeter(self):

        """ validate the size variable received from calling program """

        if self.width == 0 or self.height == 0:
            perimeter = 0
        else:
            perimeter = (self.width * 2) + (self.height * 2)

        return perimeter
