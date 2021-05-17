#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    list2 = []
    i = 0

    try:
        for n in my_list:
            print('{}'.format(n), end='')
            i += 1

        print()
        return i

    except IndexError:
        print("index out of range")
    except:
        print("unknown error")


