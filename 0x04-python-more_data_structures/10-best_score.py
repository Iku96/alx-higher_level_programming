#!/usr/bin/python3
# 10-best_score.py
# Ikundwila Mwambona <ikumwana@gmail.com>


def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
