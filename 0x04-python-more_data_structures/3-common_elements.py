#!/usr/bin/python3
# 3-common_element.py
# Ikundwila Mwambona <ikumwana@gmail.com>

def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets"""
    common_elements = set_1 & set_2
    return common_elements
