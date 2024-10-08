#!/usr/bin/python3
"""
A script that ads all arguments in
a Python list, and then save them to a file
"""
import sys
import json

if __name__ == "__main__":
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file('add_item.json')
    except (FileNotFoundError, json.JSONDecodeError):
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, 'add_item.json')
