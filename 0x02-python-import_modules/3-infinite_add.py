#!/usr/bin/python3
# 3-infinite_add.py
# Ikundwila Mwambona<ikumwana@gmail.com>

if __name__ == "__main__":
    """Prints the result of all arguments"""
    from sys import argv

    sum = 0
    for i in range(len(argv) - 1):
        sum += int(argv[i + 1])
    print("{}".format(sum))
