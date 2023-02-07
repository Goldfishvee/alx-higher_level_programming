#!/usr/bin/python3
"""
Writes a script that adds all arguments from cmd line to a Python list
then saves to a JSON file.
"""
import sys

save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"


try:
    json_list = load_file(filename)
except FileNotFoundError:
    json_list = []


json_list += sys.argv[1:]  # append items to list
save_file(json_list, filename)  # save items to file
