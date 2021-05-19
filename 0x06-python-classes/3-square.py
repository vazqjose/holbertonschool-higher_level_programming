#!/usr/bin/python3


""" lets add an attribute to our class """


class Square:
    """ create the size attribute """

    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):

        """ validate the size variablo received from calling program """

        return (self.__size ** 2)
