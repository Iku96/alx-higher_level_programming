#!/usr/bin/python3
# 0-safe_print_list.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def safe_print_list(my_list=[], x=0):
    """Prints x elements in a list"""
    counter = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            counter += 1
        except IndexError:
            break
    print()
    return counter
