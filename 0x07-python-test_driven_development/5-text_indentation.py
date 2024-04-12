#!/usr/bin/python3
# 5-text_indentation.py
# Ikundwila N Mwambona <ikumwana@gmail.com>
"""
This is the 5-text_indentation module.
It contains a function that prints a text with two new lines after
each of these characters: ".", "?", ":"
"""


def text_indentation(text):
    """This function prints a text with two new lines after
        each of these characters: ".", "?", ":"

    Args:
        text: The text to be rearranged
    Returns:
        None.
    """
    # Check to make sure text is a string
    if not isinstance(text, str):
        # Raise an TypeError if it's not a string
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    while ' .\n\n' in text:
        text = text.replace(' .\n\n', '.\n\n')
    while ' ?\n\n' in text:
        text = text.replace(' ?\n\n', '?\n\n')
    while ' :\n\n' in text:
        text = text.replace(' :\n\n', ':\n\n')

    print(text, end="")
