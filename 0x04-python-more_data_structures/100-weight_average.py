#!/usr/bin/python3
def weight_average(my_list=[]):

    total = 0
    totalweight = 0

    if len(my_list) == 0:
        return 0

    for mytup in my_list:
        total += mytup[0] * mytup[1]
        totalweight += mytup[1]

    return (total / totalweight)
