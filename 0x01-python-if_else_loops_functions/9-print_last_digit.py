#!/usr/bin/python3
# Function returns last digit

def print_last_digit(number):
    """ Returns the last digit of a number """
    last_digit = abs(number) % 10
    if number < 0:
        print("{}".format(-last_digit))
    else:
        print("{}".format(last_digit))
