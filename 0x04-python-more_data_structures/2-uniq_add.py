#!/usr/bin/python3
# 2-uniq_add.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def uniq_add(my_list=[]):
    """Adds all unique integers in a list (once for each integer)"""
    uniq_elements = set(my_list)
    total = sum(uniq_elements)
    return total
