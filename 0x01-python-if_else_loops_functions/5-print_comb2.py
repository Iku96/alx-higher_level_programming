#!/usr/bin/python3
# 5-print_comb2.py
# Auth: Ikundwila

""" prints numbers from 0 to 99. """
for i in range(100):
    if i == 99:
        print("{}".format(99))
    else:
        print("{:02},".format(i), end=" ")
