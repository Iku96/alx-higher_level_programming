#!/usr/bin/python3
# 2-replace_in_list.py
# Ikundwila Mwambona <ikumwana@gmail.com>

def replace_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific index"""
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    my_list[idx] = element
    return my_list
