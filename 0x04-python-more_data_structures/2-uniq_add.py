#!/usr/bin/python3
def uniq_add(my_list=[]):

    uniqueList = []
    total = 0

    for item in my_list:
        if item not in uniqueList:
            uniqueList.append(item)
            total = total + item

    return total
