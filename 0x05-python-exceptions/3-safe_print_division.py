#!/usr/bin/python3
# 3-safe_print_division.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def safe_print_division(a, b):
    """divides two integers and prints the result"""
    try:
        quotient = a / b
    except (TypeError, ZeroDivisionError):
        quotient = None
    finally:
        print("{}".format(quotient))
