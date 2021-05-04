#!/usr/bin/python3
def print_list_integer(my_list=[]):

    length = len(my_list)
    if length == 0:
        return (None)

    for n in range(0, length):
        print('{}'.format(my_list[n]))
