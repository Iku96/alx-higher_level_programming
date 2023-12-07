#!/usr/bin/python3
# 1-search_replace.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by another in a new list"""
    new_list = []
    for number in my_list:
        if number == search:
            number = replace
        new_list.append(number)
    return new_list
