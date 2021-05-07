#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    dictionary_items = a_dictionary.items()
    sorted_items = sorted(dictionary_items)

    for key, item in sorted_items:
        print('{}: {}'.format(key, item))
