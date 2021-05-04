#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        exit

    return my_string.translate({ord('c'): None, ord('C'): None})
