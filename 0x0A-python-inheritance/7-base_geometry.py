#!/usr/bin/python3
"""
Write a class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """ class of base geometry """

    def area(self):
        """ raise an exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value if int """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
