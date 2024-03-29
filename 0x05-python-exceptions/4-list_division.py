#!/usr/bin/python3
# 4-list_division.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists"""
    new_list = []
    for i in range(0, list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(quotient)
    return (new_list)
