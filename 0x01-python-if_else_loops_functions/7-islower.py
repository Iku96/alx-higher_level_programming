#!/usr/bin/python3
# 7-islower.py
# Auth: Iku
"""
A function that checks for lowercase character
Function name: islower(c)

"""


def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
