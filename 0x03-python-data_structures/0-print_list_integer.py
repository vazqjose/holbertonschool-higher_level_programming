#!/usr/bin/python3
def print_list_integer(my_list=[]):
        if len(my_list) == 0:
            return (None)

        for n in my_list:
            print('{:d}'.format(n))
