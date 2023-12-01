#!/usr/bin/python3
# 2-args.py
# Auth: Iku<ikumwana@gmail.com>

if __name__ == "__main__":
    import sys
    argCount = len(sys.argv) - 1
    if argCount == 0:
        print("0 arguments.")
    elif argCount == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for arg in range(argCount):
        print("{}: {}".format(arg + 1, sys.argv[arg + 1]))
