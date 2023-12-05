#!/usr/bin/python3
# 1-element_at.py
# Ikundwila Mwambona <ikumwana@gmail.com>

def element_at(my_list, idx):
    """Retrieves an element from a list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return none
    else:
        return my_list[idx]
