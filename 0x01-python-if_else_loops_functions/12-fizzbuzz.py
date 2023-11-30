#!/usr/bin/python3
# 12-fizzbuzz.py
# Author: Iku

"""
Function: prints numbers 1 to 100 separated by space
Prototype: def fizzbuzz():
Description: prints Fizz for multiples of 3, Buzz for multiples of 5,
             and FizzBuzz for multiples of both 3 and 5
"""


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0 and number % 5 != 0:
            print("Fizz", end=" ")
        elif number % 5 == 0 and number % 3 != 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(number), end=" ")
