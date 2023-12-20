#!/usr/bin/python3
# 2-safe_print_list_integers.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers"""
    numberOfIntegers = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                numberOfIntegers += 1
        except IndexError:
            raise
        except ValueError:
            break
    print()
    return (numberOfIntegers)
