#!/usr/bin/python3
""" lets add some integers """
def add_integer(a, b=98):
    """
    a and b must be integers or floats, otherwise raise
    a TypeError exception with the message a must be an
    integer or b must be an integer
    """
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(a) is float:
        a = int(a)

    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    elif type(b) is float:
        b = int(b)

    return (a + b)
