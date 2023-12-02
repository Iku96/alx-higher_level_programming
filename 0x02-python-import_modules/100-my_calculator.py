#!/usr/bin/python3
# 100-my_calculator.py
# Ikundwila Mwambona <ikumwana@gmail.com>

if __name__ == "__main__":
    """Imports all functions from the file calculator_1.py and
        handles basic operations."""
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    match operator:
        case '+':
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        case '-':
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        case '*':
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        case '/':
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")

    exit(1)
