#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):

    newlist = []

    for i in range(len(my_list)):
        newlist.append(my_list[i] * number)

    return newlist
