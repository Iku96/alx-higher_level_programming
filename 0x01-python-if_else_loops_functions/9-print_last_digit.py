#!/usr/bin/python3
# Function returns last digit

def print_last_digit(number):
    """ Returns the last digit of a number """
    last_digit = abs(number) % 10
    if number < 0:
        return -last_digit
    else:
        return last_digit
