#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    if my_list is None:
        exit

    if idx < 0:
        return(my_list)
    elif idx > len(my_list) - 1:
        return(my_list)
    else:
        listcpy = my_list[:]
        listcpy[idx] = element
        return (listcpy)
