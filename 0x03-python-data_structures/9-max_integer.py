#!/usr/bin/python3
# 9-max_integer.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def max_integer(my_list=[]):
    if my_list == []:
        return None
    maxNum = my_list[0]
    for num in my_list:
        if num > maxNum:
            maxNum = num
    return maxNum
