#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square to inherit from Rectangle """

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

    def update(self, *args, **kwargs):
        """
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """

        if len(args) > 0:
            for key, val in enumerate(args):
                if key == 0:
                    self.id = val
                if key == 1:
                    self.size = val
                if key == 2:
                    self.x = val
                if key == 3:
                    self.y = val
        else:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                if key == "size":
                    self.size = val
                if key == "x":
                    self.x = val
                if key == "y":
                    self.y = val

    def to_dictionary(self):
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
