#!/usr/bin/python3
def search_replace(my_list, search, replace):

    def swapMe(item):
        if item == search:
            item = replace
        return item

    return list(map(swapMe, my_list))
