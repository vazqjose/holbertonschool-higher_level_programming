#!/usr/bin/python3
""" this is a sample docstring """


class Square:

    """ create size class """

    def __init__(self, size=0, position=(0, 0)):

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return (self.__position)


    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")

        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")


    def area(self):

        """ validate the size variablo received from calling program """

        return (self.__size ** 2)

    def my_print(self):

        """ prints to stdout a bunch of size amount of #'s """

        if self.size is 0:
            print()
        else:
            for i in range(self.size):
                for n in range(self.size):
                    print('#', end='')
                print()
