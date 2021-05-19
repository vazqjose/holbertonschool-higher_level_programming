#!/usr/bin/python3


""" lets add an attribute to our class """


class Square:
    """ create the size attribute """

    def __init__(self, size=0):
        self.__size = size

    def validate(self):

        """ validate the size variablo received from calling program """

        if not self.__size.isdigit():
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")
