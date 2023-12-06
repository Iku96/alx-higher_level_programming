#!/usr/bin/python3
# 4-new_in_list.py
# Ikundwila Mwambona <ikumwana@gmail.com>

def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
        without modifying the original list"""
    if idx >= 0 and idx < (len(my_list) - 1):
        my_list2 = my_list.copy()
    my_list2[idx] = element
    return my_list2
