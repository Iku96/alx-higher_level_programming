#!/usr/bin/python3
# Function returns last digit

def print_last_digit(number):
    """ Returns the last digit of a number """
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
