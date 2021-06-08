#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        self.x = x
        self.y = y
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return Rectangle.width.fget(self)

    @size.setter
    def size(self, value):
        Rectangle.width.fset(self, value)

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                                 self.id, self.x, self.y,
                                                 super().width))
