#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):

    def mult(num):
        return num * number

    newlist = []

    newlist.append(list(map(mult, my_list)))
    return newlist
