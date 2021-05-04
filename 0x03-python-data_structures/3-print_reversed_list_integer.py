#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if len(my_list) is 0:
        exit

    for n in reversed(my_list):
        print('{:d}'.format(n))
