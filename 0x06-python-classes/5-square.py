#!/usr/bin/python3
""" this is a sample docstring """


class Square:

    """ create size class """

    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """ validate the size variablo received from calling program """

        return (self.__size ** 2)

    def my_print(self):

        """ prints to stdout a bunch of size amount of #'s """

        if self.size is 0:
            print()
        else:  # i = 3
            for i in range(self.size):
                for n in range(self.size):
                    print('#', end='')
                print()
