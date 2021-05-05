#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    list1 = my_list.sort()
    return list1[-1]
