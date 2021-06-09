#!/usr/bin/python3
""" Write the class Rectangle that inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ rectangle class """

    print_symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @property
    def x(self):
        return (self.__x)

    @property
    def y(self):
        return (self.__y)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 1:
                raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 1:
                raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
                raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
                raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calculate and return area: width x height
        """

        return (self.width * self.height)

    def display(self):
        """
            width: amount of #'s to print
            height: amount of lines printed
            x: blank chars to print at the start of each line
            y: new lines to print at the start
        """
        myRect = ""

        for line in range(self.y):
            myRect += "\n"

        for i in range(self.height):
            for col in range(self.x):
                myRect += " "

            myRect += str(self.print_symbol) * self.width

            if i + 1 < self.height:
                myRect += "\n"

        print(myRect)

    def __str__(self):
        """
        Lets replace the str method
        """

        return ("[{}] ({}) {}/{} - {}/{}". format(self.__class__.__name__,
                                                  self.id, self.x, self.y,
                                                  self.width, self.height))

    def update(self, *args, **kwargs):
        """
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """

        if len(args) > 0:
            for key, val in enumerate(args):
                if key == 0:
                    self.id = val
                if key == 1:
                    self.__width = val
                if key == 2:
                    self.__height = val
                if key == 3:
                    self.__x = val
                if key == 4:
                    self.__y = val
        else:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                if key == "width":
                    self.__width = val
                if key == "height":
                    self.__height = val
                if key == "x":
                    self.__x = val
                if key == "y":
                    self.__y = val

    def to_dictionary(self):
        """ Return a dictionary representation of the rectangle obj """

        return {"id":self.id, "width":self.__width, "height":self.__height,
                "x":self.__x, "y":self.__y}
